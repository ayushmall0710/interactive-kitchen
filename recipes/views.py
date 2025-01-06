import openai
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from inventory.models import InventoryItem
from .utils import gpt_utils
import openai

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def suggest_recipe(request):
    """
    API endpoint for generating recipe suggestions based on user input.
    Requires user authentication.
    """
    # # Validate API Key
    if not gpt_utils.OPENAI_API_KEY:
        return Response({"error": "API key not configured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Extract user details
    user = request.user
    gpt_utils.logger.info(f"Recipe request by user: {user.username}")

    # Extract and validate input data
    ingredients = request.data.get(
        'ingredients',
        list(InventoryItem.objects.filter(added_by=user.id).values('name', 'unit', 'quantity', 'expiration_date'))
    )
    cuisine = request.data.get('cuisine', 'any')
    spicy_level = request.data.get('spicy_level', 'medium')
    cooking_time = request.data.get('cooking_time', 'any')

    if not ingredients:
        return Response({"error": "'ingredients' field is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Generate recipe synchronously
        recipe = gpt_utils.generate_recipe(ingredients, cuisine, spicy_level, cooking_time)
        return Response({
            "user": {
                "username": user.username,
                "email": user.email,
            },
            "recipe": recipe
        }, status=status.HTTP_200_OK)
    except openai.OpenAIError as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
