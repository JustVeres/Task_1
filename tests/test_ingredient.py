import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *

class TestIngredient:

    @pytest.mark.parametrize(
        "type_ing, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
            (INGREDIENT_TYPE_FILLING, "sausage", 300.0)
        ]
    )
    def test_ingredient_create(self, type_ing, name, price):
        """Проверка создания модели ингредиента"""
        ing = Ingredient(type_ing, name, price)

        assert isinstance(ing.get_type(), str) == True
        assert isinstance(ing.get_name(), str) == True
        assert isinstance(ing.get_price(), float) == True

        assert ing.get_type().strip() != ""
        assert ing.get_name().strip() != ""
        assert ing.get_price() > 0

        assert ing.get_type() == type_ing
        assert ing.get_name() == name
        assert ing.get_price() == price
