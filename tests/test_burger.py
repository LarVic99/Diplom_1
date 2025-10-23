import pytest
from praktikum.burger import Burger
from data import *
from unittest.mock import Mock

class TestBurger: # Класс тестов класса Burger

    @pytest.mark.parametrize('buns_id', [0, 1]) 
    def test_set_buns_true(self, buns_id, buns_with_ingred): # тестирование метода добавления булки
        burger = Burger()
        mock_bun = buns_with_ingred[0][buns_id] # [булки], [id булки]
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @pytest.mark.parametrize('ingred_id', [0, 1])
    def test_add_ingredient_true(self, ingred_id, buns_with_ingred): # тестирование метода добавления ингридиента
        burger = Burger()
        mock_ingred = buns_with_ingred[1][ingred_id] # [ингридиенты], [id ингридиента]
        burger.add_ingredient(mock_ingred)
        # Проверяем, что ингредиент добавился в список
        assert burger.ingredients[0] == mock_ingred

    def test_remove_ingredient_true(self, buns_with_ingred): # тестирование метода удаления ингредиента
        burger = Burger()
        burger.add_ingredient(buns_with_ingred[1][0]) # добавляем первый ингредиент
        burger.remove_ingredient(0) # удаляем первый ингредиент по индексу
        # Проверяем, что список ингредиентов пуст
        assert burger.ingredients == []

    def test_move_ingredient_true(self, buns_with_ingred): # тестирование метода перемещения ингредиента
        burger = Burger()
        burger.add_ingredient(buns_with_ingred[1][0]) # добавляем первый ингредиент
        burger.add_ingredient(buns_with_ingred[1][1]) # добавляем второй
        burger.move_ingredient(1, 0) # перемещаем второй ингредиент на место первого
        # Проверяем, что второй ингредиент теперь на первом месте
        assert burger.ingredients[0] == buns_with_ingred[1][1]

    @pytest.mark.parametrize('id', [0, 1])
    def test_get_price_true(self, id, buns_with_ingred): # тестирование метода получения цены
        burger = Burger()
        burger.set_buns(buns_with_ingred[0][id]) # установить булку по id
        burger.add_ingredient(buns_with_ingred[1][id]) # добавить ингридиент по id
        # Проверка, что цена равна сумме цен булки (умноженной на 2) и ингредиента
        assert burger.get_price() == (buns_with_ingred[0][id].get_price() * 2 + buns_with_ingred[1][id].get_price())

    @pytest.mark.parametrize('id', [0, 1])
    def test_get_receipt(self, id, buns_with_ingred): # тестирование метода получения чека
        burger = Burger()
        burger.set_buns(buns_with_ingred[0][id]) # устанавливаем булку
        burger.add_ingredient(buns_with_ingred[1][id]) # добавляем ингредиент
        # Проверка, что чек совпадает с ожидаемым, вызовом метода get_my_receipt
        assert burger.get_receipt() == BunsWithIngred.get_my_receipt(buns_with_ingred[0][id], buns_with_ingred[1][id])

    # Дополнительные тесты для полного покрытия методов

    def test_burger_with_only_buns(self, buns_with_ingred):
        burger = Burger()
        burger.set_buns(buns_with_ingred[0][0]) # только булка
        expected_price = buns_with_ingred[0][0].get_price() * 2
        # Проверка цены без ингредиентов
        assert burger.get_price() == expected_price
        # Проверка чека
        expected_receipt = BunsWithIngred.get_my_receipt(
            buns_with_ingred[0][0],
            []
        )
        assert burger.get_receipt() == expected_receipt

    def test_burger_without_ingredients(self, buns_with_ingred):
        burger = Burger()
        burger.set_buns(buns_with_ingred[0][0]) # установка булки
        # без ингредиентов
        assert burger.get_price() == buns_with_ingred[0][0].get_price() * 2
        # чек без ингредиентов
        expected_receipt = BunsWithIngred.get_my_receipt(
            buns_with_ingred[0][0],
            []
        )
        assert burger.get_receipt() == expected_receipt
        
    def test_remove_ingredient_invalid_index(self, buns_with_ingred):
        burger = Burger()
        burger.add_ingredient(buns_with_ingred[1][0])
        # Проверка исключения или поведения при неверном индексе удаления
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)

    def test_move_ingredient_invalid_indices(self, buns_with_ingred):
        burger = Burger()
        burger.add_ingredient(buns_with_ingred[1][0])
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 10)

    def test_get_price_without_bun(self, buns_with_ingred):
        burger = Burger()
        burger.add_ingredient(buns_with_ingred[1][0])
    # Если булка не установлена — цена равна сумме ингредиентов (или 0)
        assert burger.get_price() == buns_with_ingred[1][0].get_price()

    def test_get_receipt_without_bun(self, buns_with_ingred):
        burger = Burger()
        burger.add_ingredient(buns_with_ingred[1][0])
    # Проверяем чек без булки — в зависимости от реализации
        expected_receipt = BunsWithIngred.get_my_receipt(None, [buns_with_ingred[1][0]])
        assert burger.get_receipt() == expected_receipt


@pytest.fixture
def buns_with_ingred():
    # Создаем мок-объекты для булок
    mock_bun1 = Mock()
    mock_bun1.get_name.return_value = 'Булка классическая'
    mock_bun1.get_price.return_value = 50
    mock_bun1.get_type.return_value = 'BUN'

    mock_bun2 = Mock()
    mock_bun2.get_name.return_value = 'Булка с кунжутом'
    mock_bun2.get_price.return_value = 60
    mock_bun2.get_type.return_value = 'BUN'

    # Создаем мок-объекты для ингредиентов
    mock_ingr1 = Mock()
    mock_ingr1.get_name.return_value = 'Салат'
    mock_ingr1.get_price.return_value = 15
    mock_ingr1.get_type.return_value = 'INGREDIENT'

    mock_ingr2 = Mock()
    mock_ingr2.get_name.return_value = 'Соус'
    mock_ingr2.get_price.return_value = 10
    mock_ingr2.get_type.return_value = 'INGREDIENT'

    return [
        [mock_bun1, mock_bun2],      # Булки
        [mock_ingr1, mock_ingr2]     # Ингредиенты
    ]
