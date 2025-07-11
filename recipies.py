import csv
import os

RECIPE_FILE = 'recipes.csv'

def add_recipe():
    title = input("Enter recipe title: ")
    ingredients = input("Enter ingredients (comma-separated): ")
    instructions = input("Enter instructions: ")

    with open(RECIPE_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, ingredients, instructions])
    print(f"Recipe '{title}' added.")

def view_recipes():
    if not os.path.exists(RECIPE_FILE):
        print("No recipes found.")
        return

    with open(RECIPE_FILE, 'r') as file:
        reader = csv.reader(file)
        print("\nRecipes:")
        for row in reader:
            print(f"Title: {row[0]}, Ingredients: {row[1]}, Instructions: {row[2]}")

def search_recipes():
    query = input("Enter title or ingredient to search: ")
    found = False

    with open(RECIPE_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if query.lower() in row[0].lower() or query.lower() in row[1].lower():
                print(f"Title: {row[0]}, Ingredients: {row[1]}, Instructions: {row[2]}")
                found = True
    if not found:
        print("No matching recipes found.")

def edit_recipe():
    title = input("Enter the title of the recipe you want to edit: ")
    recipes = []

    with open(RECIPE_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == title:
                new_title = input("Enter new title (leave blank to keep the same): ")
                ingredients = input("Enter new ingredients (leave blank to keep the same): ")
                instructions = input("Enter new instructions (leave blank to keep the same): ")

                new_title = new_title if new_title else title
                ingredients = ingredients if ingredients else row[1]
                instructions = instructions if instructions else row[2]

                recipes.append([new_title, ingredients, instructions])
            else:
                recipes.append(row)

    with open(RECIPE_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(recipes)
    print(f"Recipe '{title}' updated.")

def delete_recipe():
    title = input("Enter the title of the recipe you want to delete: ")
    recipes = []

    with open(RECIPE_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != title:
                recipes.append(row)

    with open(RECIPE_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(recipes)
    print(f"Recipe '{title}' deleted if it existed.")
