import inspect
import sys


def plus(a, b):
    return a + b


def test_01():
    assert plus(2, 2) == 4


def test_02():
    assert plus(100, 9) == 108, "Неверный результат"


def test_03():
    assert plus(-1, 1) == 0


def test_zero():
    assert plus(0, 0) == 0


# all_obj = globals().copy()
# exists_errors = False
# for name, value in all_obj.items():
#     if name.startswith('test_') and inspect.isfunction(value):
#         try:
#             print(f'exec {name}')
#             value()
#             print(f'{name} PASSED')
#         except Exception as error:
#             print(f'{name} FAILED {error}')
#             exists_errors = True
#
# if exists_errors:
#     sys.exit(1)