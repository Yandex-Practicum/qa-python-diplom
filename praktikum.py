from typing import List

from bun import Bun
from burger import Burger
from database import Database
from ingredient import Ingredient


def main():
    # Инициализируем базу данных
    database: Database = Database()

    # Создадим новый бургер
    burger: Burger = Burger()

    # Считаем список доступных булок из базы данных
    buns: List[Bun] = database.available_buns()

    # Считаем список доступных ингредиентов из базы данных
    ingredients: List[Ingredient] = database.available_ingredients()

    # Соберём бургер
    burger.set_buns(buns[0])

    burger.add_ingredient(ingredients[1])
    burger.add_ingredient(ingredients[4])
    burger.add_ingredient(ingredients[3])
    burger.add_ingredient(ingredients[5])

    # Переместим слой с ингредиентом
    burger.move_ingredient(2, 1)

    # Удалим ингредиент
    burger.remove_ingredient(3)

    # Распечатаем рецепт бургера
    print(burger.get_receipt())


if __name__ == "__main__":
    main()
