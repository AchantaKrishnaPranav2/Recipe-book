from recipies import add_recipe, view_recipes, search_recipes, edit_recipe, delete_recipe

def main():
    while True:
        print("\nRecipe Organizer")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Search Recipes")
        print("4. Edit Recipe")
        print("5. Delete Recipe")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_recipe()
        elif choice == "2":
            view_recipes()
        elif choice == "3":
            search_recipes()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
