from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    with pytest.raises(TypeError):
        Dish("miojo", "biscoito")

    with pytest.raises(ValueError):
        Dish("miojo", 0)

    dish = Dish("miojo", 8.00)
    dish2 = Dish("miojo", 8.00)
    dish3 = Dish("arroz", 10.00)

    assert repr(dish) == "Dish('miojo', R$8.00)"
    assert dish.name == "miojo"

    assert dish.__eq__(dish2) is True
    assert dish.__eq__(dish3) is False

    assert hash(dish) == hash(dish2)
    assert hash(dish) != hash(dish3)

    ingredient1 = Ingredient("salmão")
    ingredient2 = Ingredient("camarão")

    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)

    assert dish.get_ingredients() == {
        Ingredient("salmão"),
        Ingredient("camarão"),
    }

    assert dish.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
