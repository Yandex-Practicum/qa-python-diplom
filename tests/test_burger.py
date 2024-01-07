import allure
import pytest
from unittest.mock import Mock, patch

from burger import Burger
from data import BUN_NAME, BUN_PRICE, BUN2_NAME, BUN2_PRICE, SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE, FILLING_TYPE, \
    FILLING_NAME, FILLING_PRICE


class TestBurger:
    """
    Тесты методов класса Burger.
    """

    #
    # Тесты метода set_buns() - добавление булок
    #
    @allure.title('Проверяем метод set_buns - добавление булок: 1 булка')
    def test_set_buns(self, setup_bun):
        burger = Burger()
        mock_bun = setup_bun
        burger.set_buns(mock_bun)

        # проверяем, что булка добавлена
        assert (burger.bun is not None and
                burger.bun.name is BUN_NAME and
                burger.bun.price is BUN_PRICE)

    @allure.title('Проверяем метод set_buns() - добавление булок: 2 булки')
    def test_set_buns_2_buns(self, setup_bun, setup_bun2):
        burger = Burger()
        # создаем и добавляем булку 1
        mock_bun = setup_bun
        burger.set_buns(mock_bun)
        # создаем и добавляем булку 2
        mock_bun2 = setup_bun2
        burger.set_buns(mock_bun2)

        # проверяем, что добавлена булка 2
        assert (burger.bun is not None and
                burger.bun.name is BUN2_NAME and
                burger.bun.price is BUN2_PRICE)

    #
    # Тесты метода add_ingredient() - добавление ингредиента
    #
    @allure.title('Проверяем метод add_ingredient() - добавление ингредиентов: 1 ингредиент')
    def test_add_ingredient_one_ingredient(self, setup_sauce):
        burger = Burger()
        # создаем и добавляем 1 ингредиент - соус
        mock_sauce = setup_sauce
        burger.add_ingredient(mock_sauce)

        # проверяем, что в списке 1 ингредиент - соус
        assert len(burger.ingredients) == 1

    @allure.title('Проверяем метод add_ingredient() - добавление ингредиентов: 2 ингредиента')
    @pytest.mark.parametrize('ingredient1_type, ingredient2_type', [
        [SAUCE_TYPE, FILLING_TYPE],  # соус и начинка
        [FILLING_TYPE, SAUCE_TYPE],  # начинка и соус
        [SAUCE_TYPE, SAUCE_TYPE],  # 2 соуса
        [FILLING_TYPE, FILLING_TYPE]  # 2 начинки
    ])
    def test_add_ingredient_two_ingredients(self, setup_sauce, setup_filling,
                                            ingredient1_type, ingredient2_type):
        burger = Burger()
        # создаем 2 ингредиента - соус и начинка
        mock_sauce = setup_sauce
        mock_filling = setup_filling
        # Добавляем 1-й ингредиент
        if ingredient1_type == SAUCE_TYPE:
            burger.add_ingredient(mock_sauce)
        else:
            burger.add_ingredient(mock_filling)
        # Добавляем 2-й ингредиент
        if ingredient2_type == SAUCE_TYPE:
            burger.add_ingredient(mock_sauce)
        else:
            burger.add_ingredient(mock_filling)

        # проверяем, что в списке 2 добавленных ингредиента
        assert (len(burger.ingredients) == 2 and
                burger.ingredients[0].type == ingredient1_type and
                burger.ingredients[1].type == ingredient2_type)

    @allure.title('Проверяем метод add_ingredient() - добавление 6 ингредиентов: 3 соуса и 3 начинки')
    def test_add_ingredient_6_ingredients(self, setup_sauce, setup_filling, get_burger_with_6_ingredients):
        burger = get_burger_with_6_ingredients
        # проверяем, что в списке 6 ингредиентов
        assert len(burger.ingredients) == 6

    #
    # Тесты метода remove_ingredient() - удаление ингредиента
    #
    @allure.title('Проверяем метод remove_ingredient() - удаление ингредиента: 1 ингредиент в списке')
    def test_remove_ingredient_one_ingredient_in_list(self, setup_sauce):
        # создаем бургер и добавляем 1 ингредиент - соус
        burger = Burger()
        mock_sauce = setup_sauce
        burger.add_ingredient(mock_sauce)
        # удаляем ингредиент
        burger.remove_ingredient(0)

        # проверяем, что список пустой
        assert len(burger.ingredients) == 0

    @allure.title('Проверяем метод remove_ingredient() - удаление ингредиента: 2 ингредиента в списке')
    @pytest.mark.parametrize('index', [0, 1])
    def test_remove_ingredient_two_ingredients_in_list(self, setup_sauce, setup_filling, index):
        burger = Burger()
        # создаем 2 ингредиента - соус и начинка
        mock_sauce = setup_sauce
        mock_filling = setup_filling
        # добавляем 2 ингредиента - соус и начинка
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # удаляем ингредиент с индексом index (0 или 1)
        burger.remove_ingredient(index)
        if index is 0:
            expected_type = FILLING_TYPE
        else:
            expected_type = SAUCE_TYPE

        # проверяем, что в списке остался один ингредиент - не тот, который был удален
        assert (len(burger.ingredients) is 1 and
                burger.ingredients[0].type == expected_type)

    @allure.title('Проверяем метод remove_ingredient() - удаление ингредиента: пустой список')
    def test_remove_ingredient_empty_list_no_changes(self):
        burger = Burger()
        burger.remove_ingredient(0)

        # проверяем что программа не сломалась и список остался пустым
        assert len(burger.ingredients) == 0

    @allure.title('Проверяем метод remove_ingredient() - удаление ингредиента: неправильный индекс')
    def test_remove_ingredient_invalid_index_no_changes(self, setup_sauce, setup_filling):
        # создаем бургер и 2 ингредиента и добавляем их (с индексами 0 и 1)
        burger = Burger()
        mock_sauce = setup_sauce
        mock_filling = setup_filling
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # пытаемся удалить ингредиент с индексом 2
        burger.remove_ingredient(2)

        # проверяем что программа не сломалась и в списке осталось 2 ингредиента
        assert len(burger.ingredients) == 2

    #
    # Тесты метода move_ingredient() - перемещение ингредиента
    #
    @allure.title(
        'Проверяем метод move_ingredient() - перемещение ингредиента: 2 ингредиента в списке, поменять индексы')
    @pytest.mark.parametrize('index_before, index_after', [[0, 1], [1, 0]])
    def test_move_ingredient_move_1_and_2(self, setup_sauce, setup_filling, index_before, index_after):
        # создаем бургер и 2 ингредиента и добавляем их (с индексами 0 и 1)
        burger = Burger()
        mock_sauce = setup_sauce
        mock_filling = setup_filling
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # перемещаем ингредиент с индексом index_before на место index_after
        burger.move_ingredient(index_before, index_after)

        # проверяем что в списке осталось 2 элемента и они поменялись местами
        assert (len(burger.ingredients) == 2 and
                burger.ingredients[0].type == FILLING_TYPE and
                burger.ingredients[1].type == SAUCE_TYPE)

    @allure.title('Проверяем метод move_ingredient() - перемещение ингредиента: 2 ингредиента, тот же индекс')
    @pytest.mark.parametrize('index', [0, 1])
    def test_move_ingredient_the_same_index(self, setup_sauce, setup_filling, index):
        # создаем бургер и 2 ингредиента и добавляем их (с индексами 0 и 1)
        burger = Burger()
        mock_sauce = setup_sauce
        mock_filling = setup_filling
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        # перемещаем ингредиент с индексом index на то же место
        burger.move_ingredient(index, index)

        # проверяем что в списке остались 2 элемента на тех же местах
        assert (len(burger.ingredients) == 2 and
                burger.ingredients[0].type == SAUCE_TYPE and
                burger.ingredients[1].type == FILLING_TYPE)

    @allure.title('Проверяем метод move_ingredient() -  перемещение ингредиента: пустой список')
    def test_move_ingredient_empty_list(self):
        # создаем бургер с пустым списком ингредиентов
        burger = Burger()
        burger.move_ingredient(0, 1)

        # проверяем что программа не сломалась и список остался пустым
        assert len(burger.ingredients) == 0

    @allure.title('Проверяем метод move_ingredient() -  перемещение ингредиента: неправильный индекс')
    @pytest.mark.parametrize('index_before, index_after', [[0, 2], [2, 1], [3, 5]])
    def test_move_ingredient_invalid_index(self, setup_sauce, setup_filling, index_before, index_after):
        # создаем бургер и 2 ингредиента и добавляем их (с индексами 0 и 1)
        burger = Burger()
        mock_sauce = setup_sauce
        mock_filling = setup_filling
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        # перемещаем ингредиент с индексом index_before на место index_after
        burger.move_ingredient(index_before, index_after)

        # проверяем что программа не сломалась и в списке остались 2 ингредиента
        assert len(burger.ingredients) == 2

    #
    # Тесты метода get_price() - получение стоимости бургера
    #
    @allure.title('Проверяем метод get_price() - получение стоимости бургера')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    @pytest.mark.parametrize('has_buns, has_sauce, has_filling, has_price', [
        [True, True, True, 400],  # булки и 2 ингредиента
        [True, False, False, 100],  # только булки
        [True, True, False, 200],  # булки и соус
        [False, True, False, 100],  # только соус без булок
        [False, False, False, 0]  # "пустой" бургер - без булок и ингредиентов
    ])
    def test_get_price(self,
                       mock_ingredient_class,
                       mock_bun_class,
                       has_buns, has_sauce, has_filling, has_price):
        # создаем моки для булок и ингредиентов
        # назначаем возвращаемое значение мокам для метода get_price()
        mock_bun = Mock()
        mock_bun.get_price.return_value = BUN_PRICE
        mock_sauce = Mock()
        mock_sauce.get_price.return_value = SAUCE_PRICE
        mock_filling = Mock()
        mock_filling.get_price.return_value = FILLING_PRICE
        # создаем бургер и добавляем в него булки и ингредиенты
        burger = Burger()
        if has_buns:
            burger.set_buns(mock_bun)
        if has_sauce:
            burger.add_ingredient(mock_sauce)
        if has_filling:
            burger.add_ingredient(mock_filling)

        # проверяем, что метод get_price() возвращает правильную стоимость
        assert burger.get_price() == has_price

    #
    # Тесты метода get_receipt() - получение рецепта бургера
    #
    @allure.title('Проверяем метод get_receipt() - получение рецепта бургера')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    @patch('burger.Burger.get_price', return_value=500)
    @pytest.mark.parametrize('has_buns, has_sauce, has_filling', [
        [True, True, True],        # булки и 2 ингредиента
        [True, False, False],      # только булки
        [True, True, False],       # булки и соус
        [False, True, False],      # только соус без булок
        [False, False, False]     # "пустой" бургер - без булок и ингредиентов
    ])
    def test_get_receipt(self,
                         mock_burger_get_price,
                         mock_ingredient_class,
                         mock_bun_class,
                         has_buns, has_sauce, has_filling):
        # создаем моки для булок и ингредиентов
        # назначаем возвращаемое значение для методов get_name() и get_type()
        mock_bun = Mock()
        mock_bun.get_name.return_value = BUN_NAME
        mock_bun.get_price.return_value = BUN_PRICE
        mock_sauce = Mock()
        mock_sauce.get_type.return_value = SAUCE_TYPE
        mock_sauce.get_name.return_value = SAUCE_NAME
        mock_sauce.get_price.return_value = SAUCE_PRICE
        mock_filling = Mock()
        mock_filling.get_type.return_value = FILLING_TYPE
        mock_filling.get_name.return_value = FILLING_NAME
        mock_filling.get_price.return_value = FILLING_PRICE

        # создаем бургер
        burger = Burger()
        if has_buns:
            burger.set_buns(mock_bun)
        if has_sauce:
            burger.add_ingredient(mock_sauce)
        if has_filling:
            burger.add_ingredient(mock_filling)

        # получаем рецепт
        receipt = burger.get_receipt()

        #print(f'\n===============================\n{receipt}\n===============================\n')

        # проверяем что рецепт получен
        assert type(receipt) is str and len(receipt) > 0
        # проверяем что рецепт полный - указаны названия всех ингредиентов
        receipt = receipt.lower()
        receipt_is_full = True
        if has_buns:
            receipt_is_full = receipt_is_full and BUN_NAME.lower() in receipt
        if has_sauce:
            receipt_is_full = receipt_is_full and SAUCE_NAME.lower() in receipt
        if has_filling:
            receipt_is_full = receipt_is_full and FILLING_NAME.lower() in receipt
        assert receipt_is_full

