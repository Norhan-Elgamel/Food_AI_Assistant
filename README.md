# Food_AI_Assistant
Python desktop app using Gemini AI for ingredient recognition and recipe generation
README for Food_AI_Assistant
🍳 Food AI Assistant
A professional desktop application that leverages Artificial Intelligence to bridge the gap between image recognition and meal preparation.

🚀 Overview
This project was developed during my internship at Smart Vision Technology. The application allows users to upload an image of a dish, uses the Gemini AI API to identify ingredients, and matches them against a local inventory to suggest recipes and identify missing items.

✨ Features
AI Image Analysis: Uses Google Gemini API to extract ingredients from food photos.

Fuzzy Matching: Implements fuzzy search logic to match AI results with local database naming conventions.

Inventory Management: Distinguishes between "Available" and "Missing" ingredients.

Recipe Generation: Provides step-by-step cooking instructions and estimated cooking times.

Professional UX: Built with a clean Python Tkinter interface.

🛠️ Tech Stack
Language: Python 3.x

GUI Library: Tkinter

AI Model: Google Gemini API

Database: SQLite / CSV (Inspired by Kaggle's "What's Cooking" dataset)

Environment Management: python-dotenv for API security.

📂 Dataset Credit
The recipe logic and ingredient mapping are based on the Kaggle "What's Cooking?" Dataset.
