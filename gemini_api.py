import google.generativeai as genai
from config import API_KEY

genai.configure(api_key=API_KEY)

# Use supported model
model = genai.GenerativeModel("gemini-2.5-flash")

# -------- IMAGE → INGREDIENTS --------
def get_ingredients_from_image(image_path):
    image_file = genai.upload_file(image_path)

    response = model.generate_content([
        "List food ingredients as a comma-separated list.",
        image_file
    ])

    return [i.strip().lower() for i in response.text.split(",")]

# -------- TEXT → INGREDIENTS --------
def get_ingredients_from_text(prompt):
    response = model.generate_content(prompt)
    return [i.strip().lower() for i in response.text.split(",")]

# -------- RECIPE INSTRUCTIONS --------
def get_recipe_instructions(prompt):
    response = model.generate_content(prompt)
    return response.text
