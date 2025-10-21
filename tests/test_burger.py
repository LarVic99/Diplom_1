import sys 
sys.path.append('..')
import pytest
import pytest_cov
from burger import Burger
from data import *

class TestBurger: # Класс тестов класса Burger
    
    @pytest.mark.parametrize('buns_id', [0, 1]) 
    def test_set_buns_true(self, buns_id, buns_with_ingred): # тестирование метода добавления булки
        burger = Burger()
        mock_bun = buns_with_ingred[0][buns_id]
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @pytest.mark.parametrize('ingred_id', [0, 1])
    def test_add_ingredient_true(self, ingred_id, buns_with_ingred): # тестирование метода добавления ингридиента
        burger = Burger()
        mock_ingred = buns_with_ingred[1][ingred_id] # [ингридиент] [id ингридиента]
        burger.add_ingredient(mock_ingred)
        assert burger.ingredients[0] == mock_ingred

    def test_remove_ingredient_true(self, buns_with_ingred): # тестирование метода удаления ингредиента
        burger = Burger()
        burger.add_ingredient(buns_with_ingred[1][0]) # Добавляем 1-ый ингридиент
        burger.remove_ingredient(0) # Удаляем 1-ый ингридиент
        assert burger.ingredients == []

    def test_move_ingredient_true(self, buns_with_ingred): # тестирование метода перемещения ингредиента
        burger = Burger()
        burger.add_ingredient(buns_with_ingred[1][0]) # Добавляем 1-ый ингридиент
        burger.add_ingredient(buns_with_ingred[1][1]) # Добавляем 2-ой ингридиент
        burger.move_ingredient(1, 0) # [1- index, 0 - new_index] - перемещаем 2-ой ингредиент со 2 места на 1 место
        assert burger.ingredients[0] == buns_with_ingred[1][1] # Проверяем что на 1 месте находится 2-ой ингридиент
        
    @pytest.mark.parametrize('id', [0, 1])
    def test_get_price_true(self, id, buns_with_ingred): # тестирование метода получения цены
        burger = Burger()
        burger.set_buns(buns_with_ingred[0][id]) # id булки
        burger.add_ingredient(buns_with_ingred[1][id]) # id ингридиента
        assert burger.get_price() == (buns_with_ingred[0][id].get_price()*2 + buns_with_ingred[1][id].get_price())

    @pytest.mark.parametrize('id', [0, 1])
    def test_get_receipt(self, id, buns_with_ingred): # тестирование метода получения чека
        burger = Burger()
        burger.set_buns(buns_with_ingred[0][id]) # id булки
        burger.add_ingredient(buns_with_ingred[1][id]) # id ингридиента
        assert burger.get_receipt() == BunsWithIngred.get_my_receipt(buns_with_ingred[0][id], buns_with_ingred[1][id])
