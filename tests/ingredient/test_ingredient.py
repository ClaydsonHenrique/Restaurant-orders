from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


def test_instantiate_ingredient_with_valid_arguments():
    ingredient = Ingredient("Tomato", ["vegetarian", "gluten-free"])
    assert isinstance(ingredient, Ingredient)


def test_check_ingredient_name():
    name = "Tomato"
    ingredient = Ingredient(name, [])
    assert ingredient.name == name


def test_verify_ingredient_restrictions():
    restrictions = ["vegetarian", "gluten-free"]
    ingredient = Ingredient("Tomato", restrictions)
    assert ingredient.restrictions == set(restrictions)


def test_representation_of_ingredient():
    ingredient = Ingredient("Tomato", ["vegetarian", "gluten-free"])
    expected_repr = (
        "Ingredient(name='Tomato', "
        "restrictions=['vegetarian', 'gluten-free'])"
    )
    assert repr(ingredient) == expected_repr


def test_compare_two_equal_ingredients():
    ingredient1 = Ingredient("Tomato", ["vegetarian", "gluten-free"])
    ingredient2 = Ingredient("Tomato", ["vegetarian", "gluten-free"])
    assert ingredient1 == ingredient2


def test_verify_hash_of_ingredient():
    ingredient1 = Ingredient("Tomato", ["vegetarian", "gluten-free"])
    ingredient2 = Ingredient("Tomato", ["vegetarian", "gluten-free"])
    assert hash(ingredient1) == hash(ingredient2)


def test_compare_hash_of_different_ingredients():
    ingredient1 = Ingredient("Tomato", ["vegetarian", "gluten-free"])
    ingredient2 = Ingredient("Onion", ["vegetarian", "gluten-free"])
    assert hash(ingredient1) != hash(ingredient2)


def test_compare_different_ingredients():
    ingredient1 = Ingredient("Tomato", ["vegetarian", "gluten-free"])
    ingredient2 = Ingredient("Onion", ["vegetarian", "gluten-free"])
    assert ingredient1 != ingredient2


def test_representation_of_ingredient_incorrect():
    ingredient = Ingredient("Tomato", ["vegetarian", "gluten-free"])
    assert repr(ingredient) != "Ingredient(name='Tomato')"
