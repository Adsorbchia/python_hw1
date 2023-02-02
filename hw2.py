# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а 
# некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# # 2
#Решение. Монетку гербом вверх, условно обозначим 1, решкой -0, соответственно вводим 0 или 1 
# n = int(input("Введите кол-во монет " ))
# count1=0
# count2=0
# for _ in range(n):
#     x=int(input())
#     if x==0:
#         count1+=1
#     else:
#          count2+=1
# if count1>count2:
#     print (count2)
# else:
#     print (count1)


#Задача 12: Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# # Помогите Кате отгадать задуманные Петей числа.
# Решение
# решаем задачу методом перебора, проверяя совпадает ли условие
# summa = int(input("Введите число " ))
# p = int(input("Введите число " ))
# n = int(input("Введите число попыток  " ))
# for _ in range (n):
#     x = int(input("Введите число x= "))
#     y =  int(input("Введите число y= "))
#     if x+y==summa and x*y==p:
#         print (x,y)
#     else:
#         print("совпадений нет, попытайтесь еще раз")



# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
# n = int(input("Введите число " ))
# i=0
# a=2**i
# while a<n:
#     print(a)
#     i+=1
#     a=2**i

