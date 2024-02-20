from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredient1 = Ingredient("queijo provolone")
    ingredient2 = Ingredient("massa de lasanha")
    assert ingredient1 != ingredient2
    ingredient1 = Ingredient("salmão")
    ingredient2 = Ingredient("salmão")
    assert hash(ingredient1) == hash(ingredient2)
    ingredient1 = Ingredient("frango")
    ingredient2 = Ingredient("frango")
    assert ingredient1 == ingredient2
    ingredient1 = Ingredient("carne")
    ingredient2 = Ingredient("creme de leite")
    assert not ingredient1 == ingredient2
    ingredient1 = Ingredient("bacon")
    assert ingredient1.name == "bacon"
    assert ingredient1.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    ingredient1 = Ingredient("caldo de carne")
    assert repr(ingredient1) == "Ingredient('caldo de carne')"
    ingredient1 = Ingredient("massa de lasanha")
    ingredient2 = Ingredient("ovo")
    assert not hash(ingredient1) == hash(ingredient2)
    ingredient1 = Ingredient("massa de lasanha")
    assert ingredient1.restrictions != {Restriction.ANIMAL_DERIVED}
