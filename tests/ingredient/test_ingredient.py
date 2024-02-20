# import pytest
from src.models.ingredient import Ingredient


def test_instantiate_ingredient_with_valid_arguments():
    ingredient = Ingredient("Tomato")
    assert isinstance(ingredient, Ingredient)


def test_check_ingredient_name():
    name = "Tomato"
    ingredient = Ingredient(name)
    assert ingredient.name == name


def test_verify_ingredient_restrictions():
    restrictions = {"vegetarian", "gluten-free"}
    ingredient = Ingredient("Tomato")
    assert ingredient.restrictions == restrictions


def test_representation_of_ingredient():
    ingredient = Ingredient("Tomato")
    expected_repr = "Ingredient(name='Tomato')"
    assert repr(ingredient) == expected_repr


def test_compare_two_equal_ingredients():
    ingredient1 = Ingredient("Tomato")
    ingredient2 = Ingredient("Tomato")
    assert ingredient1 == ingredient2


def test_verify_hash_of_ingredient():
    ingredient1 = Ingredient("Tomato")
    ingredient2 = Ingredient("Tomato")
    assert hash(ingredient1) == hash(ingredient2)


def test_compare_hash_of_different_ingredients():
    ingredient1 = Ingredient("Tomato")
    ingredient2 = Ingredient("Onion")
    assert hash(ingredient1) != hash(ingredient2)


def test_compare_different_ingredients():
    ingredient1 = Ingredient("Tomato")
    ingredient2 = Ingredient("Onion")
    assert ingredient1 != ingredient2


def test_representation_of_ingredient_incorrect():
    ingredient = Ingredient("Tomato")
    assert repr(ingredient) != "Ingredient(name='Tomato')"
