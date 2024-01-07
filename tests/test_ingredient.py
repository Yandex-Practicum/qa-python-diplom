import allure
import pytest

from ingredient import Ingredient

from data import SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE


class TestIngredient:
    """
    Тесты методов класса Ingredient.
    """

    @allure.title('Проверяем конструктор ингредиента __init__()')
    def test_init_ingredient(self):
        sauce = Ingredient(SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE)
        assert sauce.type is SAUCE_TYPE and sauce.name is SAUCE_NAME and sauce.price is SAUCE_PRICE

    @allure.title('Проверяем конструктор __init__() с пустым или незаданным типом ингредиента')
    @pytest.mark.parametrize('ingredient_type', ['', None])
    def test_init_ingredient_type(self, ingredient_type):
        sauce = Ingredient(ingredient_type, SAUCE_NAME, SAUCE_PRICE)
        assert sauce.type is ingredient_type

    @allure.title('Проверяем конструктор __init__() с пустым или незаданным названием ингредиента')
    @pytest.mark.parametrize('name', ['', None])
    def test_init_ingredient_name(self, name):
        sauce = Ingredient(SAUCE_TYPE, name, SAUCE_PRICE)
        assert sauce.name == name

    @allure.title('Проверяем конструктор __init__() с нулевой или незаданной стоимостью ингредиента')
    @pytest.mark.parametrize('price', [0.0, None])
    def test_init_ingredient_price(self, price):
        sauce = Ingredient(SAUCE_TYPE, SAUCE_NAME, price)
        assert sauce.price == price

    @allure.title('Проверяем метод get_type() - получить тип ингредиента')
    def test_get_type(self):
        sauce = Ingredient(SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE)
        assert sauce.get_type() is SAUCE_TYPE

    @allure.title('Проверяем метод get_name() - получить название ингредиента')
    def test_get_name(self):
        sauce = Ingredient(SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE)
        assert sauce.get_name() is SAUCE_NAME

    @allure.title('Проверяем метод get_price() - получить стоимость ингредиента')
    def test_get_price(self):
        sauce = Ingredient(SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE)
        assert sauce.get_price() is SAUCE_PRICE


