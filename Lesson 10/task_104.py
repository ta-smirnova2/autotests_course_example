# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
@pytest.mark.usefixtures('RunTimeClass')
class TestExample:

    @pytest.mark.usefixtures('RunTimeTest')
    def test_1(self):
        print("Выполняется тест_1")

    def test_2(self):
        print("Выполняется тест_2")

    @pytest.mark.usefixtures('RunTimeTest')
    def test_3(self):
        print("Выполняется тест_3")
