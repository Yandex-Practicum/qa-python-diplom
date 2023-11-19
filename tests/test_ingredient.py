import pytest
from ingredient import Ingredient
import ingredient_types


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', [
        [ingredient_types.INGREDIENT_TYPE_SAUCE, 'barbecue', 10],
        [ingredient_types.INGREDIENT_TYPE_FILLING, 'tomatoes', 15]
    ])
    def test_get_price_valid_price_returned_correct_price_ingredient(self, ingredient_type, name, price):
        my_ingredient = Ingredient(ingredient_type, name, price)
        expected_result = my_ingredient.get_price()
        assert expected_result == price

    @pytest.mark.parametrize('ingredient_type, name, price', [
        [ingredient_types.INGREDIENT_TYPE_SAUCE, 'garlic', 8.5],
        [ingredient_types.INGREDIENT_TYPE_FILLING, 'bacon', 25]
    ])
    def test_get_name_valid_name_returned_correct_name_ingredient(self, ingredient_type, name, price):
        my_ingredient = Ingredient(ingredient_type, name, price)
        expected_result = my_ingredient.get_name()
        assert expected_result == name

    @pytest.mark.parametrize('ingredient_type, name, price', [
        [ingredient_types.INGREDIENT_TYPE_SAUCE, 'cheese', 6.5],
        [ingredient_types.INGREDIENT_TYPE_FILLING, 'pickles', 12.5]
    ])
    def test_get_type_valid_type_returned_correct_type_ingredient(self, ingredient_type, name, price):
        my_ingredient = Ingredient(ingredient_type, name, price)
        expected_result = my_ingredient.get_type()
        assert expected_result == ingredient_type
