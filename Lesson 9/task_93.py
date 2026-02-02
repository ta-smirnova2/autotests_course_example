# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
from pathlib import Path

lst_sum = []
sum = 0
try:
    f = open('C:/Course/autotests_course_example/Lesson 9/test_file/task_3.txt', 'r', encoding='utf-8')
    try:
        lines = f.readlines()
        for l in lines:
            if l == '\n':
                lst_sum.append(sum)
                sum = 0
            else:
                sum += int(l[:len(l)-1])
    except Exception as e:
        print(f"{e}")
    finally:
        f.close()
except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлом")
lst_sum = sorted(lst_sum)
three_most_expensive_purchases = lst_sum[len(lst_sum)-3] + lst_sum[len(lst_sum)-2] + lst_sum[len(lst_sum)-1]


assert three_most_expensive_purchases == 202346
