import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize(
        "name",
        [
            "Bun",              # латиница
            "Булочка",          # кириллица
            "Bun123",           # буквы + цифры
            "Bun!",             # спецсимвол
            "   Bun   "         # пробелы
        ]
    )
    def test_bun_name_create(self, name):
        """Проверка создания названия для булочки"""
        bun = Bun(name, 100.0)

        assert isinstance(bun.get_name(), str)
        assert bun.get_name().strip() != ""
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "price",
        [
            0.1,        # минимально допустимое
            1.0,        # обычное
            9999.9,     # большое
            100.555,    # дробное
        ]
    )
    def test_bun_price_create(self, price):
        """Проверка создания цены для булочки"""
        bun = Bun("test bun", price)
        assert isinstance(bun.get_price(), float)
        assert bun.get_price() > 0
        assert bun.get_price() == price
