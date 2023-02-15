# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# # помощью рекурсии.
# def exponentiation_of_a_num(n,k):
#     if (k-1)==0:
#         return n

#     return (n*exponentiation_of_a_num(n, k-1))
# a=int(input("введите число "))
# b=int(input("введите число "))
# print(exponentiation_of_a_num(a, b))


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# # 4
# def summa_num(n,k):
#     if k-1==0:
#         return n+1
#     return(1+summa_num(n, k-1))
# a=int(input("введите число "))
# b=int(input("введите число "))
# print (summa_num(a, b))