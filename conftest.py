import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def mock_bun():                             # Мокаем булочку
    mock_bun = Mock()
    mock_bun.get_name.return_value = "black bun"
    mock_bun.get_price.return_value = 100.0
    return mock_bun

@pytest.fixture
def mock_ingredient_type_sauce():           # Мокаем ингредиент - соус
    mock_ingredient_type_sauce = Mock()
    mock_ingredient_type_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_ingredient_type_sauce.get_name.return_value = "sour cream"
    mock_ingredient_type_sauce.get_price.return_value = 200.0
    return mock_ingredient_type_sauce

@pytest.fixture
def mock_ingredient_type_filling():         # Мокаем ингредиент - начинка
    mock_ingredient_type_filling = Mock()
    mock_ingredient_type_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_ingredient_type_filling.get_name.return_value = "cutlet"
    mock_ingredient_type_filling.get_price.return_value = 100.0
    return mock_ingredient_type_filling
