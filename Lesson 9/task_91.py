# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
from pathlib import Path
work_dir = Path.cwd()
print(f"Текущая рабочая директория: {work_dir}")
path = Path("test_file/task1_data.txt")
lst_lines = []
try:
    f = open('C:/Course/autotests_course_example/Lesson 9/test_file/task1_data.txt', 'r', encoding='utf-8')
    try:
        lines = f.readlines()
        for l in lines:
            string = ""
            for i in range(0, len(l)):
                if not l[i].isdigit():
                    string += l[i]
            lst_lines.append(string)
    except Exception as e:
        print(f"{e}")
    finally:
        f.close()
except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлом")

try:
    f1 = open('C:/Course/autotests_course_example/Lesson 9/test_file/task1_answer.txt', 'w', encoding='utf-8')
    try:
        for l in lst_lines:
            f1.write(l)
    except Exception as e:
        print(f"{e}")
    finally:
        f1.close()
except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлом")

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
