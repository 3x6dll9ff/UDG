# def suma_prvih_n(n):
#     if n == 1:  
#         return 1
#     else:
#         return n + suma_prvih_n(n - 1) 
    
# def faktorial(n):
#     if n == 1:  
#         return 1
#     else:
#         return n * faktorial(n - 1) 
    
# n = 5
# rezultat = faktorial(n)
# print(f"Сума првих {n} бројева је: {rezultat}")


# def print_list(lista):
#     if len(lista) ==1:
#         return lista[0]
#     else:
#         print(lista[0])
#         return print_list(lista[1:])
    
# niz = ['a','b','c', 2, 3,4]
# print_list(niz)

# def string_rec(str):
#     if len(str) == 0:
#         return ""
#     else:
#         return string_rec(str[1:]) + str[0] 
    

# print(string_rec('hello'))
 
# def element(list_num):
#     if len(list_num) == 0:
#         return "Error"
#     else:
#        list_num.remove(min(list_num))
#        return element(list_num)
    
# niz = [1,2,3,4,5,6,7,8,9,10]

# hello = element(niz)
# print(hello)

# def element_rec(list_num):
#     if len(list_num) == 1:
#         return list_num
#     elif len(list_num) == 0:
#         return "Список пуст."
#     else:
        
#         return element_rec(list_num[1:]) + [list_num[0]]
    
# niz = [1,2,3,4,5,6,7,8,9,10]
    
# print(element_rec(niz))

