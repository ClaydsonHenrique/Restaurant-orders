import csv
from src.models.dish import Dish


class MenuData:
    def __init__(self, source_path: str):
        self.source_path = source_path
        self.dishes = [
            Dish(
                row["name"],
                float(row["price"]),
                {row["ingredient"]: int(row["amount"])},
            )
            for row in csv.DictReader(open(self.source_path))
        ]
        self.dishes = [
            dict(dish)
            for dish in set(frozenset(d.items()) for d in self.dishes)
        ]
