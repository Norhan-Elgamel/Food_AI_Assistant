import sqlite3
import pandas as pd

df = pd.read_csv("ingredients_list.csv")

conn = sqlite3.connect("ingredients.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT UNIQUE
)
""")

for ing in df["ingredient"].unique():
    cursor.execute(
        "INSERT OR IGNORE INTO ingredients (ingredient) VALUES (?)",
        (ing,)
    )

cursor.execute("""
CREATE TABLE IF NOT EXISTS cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT,
    quantity INTEGER
)
""")

conn.commit()
conn.close()

print("SQLite database created with",
      len(df["ingredient"].unique()),
      "unique ingredients")
