import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    """Тесты для класса Ingredient"""

    @pytest.mark.parametrize("ingredient_type,name,price", [
        ("SAUCE", "hot sauce", 100),
        ("FILLING", "cutlet", 200),
        ("SAUCE", "sour cream", 150.5),
        ("FILLING", "dinosaur", 300.75),
    ])
    def test_ingredient_initialization(self, ingredient_type, name, price):
        """Тестирование инициализации ингредиента с разными параметрами"""
        ingredient = Ingredient(ingredient_type, name, price)
        
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    @pytest.mark.parametrize("ingredient_type,name,price", [
        ("SAUCE", "hot sauce", 100),
        ("FILLING", "cutlet", 200),
    ])
    def test_get_price(self, ingredient_type, name, price):
        """Тестирование метода get_price"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type,name,price", [
        ("SAUCE", "hot sauce", 100),
        ("FILLING", "cutlet", 200),
    ])
    def test_get_name(self, ingredient_type, name, price):
        """Тестирование метода get_name"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type,name,price", [
        ("SAUCE", "hot sauce", 100),
        ("FILLING", "cutlet", 200),
    ])
    def test_get_type(self, ingredient_type, name, price):
        """Тестирование метода get_type"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type