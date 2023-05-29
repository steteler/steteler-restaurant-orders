from models.dish import Dish
from models.ingredient import Ingredient
import pandas as pd


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = {}
        self.csv_data = pd.read_csv(source_path)

        dishes = {
            name: Dish(name, price)
            for name, price, ingredient, amount
            in self.csv_data.itertuples(index=False)
        }

        for name, _, ingredient, amount in self.csv_data.itertuples(
            index=False
        ):
            data = Ingredient(ingredient)
            dishes[name].add_ingredient_dependency(data, amount)

        self.dishes.update(dishes.values())
