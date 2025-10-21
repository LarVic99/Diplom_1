import sys 
sys.path.append('..')
from unittest.mock import Mock

class BunsWithIngred:
    # Моки булок
    mock_buns = []
    mock_bun1 = Mock()
    mock_bun1.get_name.return_value = "white bun"
    mock_bun1.get_price.return_value = 200.0
    mock_bun2 = Mock()
    mock_bun2.get_name.return_value = "red bun"
    mock_bun2.get_price.return_value = 300.0
    mock_buns.append(mock_bun1)
    mock_buns.append(mock_bun2)

    # Моки ингредиентов
    mock_ingredients = []
    mock_ingredient1 = Mock()
    mock_ingredient1.get_name.return_value = "chili sauce"
    mock_ingredient1.get_price.return_value = 300.0
    mock_ingredient1.get_type.return_value = 'SAUCE'
    mock_ingredient2 = Mock()
    mock_ingredient2.get_name.return_value = "cutlet"
    mock_ingredient2.get_price.return_value = 100.0
    mock_ingredient2.get_type.return_value = 'FILLING'
    mock_ingredients.append(mock_ingredient1)
    mock_ingredients.append(mock_ingredient2)

    # Вывод сформированного рецепта для 1 булки и 1 ингредиента
    @staticmethod
    def get_my_receipt(bun, ingredient):
        my_receipt = f'(==== {bun.get_name()} ====)\n'
        my_receipt += f'= {str(ingredient.get_type()).lower()} {ingredient.get_name()} =\n'
        my_receipt += f'(==== {bun.get_name()} ====)\n\n'
        my_receipt += f'Price: {bun.get_price() * 2 + ingredient.get_price()}'
        return my_receipt
