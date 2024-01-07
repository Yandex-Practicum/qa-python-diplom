import allure
import pytest
from unittest.mock import Mock

from burger import Burger
from data import BUN_NAME, BUN_PRICE, BUN2_NAME, BUN2_PRICE, SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE, FILLING_TYPE, FILLING_NAME, FILLING_PRICE


@allure.title('Создаем мок булки')
@pytest.fixture
def setup_bun():
    mock_bun = Mock()
    mock_bun.name = BUN_NAME
    mock_bun.price = BUN_PRICE
    mock_bun.return_value.get_name = BUN_NAME
    mock_bun.return_value.get_price = BUN_PRICE
    return mock_bun


@allure.title('Создаем мок булки 2')
@pytest.fixture
def setup_bun2():
    mock_bun = Mock()
    mock_bun.name = BUN2_NAME
    mock_bun.price = BUN2_PRICE
    mock_bun.return_value.get_name = BUN2_NAME
    mock_bun.return_value.get_price = BUN2_PRICE
    return mock_bun


@allure.title('Создаем мок соуса')
@pytest.fixture
def setup_sauce():
    mock_sauce = Mock()
    mock_sauce.type = SAUCE_TYPE
    mock_sauce.name = SAUCE_NAME
    mock_sauce.price = SAUCE_PRICE
    mock_sauce.return_value.get_type = SAUCE_TYPE
    mock_sauce.return_value.get_name = SAUCE_NAME
    mock_sauce.return_value.get_price = SAUCE_PRICE
    return mock_sauce


@allure.title('Создаем мок начинки')
@pytest.fixture
def setup_filling():
    mock_filling = Mock()
    mock_filling.type = FILLING_TYPE
    mock_filling.name = FILLING_NAME
    mock_filling.price = FILLING_PRICE
    mock_filling.return_value.get_type = FILLING_TYPE
    mock_filling.return_value.get_name = FILLING_NAME
    mock_filling.return_value.get_price = FILLING_PRICE
    return mock_filling

@allure.title('Создаем бургер с 6 мок-ингредиентами')
@pytest.fixture
def get_burger_with_6_ingredients(setup_sauce, setup_filling):
    # создаем бургер
    burger = Burger()
    # добавляем 3 соуса
    mock_sauce1 = setup_sauce
    burger.add_ingredient(mock_sauce1)
    mock_sauce2 = setup_sauce
    burger.add_ingredient(mock_sauce2)
    mock_sauce3 = setup_sauce
    burger.add_ingredient(mock_sauce3)
    # добавляем 3 начинки
    mock_filling1 = setup_filling
    burger.add_ingredient(mock_filling1)
    mock_filling2 = setup_filling
    burger.add_ingredient(mock_filling2)
    mock_filling3 = setup_filling
    burger.add_ingredient(mock_filling3)
    # возвращаем бургер
    return burger


