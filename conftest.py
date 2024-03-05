import pytest
import praktikum.ingredient_types

from unittest.mock import Mock
from praktikum.burger import Burger

@pytest.fixture
def cooked_burger_fixture():
    # Создание экземпляра класса Burger
    burger = Burger()

    # Создание и настройка заглушки для булочки
    mock_bun = Mock()
    mock_bun.get_name.return_value = "Краторная булка"
    mock_bun.get_price.return_value = 11.0

    # Создание и настройка заглушки для начинки
    mock_filling = Mock()
    mock_filling.get_name.return_value = "Хрустящие минеральные кольца"
    mock_filling.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
    mock_filling.get_price.return_value = 3.0

    # Создание и настройка заглушки для соуса
    mock_sauce = Mock()
    mock_sauce.get_name.return_value = "Соус традиционный галактический"
    mock_sauce.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE
    mock_sauce.get_price.return_value = 7

    # Настройка бургера с заглушками ингредиентов
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_filling)
    burger.add_ingredient(mock_sauce)

    return burger