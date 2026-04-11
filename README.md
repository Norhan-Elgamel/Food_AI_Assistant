# Food_AI_Assistant
Python desktop app using Gemini AI for ingredient recognition and recipe generation

Project Overview
This is a desktop application developed during my internship at Smart Vision Technology. It uses Artificial Intelligence to identify food ingredients from images and provide recipe suggestions.

Key Features

AI Identification: Connects to the Gemini API to analyze food photos.

Ingredient Matching: Compares AI results with a local database based on the Kaggle "What's Cooking" dataset.

Smart Logic: Uses fuzzy search to find ingredients even if the names don't match perfectly.

Recipe Output: Generates full cooking instructions and missing ingredient lists.

Setup Requirements

Python 3.x

Tkinter (for the interface)

A .env file containing your Gemini API key (hidden for security).
