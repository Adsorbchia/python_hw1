# Задача № 1
# Напишите функцию read_last(lines, file), которая
#  будет открывать определенный файл file и выводить на печать построчно последние 
# строки в количестве lines (на всякий случай проверим, что задано положительное целое число). 
# # Протестируем функцию на файле «article.txt» 

# def read_last(lines, file):
#     with open ("article.txt","r",encoding="utf-8") as file:
#         text = file.read().splitlines()
#         for el in range(len(text)-1 - lines+1,len(text)):
#             print(("\t"+ text[el] + "\n "))

# num = int(input("Введите число "))
# if num <0:
#     num=num*-1
#     read_last(num, "article.txt")
# else:
#     read_last(num, "article.txt")


# Задача №2 
# Требуется реализовать функцию longest_words(file), которая выводит слово,
#  имеющее максимальную длину (или список слов, если таковых несколько.

# def longest_words(file):
#     with open ("article.txt","r",encoding="utf-8") as file:
#         maxx=0
#         text = file.read().splitlines()
#         st = " "
#         my_list=[]
#         my_dict={}
#         for line in text:
#             st += line +" "
#             my_list= st.split()
#         for  word in my_list:
#             for i in word:
#                 if i in word:
#                     my_dict[word]= my_dict.get(word,0)+1
#         maxx = max(my_dict.values())
#         v= list (my_dict.values())
#         k = list (my_dict.keys())
#         for i in range(len(v)):
#             if v[i]==maxx:
#                 print (k[i])       
# longest_words("article.txt")

# ДОП ЗАДАЧА.
# Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена заполнения 
# всего бассейна только одной данной работающей трубой (в часах). 
# Затем после пустой строки перечислены трубы, которые будут заполнять бассейн. 
# Сколько минут на это потребуется?
# Номер трубы соответствует номеру строки, в которой записана ее производительность.
# Результат запишите в файл time.txt
import random
n= int (input("Введите количество труб N = "))
with open ("pipes.txt","w",encoding="utf-8") as file:
    pipes_list =[]
    for i in range(n):
        pipes_list.append(random.randint(1, 4))
    pipes_list = list(map(str,pipes_list))
    for num in pipes_list:
        file.write(num+"\n" )
      
with open ("pipes.txt","a",encoding="utf-8") as file:
    pipes_list2=[]
    for i in range(n):
        pipes_list2.append(random.randint(1, n-1))
        pipes_list2 = list(map(str,pipes_list2))
    file.write("\n")
    for num in pipes_list2:
        file.write(num)

with open ("pipes.txt","r",encoding="utf-8") as file:
    pipes = []
    working_time=[]
    res=[]
    for i in range(n+2):
        line=file.readline()
        if i==n+1:
            pipes.append(line.strip())
        elif i <n:
            working_time.append(line.strip())
    working_time=list(map(int, working_time))       
    pipes=" ".join(map(str, pipes))
    pipes=set(list(map(int,pipes)))
    print(pipes) # номера труб,которые заполняют бассейн
    print(working_time) # время заполнения  в часах 
    for ind in pipes:
        res.append(1/working_time[ind-1]) 
       
    print(res)
    time = (1/sum(res))*60
    time = str(time)
    print (time)
with open ("time.txt","w",encoding="utf-8") as file:
    file.write(time)
