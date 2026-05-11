import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from threading import Thread

from gemini_api import (
    get_ingredients_from_image,
    get_recipe_instructions
)
from database import fetch_all_ingredients, add_to_cart
from fuzzy_match import match_ingredients

# -------------------------
# Globals
# -------------------------
available_items = []
missing_items = []

# -------------------------
# Image Processing
# -------------------------
def process_image(file_path):
    status_label.config(text="⏳ Analyzing image...", fg="#ff9800")

    try:
        ai_ingredients = get_ingredients_from_image(file_path)
        db_ingredients = fetch_all_ingredients()

        matched, unmatched = match_ingredients(ai_ingredients, db_ingredients)

        available_items.clear()
        missing_items.clear()

        for item in matched:
            available_items.append(item)
            add_to_cart(item)

        for item in unmatched:
            missing_items.append(item)

        update_result_box()
        status_label.config(text="✔ Done", fg="green")

    except Exception as e:
        status_label.config(text="❌ Error", fg="red")
        messagebox.showerror("Error", str(e))

# -------------------------
# Upload Image
# -------------------------
def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Images", "*.jpg *.png *.jpeg")]
    )
    if not file_path:
        return

    img = Image.open(file_path)
    img.thumbnail((280, 280))
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk

    Thread(target=process_image, args=(file_path,), daemon=True).start()

# -------------------------
# Update Result Box
# -------------------------
def update_result_box():
    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)

    result_text.insert(tk.END, "✅ Available Ingredients:\n\n", "good")
    for item in available_items:
        result_text.insert(tk.END, f"- {item}\n")

    result_text.insert(tk.END, "\n❌ Missing Ingredients:\n\n", "bad")
    for item in missing_items:
        result_text.insert(tk.END, f"- {item}\n")

    result_text.config(state="disabled")

# -------------------------
# View Cart
# -------------------------
def view_cart():
    if not available_items:
        messagebox.showinfo("Cart", "No available ingredients yet.")
        return

    messagebox.showinfo(
        "Available Ingredients",
        "\n".join(available_items)
    )

# -------------------------
# Get Recipe (Gemini)
# -------------------------
def get_recipe():
    if not available_items:
        messagebox.showwarning("No Ingredients", "Upload an image first.")
        return

    prompt = f"""
Create a clean, well-structured recipe using ONLY these ingredients:

{", ".join(available_items)}

Format exactly as:
Title
---
Ingredients list
---
Step-by-step instructions
---
Cooking time
"""

    recipe = get_recipe_instructions(prompt)

    recipe_window = tk.Toplevel(root)
    recipe_window.title("🍲 Recipe Instructions")

    text = tk.Text(
        recipe_window,
        wrap=tk.WORD,
        font=("Arial", 12),
        width=70,
        height=28
    )
    text.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

    scrollbar = tk.Scrollbar(recipe_window, command=text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text.config(yscrollcommand=scrollbar.set)

    text.insert(tk.END, recipe)
    text.config(state=tk.DISABLED)

# -------------------------
# UI
# -------------------------
root = tk.Tk()
root.title("Food AI Assistant")
root.geometry("700x820")
root.configure(bg="#f5f5f5")

tk.Label(
    root,
    text="🍽 Food AI Assistant",
    font=("Arial", 22, "bold"),
    bg="#f5f5f5"
).pack(pady=15)

tk.Button(
    root,
    text="📸 Upload Image",
    bg="#2196f3",
    fg="white",
    font=("Arial", 12),
    width=26,
    command=upload_image
).pack(pady=6)

tk.Button(
    root,
    text="🛒 View Cart",
    bg="#ff9800",
    fg="white",
    font=("Arial", 12),
    width=26,
    command=view_cart
).pack(pady=6)

tk.Button(
    root,
    text="🍲 Get Recipe",
    bg="#4caf50",
    fg="white",
    font=("Arial", 12),
    width=26,
    command=get_recipe
).pack(pady=10)

status_label = tk.Label(
    root,
    text="Waiting for image...",
    fg="blue",
    bg="#f5f5f5"
)
status_label.pack(pady=10)

image_label = tk.Label(root, bg="#f5f5f5")
image_label.pack(pady=10)

result_text = tk.Text(root, height=14, width=65)
result_text.tag_configure("good", foreground="green", font=("Arial", 11, "bold"))
result_text.tag_configure("bad", foreground="red", font=("Arial", 11, "bold"))
result_text.config(state="disabled")
result_text.pack(pady=10)

root.mainloop()
