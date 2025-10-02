import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    """Тесты для класса Burger"""

    def test_initialization(self):
        """Тестирование инициализации бургера"""
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, mock_bun):
        """Тестирование установки булочки"""
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        """Тестирование добавления ингредиента"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, mock_ingredient):
        """Тестирование удаления ингредиента"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        """Тестирование перемещения ингредиента"""
        burger = Burger()
        
        ingredient1 = Mock()
        ingredient1.get_name.return_value = "Ингредиент 1"
        ingredient2 = Mock()
        ingredient2.get_name.return_value = "Ингредиент 2"
        
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].get_name.return_value == "Ингредиент 2"
        assert burger.ingredients[1].get_name.return_value == "Ингредиент 1"

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected", [
        (100, [], 200),
        (100, [50], 250),
        (100, [50, 75], 325),
    ])
    def test_get_price(self, bun_price, ingredient_prices, expected):
        """Тестирование расчета цены"""
        burger = Burger()
        
        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)
        
        for price in ingredient_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)
        
        assert burger.get_price() == expected

    def test_get_receipt(self, mock_bun, mock_ingredient):
        """Тестирование формирования чека"""
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        
        assert mock_bun.get_name() in receipt
        assert mock_ingredient.get_name() in receipt
        assert str(burger.get_price()) in receipt