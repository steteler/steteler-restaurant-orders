from models.dish import Dish
from models.ingredient import Ingredient
import pandas as pd


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.csv_data = pd.read_csv(source_path)

        dishes = {}

        for data in self.csv_data.itertuples(index=False):
            dish, price, ingredient, recipe_amount = data
            if dish not in dishes:
                dish_info = Dish(dish, price)
                dishes[dish] = dish_info
                self.dishes.add(dish_info)

            ingredient_data = Ingredient(ingredient)
            dishes[dish].add_ingredient_dependency(
                ingredient_data,
                recipe_amount
            )
