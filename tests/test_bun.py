import pytest
from unittest.mock import Mock
from praktikum.bun import Bun


class TestBun:
    """Тесты для класса Bun"""
    
    # Параметризация для тестирования разных значений названия и цены
    @pytest.mark.parametrize("name,price", [
        ("Краторная булка N-200i", 1255),
        ("Флюоресцентная булка R2-D3", 988),
        ("Обычная булка", 100.5),
        ("", 0),
        ("Специальная булка", 999.99)
    ])
    def test_bun_initialization(self, name, price):
        """Тестирование инициализации булочки с разными параметрами"""
        bun = Bun(name, price)
        
        assert bun.name == name
        assert bun.price == price
    
    @pytest.mark.parametrize("name,price", [
        ("Краторная булка N-200i", 1255),
        ("Флюоресцентная булка R2-D3", 988),
        ("Обычная булка", 100.5)
    ])
    def test_get_name(self, name, price):
        """Тестирование метода get_name с разными названиями"""
        bun = Bun(name, price)
        
        assert bun.get_name() == name
        # Мок для проверки вызова метода
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = name
        assert mock_bun.get_name() == name
        mock_bun.get_name.assert_called_once()
    
    @pytest.mark.parametrize("name,price", [
        ("Краторная булка N-200i", 1255),
        ("Флюоресцентная булка R2-D3", 988),
        ("Обычная булка", 100.5),
        ("Дорогая булка", 0),
        ("Бюджетная булка", 999.99)
    ])
    def test_get_price(self, name, price):
        """Тестирование метода get_price с разными ценами"""
        bun = Bun(name, price)
        result = bun.get_price()
        assert result == price