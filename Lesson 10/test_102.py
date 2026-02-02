# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


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

# Два ненулевых числа
@pytest.mark.smoke
def test_01():
    assert all_division(10, 5) == 2

# Несколько ненулевых чисел
@pytest.mark.acceptance
def test_02():
    assert all_division(100, -10, 10) == -1

# Делимое = 0, остальные - числа
def test_03():
    assert all_division(0, 8, 45) == 0

# Только один аргумент
def test_04():
    assert all_division(108) == "Недостаточно данных"

# Отутствует делимое
def test_05():
    assert all_division( None, 55) == "Некорректный формат данных"

# нечисловой формат
@pytest.mark.acceptance
def test_06():
    assert all_division( 100, "98", 55) == "Некорректный формат данных"

# Деление на 0
@pytest.mark.smoke
@pytest.mark.acceptance
def test_div_by_zero():
    assert all_division(100, 0) is None
