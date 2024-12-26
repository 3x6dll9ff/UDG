# napisati rekurzivnu funkciju koja stepenuje broj x 

# def grade_stepen(x,n):
#     if n == 0:
#         return 1
#     elif x == 1:
#         return 1
#     elif x == 0:
#         return 0
#     else:
#         return x * grade_stepen(x, n-1)
    

# print(grade_stepen(2,4))


# napisati rekurzivnu funkciju koja prima pozitivan cjeli broj i vraca sumu njegivih cifata

# def summ(n):
#     if int(n) == 0:
#         return 0
#     else:
#      last_digit = n % 10
#      return last_digit + summ(n // 10)
    
# print(summ(25))

# napisati rekurzivnu funkciju koja broji koliko puta se odredjeno slovo/karaktera pojavljuje u zadatom stringu

# def rekurs_broj(str,charakter):
#     if len(str) == 0:
#         return 0
#     elif str[0] == charakter:
#         return 1 + rekurs_broj(str[1:], charakter)
#     else:
#         return rekurs_broj(str[1:], charakter)
    
# print(rekurs_broj("hello_world", 'l'))

# napisati rekurzivnu funkciju koja ima 2 broja a i b , u vraca zbir svih vijelih brojeva izmedzu nih, ukljucujuci i a i b, Postaviti da je a uvjek manje od b.


# def summ(a,b):
#     if int(a)== 0 and int(b)!= 0:
#         return 
#     elif int(b)== 0 and int(a)!= 0:
#         return a
#     else:
#      last_digit_a = a % 10
#      last_digit_b = b % 10
#      return last_digit_a + summ(n // 10)
    
# print(summ(25,55))


# variabla = ['dejan', 1 ,{}, (0, )]

