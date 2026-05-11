import sqlite3

conn = sqlite3.connect("ingredients.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM ingredients")
count = cursor.fetchone()[0]

print("Total ingredients in DB:", count)
