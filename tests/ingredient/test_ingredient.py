from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("morango")
    ingredient2 = Ingredient("paçoca")

    assert hash(ingredient1) == hash("morango")
    assert hash(ingredient1) != hash(ingredient2)

    assert ingredient1 == ingredient1
    assert ingredient1 != ingredient2

    assert repr(ingredient1) == "Ingredient('morango')"

    assert ingredient1.name == "morango"

    assert ingredient1.restrictions == set()
