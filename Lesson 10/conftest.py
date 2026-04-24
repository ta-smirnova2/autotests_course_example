from datetime import datetime as dtm
import pytest

# фикстура для класса
@pytest.fixture(scope="class")
def RunTimeClass():
    print("Начало выполнения класса", dtm.now().strftime('%Y-%m-%d %H:%M:%S'))
    yield
    print("Окончание выполнения класса", dtm.now().strftime('%Y-%m-%d %H:%M:%S'))


# фикстура для тестов
#@pytest.fixture(autouse=True)   ### если выполнять для всех тестов без исключения
@pytest.fixture(scope='function')
def RunTimeTest():
    print("Начало выполнения теста", dtm.now().strftime('%Y-%m-%d %H:%M:%S'))
    yield
    print("Окончание выполнения теста", dtm.now().strftime('%Y-%m-%d %H:%M:%S'))
