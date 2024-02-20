import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction


def test_dish():
    dish1 = Dish("Coxinha", 6.50)
    assert isinstance(dish1, Dish)
    assert dish1.name == "Coxinha"
    assert dish1.price == 6.50

    dish2 = Dish("Coxinha", 6.50)
    assert dish1 == dish2
    assert hash(dish1) == hash(dish2)

    dish3 = Dish("Pizza", 49.90)
    assert dish1 != dish3
    assert hash(dish1) != hash(dish3)

    assert repr(dish1) == f"Dish('Coxinha', R${dish1.price:.2f})"

    with pytest.raises(TypeError):
        Dish(dish1.name, "6.50")

    with pytest.raises(ValueError):
        Dish(dish1.name, -6.50)

    ingredient1 = Ingredient("bacon")
    dish1.add_ingredient_dependency(ingredient1, 2)
    assert dish1.recipe.get(ingredient1) == 2

    assert dish1.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    assert dish1.get_ingredients() == {ingredient1}

    assert dish1.recipe.get(ingredient1) == 2

    with pytest.raises(AssertionError):
        assert dish1.name == "Pizza"

    with pytest.raises(AssertionError):
        assert hash(dish1) == hash(dish3)

    with pytest.raises(AssertionError):
        assert dish1 == dish3
