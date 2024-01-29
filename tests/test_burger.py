import praktikum.ingredient_types

from praktikum.burger import Burger
from unittest.mock import Mock


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        mock_buns = Mock()
        mock_buns.get_name.return_value = 'Bun'
        mock_buns.get_price.return_value = 10.0

        burger.set_buns(mock_buns)

        assert burger.bun.get_name() == 'Bun'
        assert burger.bun.get_price() == 10.0

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'lime'
        mock_ingredient.get_price.return_value = 5.0
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING

        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0].get_price() == 5.0
        assert burger.ingredients[0].get_name() == 'lime'
        assert burger.ingredients[0].get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_FILLING

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, cooked_burger):
        first_ingredient = cooked_burger.ingredients[0]
        second_ingredient = cooked_burger.ingredients[1]

        cooked_burger.move_ingredient(0, 1)

        assert first_ingredient == cooked_burger.ingredients[1]
        assert second_ingredient == cooked_burger.ingredients[0]

    def test_get_price(self, cooked_burger):
        assert cooked_burger.get_price() == 40.0
        assert cooked_burger.bun.get_price() * 2 == 20.0

    def test_get_receipt(self, cooked_burger):
        expected_receipt = "(==== brioche ====)\n"
        expected_receipt += "= filling cheese =\n"
        expected_receipt += "= sauce ketchunes =\n"
        expected_receipt += "(==== brioche ====)\n\n"
        expected_receipt += "Price: 40.0"

        assert expected_receipt == cooked_burger.get_receipt()
