import pytest
from praktikum.bun import Bun
from data.bun_data import BunData as BD

@pytest.fixture # Фикстура для модели бургера
def bun():
    bun = Bun(BD.name, BD.price)
    return bun
