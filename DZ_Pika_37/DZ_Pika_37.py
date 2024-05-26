import requests
import random

recipes = []
for _ in range(3):
    response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
    recipe = response.json()["meals"][0]
    recipes.append(recipe)

first_recipe = recipes[0]
category = first_recipe["strCategory"]
print(f"Категория первого блюда: {category}")

response = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}")
category_meals = response.json()["meals"]

butter_meals = []
for meal in category_meals:
    meal_id = meal["idMeal"]
    response = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}")
    meal_details = response.json()["meals"][0]
    if "Butter" in meal_details["strIngredient1"] or "Butter" in meal_details["strIngredient2"] or "Butter" in meal_details["strIngredient3"] or "Butter" in meal_details["strIngredient4"] or "Butter" in meal_details["strIngredient5"] or "Butter" in meal_details["strIngredient6"] or "Butter" in meal_details["strIngredient7"] or "Butter" in meal_details["strIngredient8"] or "Butter" in meal_details["strIngredient9"] or "Butter" in meal_details["strIngredient10"] or "Butter" in meal_details["strIngredient11"] or "Butter" in meal_details["strIngredient12"] or "Butter" in meal_details["strIngredient13"] or "Butter" in meal_details["strIngredient14"] or "Butter" in meal_details["strIngredient15"]:
        butter_meals.append(meal_details["strMeal"])

print("Блюда из выбранной категории, в которых есть масло:")
for meal in butter_meals:
    print(meal)
