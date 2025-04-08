import streamlit as st

# Initialize recipe data
if "recipes" not in st.session_state:
    st.session_state.recipes = {
        "Pancakes": {
            "Ingredients": [
                "1 cup flour",
                "2 eggs",
                "1 cup milk",
                "2 tbsp sugar",
                "1 tsp baking powder"
            ],
            "Instructions": "Mix ingredients and cook on a skillet until golden."
        },
        "Scrambled Eggs": {
            "Ingredients": ["2 eggs", "Salt", "Butter"],
            "Instructions": "Beat eggs with salt, cook in butter until fluffy."
        }
    }

# App Title
st.title("📖 My Recipe Book")

# Sidebar Navigation
menu = st.sidebar.selectbox("Menu", ["View Recipes", "Add New Recipe"])

# View Recipes
if menu == "View Recipes":
    st.header("📋 Recipes List")
    recipe_names = list(st.session_state.recipes.keys())

    if recipe_names:
        selected = st.selectbox("Select a recipe", recipe_names)
        if selected:
            recipe = st.session_state.recipes[selected]
            st.subheader(selected)
            st.markdown("### 🧂 Ingredients")
            for ing in recipe["Ingredients"]:
                st.write(f"- {ing}")
            st.markdown("### 🔪 Instructions")
            st.write(recipe["Instructions"])
    else:
        st.info("No recipes available. Add one in the sidebar!")

# Add New Recipe
elif menu == "Add New Recipe":
    st.header("➕ Add a New Recipe")
    name = st.text_input("Recipe Name")
    ingredients = st.text_area("Ingredients (one per line)")
    instructions = st.text_area("Instructions")

    if st.button("Add Recipe"):
        if name and ingredients and instructions:
            st.session_state.recipes[name] = {
                "Ingredients": ingredients.splitlines(),
                "Instructions": instructions.strip()
            }
            st.success(f"✅ '{name}' added to your recipe book!")
        else:
            st.error("Please fill out all fields.")
