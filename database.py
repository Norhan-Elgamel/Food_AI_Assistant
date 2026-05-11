import sqlite3

# Allow SQLite to be used across threads
conn = sqlite3.connect("ingredients.db", check_same_thread=False)
cursor = conn.cursor()

# Fetch all ingredients from DB
def fetch_all_ingredients():
    cursor.execute("SELECT ingredient FROM ingredients")
    return [row[0] for row in cursor.fetchall()]

# Add ingredient to cart
def add_to_cart(ingredient):
    cursor.execute("INSERT INTO cart (ingredient, quantity) VALUES (?, 1)", (ingredient,))
    conn.commit()

# Fetch cart items
def fetch_cart_items():
    cursor.execute("SELECT ingredient, quantity FROM cart")
    return cursor.fetchall()
