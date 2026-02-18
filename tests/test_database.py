from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *

class TestDatabase:

    def test_available_buns_returns_list_of_buns(self, database):
        """Метод available_buns возвращает список булок"""
        buns = database.available_buns()

        assert isinstance(buns, list)
        assert all(isinstance(b, Bun) for b in buns)
        assert len(buns) > 0

    def test_available_ingredients_returns_list(self, database):
        """Метод available_ingredients возвращает список ингредиентов"""
        ingredients = database.available_ingredients()

        assert isinstance(ingredients, list)
        assert all(isinstance(i, Ingredient) for i in ingredients)
        assert len(ingredients) > 0

    def test_buns_have_name_and_price(self, database):
        """У булок есть имя и цена, пригодные для использования"""
        for bun in database.available_buns():
            assert bun.get_name()
            assert bun.get_price() > 0

    def test_ingredients_have_valid_fields(self, database):
        """Ингредиенты содержат пригодные данные"""
        for ingredient in database.available_ingredients():
            assert ingredient.get_name()
            assert ingredient.get_price() > 0
            assert ingredient.get_type() in [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
