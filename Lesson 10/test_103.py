# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest

# def all_division(*arg1):
#
#     if len(arg1[0]) == 1:
#         return "Недостаточно данных"
#     elif all(isinstance(x, (int, float)) for x in arg1[0]) is False:
#         return "Некорректный формат данных"
#     elif arg1[0][0] is None:
#         return "Отсутствует делимое"
#     else:
#         try:
#             division = arg1[0][0]
#             for i in arg1[0][1:]:
#                 division /= i
#             return division
#         except ZeroDivisionError:
#             return None

def all_division(*arg1):

    if len(arg1) == 1:
        return "Недостаточно данных"
    elif all(isinstance(x, (int, float)) for x in arg1) is False:
        return "Некорректный формат данных"
    elif arg1[0] is None:
        return "Отсутствует делимое"
    else:
        try:
            division = arg1[0]
            for i in arg1[1:]:
                division /= i
            return division
        except ZeroDivisionError:
            return None


#@pytest.mark.parametrize('*arg1, result', [(10, 5, 2), (100, -10, 10, 1), (0, 6, 0), (100), (None, 55), (100, "98", 55), (100, 0)])
#@pytest.mark.parametrize('*arg1, result', [(10, 5, 2), (100, -10, 10, 1)])
#@pytest.mark.parametrize('param', [(2, 10, 5), (-1, 100, -10, 10), (0, 0, 6)])
@pytest.mark.parametrize('array_data, result', [((10, 5), 2), ((100, -10, 10), -1), ((0, 6), 0)])
def test_division(array_data, result):
    assert all_division(*array_data) == result

# def test_division(param):
#     assert all_division(param[1:]) == param[0]
