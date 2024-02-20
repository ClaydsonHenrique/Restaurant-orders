import pytest
from src.models.dish import Dish


def test_dish_instantiation():
    dish = Dish(
        "Lasanha", 15.99, {"Massa": 200, "Molho de Tomate": 150, "Queijo": 100}
    )
    assert dish.name == "Lasanha"
    assert dish.price == 15.99
    assert dish.recipe == {"Massa": 200, "Molho de Tomate": 150, "Queijo": 100}


def test_dish_equality():
    dish1 = Dish(
        "Lasanha", 15.99, {"Massa": 200, "Molho de Tomate": 150, "Queijo": 100}
    )
    dish2 = Dish(
        "Lasanha", 15.99, {"Massa": 200, "Molho de Tomate": 150, "Queijo": 100}
    )
    assert dish1 == dish2


@pytest.mark.xfail(strict=True)
def test_dish_name_mismatch():
    dish1 = Dish(
        "Lasanha", 15.99, {"Massa": 200, "Molho de Tomate": 150, "Queijo": 100}
    )
    dish2 = Dish(
        "Pizza", 15.99, {"Massa": 200, "Molho de Tomate": 150, "Queijo": 100}
    )
    assert dish1 == dish2


@pytest.mark.xfail(strict=True)
def test_dish_hash_mismatch():
    dish1 = Dish(
        "Lasanha", 15.99, {"Massa": 200, "Molho de Tomate": 150, "Queijo": 100}
    )
    dish2 = Dish(
        "Lasanha", 15.99, {"Massa": 200, "Molho de Tomate": 150, "Queijo": 100}
    )
    assert hash(dish1) == hash(dish2)


def test_dish_equality_different_objects():
    dish1 = Dish(
        "Lasanha", 15.99, {"Massa": 200, "Molho de Tomate": 150, "Queijo": 100}
    )
    dish2 = Dish(
        "Pizza", 15.99, {"Massa": 200, "Molho de Tomate": 150, "Queijo": 100}
    )
    assert dish1 != dish2  # Verifica se os pratos são diferentes
