import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize(
        "name, price",
        [
            ("test one", 100.0),
            ("test two", 200.0),
            ("test three", 500.0)
        ]
    )
    def test_bun_create(self, name, price):
        """Проверка создания булочки"""
        bun = Bun(name, price)

        assert isinstance(bun.get_name(), str) == True
        assert isinstance(bun.get_price(), float) == True

        assert bun.get_name().strip() != ""
        assert bun.get_price() > 0

        assert bun.get_name() == name
        assert bun.get_price() == price
