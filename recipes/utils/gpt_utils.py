import openai
import asyncio
import os
from dotenv import load_dotenv
import logging

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
        f"You are a recipe assistant. Based on the following ingredients: {ingredients}, prioritize ingredients that are close to expiration and "
        f"suggest 3 recipes. The recipes should match the cuisine: {cuisine} (if any then change in output based on recipe), have a spicy level: {spicy_level}, "
        f"and take approximately {cooking_time} to cook. Provide detailed instructions and ingredient quantities in this format:\n" +
        "[{{\"recipe\": \"<recipe_name>\", \"ingredients\": [{{\"name\": \"<ingredient_name>\", \"quantity\": <quantity>, \"unit\": \"<unit>\", \"expiration_date\": \"<date>\"}}], \"cuisine\": \"<cuisine>\", \"spicy_level\": \"<spicy_level>\", \"cooking_time\": <time_in_minutes>, \"instructions\": \"<instructions>\"}}]"
    )
    try:
        response = await aclient.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant specializing in recipe suggestions."},
            {"role": "user", "content": prompt}
        ])
        print(response)
        return response.choices[0].message.content
    except openai.OpenAIError as e:
        logger.error(f"OpenAI API Error: {e}")
        raise e

def generate_recipe(*args, **kwargs):
    """
    Synchronously wraps the async recipe generation function.
    """
    return asyncio.run(generate_recipe_async(*args, **kwargs))