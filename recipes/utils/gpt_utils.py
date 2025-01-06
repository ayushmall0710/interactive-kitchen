import openai
import asyncio
import os
from dotenv import load_dotenv
import logging
import json
load_dotenv()

# Configure logging
logger = logging.getLogger(__name__)

# Load API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not OPENAI_API_KEY:
    logger.error("OpenAI API Key not found. Ensure it's set in the environment variables.")

aclient = openai.AsyncOpenAI(api_key=OPENAI_API_KEY)

# Helper Function to Call OpenAI API
async def generate_recipe_async(ingredients, cuisine, spicy_level, cooking_time):
    """
    Asynchronously generates a recipe suggestion using OpenAI API.
    """
    prompt = (
            f"You are a recipe assistant API. Based on the following ingredients: {ingredients}, prioritize ingredients that are close to expiration and "
            f"suggest upto 3 recipes. Ensure that all main (non-optional) ingredients in the recipes are selected only from the provided ingredient list. "
            f"The recipes should match the cuisine: {cuisine} (if any, then reflect in the output based on the recipe), have a spicy level: {spicy_level}, "
            f"and take approximately {cooking_time} to cook. Provide detailed instructions and ingredient quantities in this format:\n" +
            "[{{\"recipe\": \"<recipe_name>\", \"ingredients\": [{{\"name\": \"<ingredient_name>\", \"quantity\": <quantity>, \"unit\": \"<unit>\", \"expiration_date\": \"<date>\"}}], \"cuisine\": \"<cuisine of suggested recipe>\", \"spicy_level\": \"<spicy_level of suggested recipe>\", \"cooking_time\": <time_in_minutes of suggested recipe>, \"overview\": \"<overview>\", \"instructions\": \"<instructions>\"}}]"
    )

    try:
        response = await aclient.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant specializing in recipe suggestions."},
            {"role": "user", "content": prompt}
        ])
        print(response)
        return json.loads(response.choices[0].message.content)
    except openai.OpenAIError as e:
        logger.error(f"OpenAI API Error: {e}")
        raise e

def generate_recipe(*args, **kwargs):
    """
    Synchronously wraps the async recipe generation function.
    """
    return asyncio.run(generate_recipe_async(*args, **kwargs))