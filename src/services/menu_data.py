import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.path = source_path
        self.dishes = set()
        self._load_menu_data()

    def _load_menu_data(self):
        with open(self.path, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for line in reader:
                dish_name, dish_price, ingredient_name, ingredient_amount = (
                    line
                )

                dish = next(
                    (d for d in self.dishes if d.name == dish_name), None
                )
                if not dish:
                    dish = Dish(dish_name, float(dish_price))
                    self.dishes.add(dish)

                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(
                    ingredient, int(ingredient_amount)
                )
