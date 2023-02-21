# Задача № 1
# Напишите функцию read_last(lines, file), которая
#  будет открывать определенный файл file и выводить на печать построчно последние 
# строки в количестве lines (на всякий случай проверим, что задано положительное целое число). 
# # Протестируем функцию на файле «article.txt» 

# def read_last(lines, file):
#     with open ("article.txt","r",encoding="utf-8") as file:
#         text = file.read().splitlines()
#         for el in range(len(text)):
#             if el ==len(text)-1 or el==len(text)-2:
#                  print(("\t"+ text[el] + "\n ")*lines)

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