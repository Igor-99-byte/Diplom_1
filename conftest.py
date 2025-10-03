import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = "Краторная булка"
    mock.get_price.return_value = 100
    return mock


@pytest.fixture
def mock_ingredient():
    mock = Mock()
    mock.get_type.return_value = "SAUCE"
    mock.get_name.return_value = "Соус"
    mock.get_price.return_value = 50
    return mock

@pytest.fixture
def database():
    """Фикстура для создания экземпляра Database"""
    from praktikum.database import Database
    return Database()

@pytest.fixture
def sauce_ingredient():
    """Фикстура для ингредиента-соуса"""
    from praktikum.ingredient import Ingredient
    return Ingredient("SAUCE", "hot sauce", 100)


@pytest.fixture
def filling_ingredient():
    """Фикстура для ингредиента-начинки"""
    from praktikum.ingredient import Ingredient
    return Ingredient("FILLING", "cutlet", 200)