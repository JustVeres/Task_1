class TestBurger:

    def test_set_buns_with_mock(self, burger, mock_bun):
        """Проверка выбора булочки"""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_one_ingredient_with_mock(self, burger, mock_ingredient_type_sauce):
        """Проверка добавления одного ингредиента"""
        burger.add_ingredient(mock_ingredient_type_sauce)
        assert burger.ingredients[0] == mock_ingredient_type_sauce

    def test_add_two_ingredient_with_mock(self, burger, mock_ingredient_type_sauce, mock_ingredient_type_filling):
        """Проверка добавления двух ингредиентов"""
        burger.add_ingredient(mock_ingredient_type_sauce)               # type_sauce = [0]
        burger.add_ingredient(mock_ingredient_type_filling)             # type_filling = [1]
        assert burger.ingredients[0] == mock_ingredient_type_sauce
        assert burger.ingredients[1] == mock_ingredient_type_filling

    def test_remove_ingredient_with_mock(self, burger, mock_ingredient_type_sauce):
        """Проверка удаления ингредиента"""
        burger.add_ingredient(mock_ingredient_type_sauce)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_with_mock(self, burger, mock_ingredient_type_sauce, mock_ingredient_type_filling):
        """Проверка перемещения ингредиента"""
        burger.add_ingredient(mock_ingredient_type_filling)             # type_filling = [0]
        burger.add_ingredient(mock_ingredient_type_sauce)               # type_sauce = [1]
        burger.move_ingredient(0, 1)                                    # [1] → [0], [0] → [1]
        assert burger.ingredients[0] == mock_ingredient_type_sauce
        assert burger.ingredients[1] == mock_ingredient_type_filling

    def test_get_price_bun_and_ingredients_with_mock(self, burger, mock_bun, mock_ingredient_type_filling, mock_ingredient_type_sauce):
        """Проверка итоговой цены с булочкой и двумя ингредиентами"""
        burger.set_buns(mock_bun)                                       # 100 * 2 = 200
        burger.add_ingredient(mock_ingredient_type_filling)             # 100
        burger.add_ingredient(mock_ingredient_type_sauce)               # 200
        assert burger.get_price() == 500.0

    def test_get_price_only_bun_with_mock(self, burger, mock_bun):
        """Проверка итоговой цены с булочкой без ингредиентов"""
        burger.set_buns(mock_bun)                                       # 100 * 2 = 200
        assert burger.get_price() == 200.0

    def test_get_receipt_with_mock(self, burger, mock_bun, mock_ingredient_type_filling, mock_ingredient_type_sauce):
        """Проверка образования чека"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_type_filling)
        burger.add_ingredient(mock_ingredient_type_sauce)
        receipt = burger.get_receipt()
        assert "(==== black bun ====)" in receipt
        assert "= filling cutlet =" in receipt
        assert "= sauce sour cream =" in receipt
        assert "Price: 500.0" in receipt
