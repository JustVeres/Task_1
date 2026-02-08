from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestDatabase:

    def test_database_counts(self, database):
        """Проверка соответствия количества булок и ингредиентов в базе"""
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

    def test_database_types(self, database):
        """Проверка соответствия типов данных в базе"""
        assert all(isinstance(bun, Bun) for bun in database.buns)
        assert all(isinstance(ing, Ingredient) for ing in database.ingredients)

    def test_available_buns(self, database):
        """Проверка доступных булок в базе"""
        buns = database.available_buns()
        assert buns is database.buns
        assert len(buns) == 3

    def test_available_ingredients(self, database):
        """Проверка доступных ингредиентов в базе"""
        ingredients = database.available_ingredients()
        assert ingredients is database.ingredients
        assert len(ingredients) == 6

    def test_database_buns_content(self, database):
        """Проверка содержимых булок в базе"""
        names = [bun.get_name() for bun in database.buns]
        prices = [bun.get_price() for bun in database.buns]
        assert "black bun" in names
        assert "white bun" in names
        assert "red bun" in names
        assert all(price > 0 for price in prices)

    def test_database_ingredients_content(self, database):
        """Проверка содержимых ингредиентов в базе"""
        ing_names = [i.get_name() for i in database.ingredients]
        assert "hot sauce" in ing_names
        assert "sour cream" in ing_names
        assert "chili sauce" in ing_names
        assert "cutlet" in ing_names
        assert "dinosaur" in ing_names
        assert "sausage" in ing_names
