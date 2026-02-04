from data.bun_data import BunData as BD

class TestBun:
    def test_bun_get_name(self, bun):
        """Проверка названия булочки"""
        assert bun.get_name() is not None
        assert len(bun.get_name()) > 1

    def test_bun_get_price(self, bun):
        """Проверка цены булочки"""
        assert bun.get_price() is not None
        assert bun.get_price() != 0

    def test_bun_create(self, bun):
        """Проверка создания булочки"""
        assert bun.name == BD.name
        assert bun.price == BD.price
