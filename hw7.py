# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# #В русском языке 10 гласных букв:а, о, у, ы,  э, е, ё, и, ю,  я
#Решение:
text= (input("Введите текст     ")).split()
vowel_letters=[ "а", "о", "у", "ы", "э", "е", "ё", "и", "ю", "я"]
print (text)
def check_the_rhythm(array, my_list):
    my_dict={}
    a=0
    b=0
    for i,val in enumerate(array):
        for j in val:
            if j in my_list: 
                my_dict[i]= my_dict.get(i,0)+1
        print(my_dict)
    a=max(my_dict.values())
    b=min(my_dict.values())
    print(a,b)
    if a==b:
        print ("Парам пам-пам")
    else:
        print("Пам парам")

check_the_rhythm(text, vowel_letters)

# Задача 36:
#  Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая 
# принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны
#  быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
#  Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, 
# как, например, у операции умножения.
# Ввод:     
# print_operation_table(lambda x, y: x * y) Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36
#Решение:
# def print_operation_table(operation, num_rows, num_columns):
#     for x in range(1, num_rows + 1):
#         nums = []
#         for y in range(1, num_columns + 1):
#             num = operation(x, y)
#             nums.append(num)
#         print(' '.join([str(x) for x in nums]))
# operation=lambda x,y: x*y
# rows= int (input("Введите количество строк "))
# columns = int (input("Введите количество строк "))
# print_operation_table (operation, rows ,columns )