import json
import pandas as pd

with open("data/train.json", "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []
for recipe in data:
    for ing in recipe["ingredients"]:
        rows.append({"ingredient": ing.lower().strip()})

df = pd.DataFrame(rows)

df.to_csv("ingredients_list.csv", index=False)
print("CSV created with", len(df), "rows")
