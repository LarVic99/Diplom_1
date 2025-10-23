import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from data import *

# фикстура забирает моки булочек и ингредиентов и возвращает их списками в списке
@pytest.fixture()
def buns_with_ingred():
    buns = BunsWithIngred.mock_buns
    ingredients = BunsWithIngred.mock_ingredients
    return [buns, ingredients]
