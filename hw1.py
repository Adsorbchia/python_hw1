# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
# a = int(input ("Ведите трехзначное число "))
# print(a//100 + a%10 + (a%100)//10)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# s = int(input ("введите количество журавликов "))
# a = s//6 #Количество журавликов,которое сдалал каждый из мальчиков
# b = (a + a)*2 #Количество журавликов,которое сделала Катя 
# print(f"{a} {b} {a} ")

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#  Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no
# a = input ("введите номер билета ")
# b=int(a[0])+int(a[1])+int(a[2])
# c=int(a[3])+int(a[4])+int(a[5])
# if b==c:
#     print("YES")
# else:
#     print("NO")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать 
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# # 3 2 1 -> no
# n = int(input ( ))
# m = int(input ( ))
# k = int(input ( ))
# if k%n == 0 and k < n*m:
#         print("YES")
# elif k%m == 0 and k < n*m:
#         print ("YES")
# else:
#         print ("NO")