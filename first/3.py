import math

# domahi zadatak 1

# a = int(input("Введите ширину листа бумаги: "))
# b = int(input("Введите  высоту листа бумаги: "))

# povrsina = (a * b)/10
# povrsinacm = (2*(a + b))/100


# print(f" {povrsina} cм^2 \n {povrsinacm} cm ")

# domahi zadatak 2


# a = int(input("а = : "))
# b = int(input("b = : "))
# c = int(input("c = : "))

# result = math.pow(a,2) + math.pow(b,2) + math.pow(c,2) + (2 * a * b) + (2 * a * c) + (2 * b * c)

# print (f"Result : {result}")

#
# h = float(input("insert hours:  "))

# liter = h * 0.5
# liter_o = int(liter)

# print(f"He drink {liter_o} liters at {h} hours")

# zadatak 8

# P =  float(input("insert P :  "))

# pi = 3.14

# radius = math.sqrt( P/ pi) # find radius

# result = 2 * pi * radius  # find p

# print(f'Result : {result}')


# zadatak 9
# d = int(input("d = : "))
# s = int(input("s = : "))
# r = int(input("s = : "))

# d1 = d + (2*r)
# s1 = s + (2*r)

# result = 2*(d1 + s1)

# print(f'Result :  {result} - duzina terena u metrima')


# zadatak 10

# first point
# x1 = int(input("x1 = : "))
# y1 = int(input("y1 = : "))
# second point
# x2 = int(input("x2 = : "))
# y2 = int(input("y2 = : "))

# decided
# a = x2-x1  # side a
# b = y1 - y2 # side b

# c =  a * b
# d =  2 * (a+b)
# print(f' povrshina je {c} , obinma je {d} ')


# zadatak 11 eucide_distace
# first point
# x1 = int(input("x1 = : "))
# y1 = int(input("y1 = : "))
# second point
# x2 = int(input("x2 = : "))
# y2 = int(input("y2 = : "))

# a = x2-x1  # side a
# b = y1 - y2 # side b

# d = pow(a,2) + pow(b,2)

# result = math.sqrt(d)

# print (f'Result = {result}')

# zadatak 12
# first point
# x1 = int(input("x1 = : "))
# y1 = int(input("y1 = : "))
# second point
# x2 = int(input("x2 = : "))
# y2 = int(input("y2 = : "))
# third point
# x3 = int(input("x2 = : "))
# y3 = int(input("y2 = : "))

# side a
# a1 = x2 - x1
# b1 = y1 - y2
# d1 = pow(a1, 2) + pow(b1, 2)
# side1 = math.sqrt(d1)
# side b
# a2 = x2 - x3
# b2 = y2 - y3
# d2 = pow(a2, 2) + pow(b2, 2)
# side2 = math.sqrt(d2)
# side c
# a3 = x3 - x1
# b3 = y3 - y1
# d3 = pow(a3, 2) + pow(b3, 2)
# side3 = math.sqrt(d3)

# ovrshina = side1 * side2 * side3

# print(f"{povrshina}")

# zadatak 16

# x = int(input("insert kilometrs = : "))

# result = 1 + (x * 0.5)

# print(f"all price - {result}")

# zadatak 16
# x = int(input("insert price = : "))
# y = int(input("insert discont = : "))

# discont = x * (y / 100)
# result_price = x - discont

# print(f'full price with discont = {result_price}')

# ZADATAK 18
# x = int(input("insert price = : "))

# discont_down = x + (x * (0.10))
# result_price = discont_down - (discont_down * 0.10)

# print(f'full price with discont = {result_price}')

# zadatak 19
# x = int(input("insert 3 znaka = : "))

# x1 = int(x / 100)
# x2 = int(x / 10) % 10
# x3 = x % 10

# print(x1 + x2 + x3)

# zadatak 20
# x = int(input("insert 3 znaka = : "))

# x1 = int(x / 100)
# x2 = int(x / 10) % 10
# x3 = x % 10

# proizv = x1*x2*x3

# summa  =  x1 + x2 + x3

# result = proizv - summa

# print (f'Kod je {result}')


# zadatak 21
# x = int(input("insert 4 znaka = : "))

# x1 = x // 1000
# x2 = (x // 100) % 10
# x3 = (x // 10) % 10
# x4 = x % 10

# a = x1 + x4
# b = pow(x2, 2) - pow(x3, 2)

# summa = pow(a, 2) - b


# print(f"Summa kvadrata je {summa}")

# zadatak 1

# broj = int(input("insert = : "))

# if broj % 2 == 0:
#   print('se otvara')
# else:
#    print('zatvoren')

# zadatak 2

# procent = int(input("insert = : "))
# sdal = int(input("insert 1 - True / 0 - False = : "))

# if (procent >= 75) and (sdal == 1):
#    print("mozhe")
# elif sdal > 1 or sdal < 0:
#    print("wrong number")
# else:
#   print("nemozhe")

# zadatak 27

# list = [1, 2, 3, 4, 5, -5, 1, 5]

# skolvo = 0
# i = 0
# for i in range(i, len(list)):
#     if list[i] > 0:
#         print(f'{list[i]}')
#         skolvo += 1

#     else:
#         print("idi naxyi")

# print(f"{skolvo} summa jednaco celih cisel")


# Zadatak 28

"""
list = [1, 2, 3, 4, 5, -5, 1, 5]

skolvo = 0
i = 0
for i in range(i, len(list)):

    if list[i] > 0:
        print(f'{list[i]}')
        skolvo += 1

    else:
        print("idi naxyi")

print(f"{skolvo} summa jednaco celih cisel")
"""

# Zadatak 52

# list = [-2, 7, -5, 3, 1, -4]

# skolvo = 0
# for i in range(len(list)):
#     if list[i] < 0 and list[i] % 2 == 0:
#         print(f'{list[i]}')
#         skolvo += list[i]
#     else:
#         print("idi naxyi")

# a = len(list)
# output = a * skolvo
# print(f"{output}  = {a} * {skolvo}")


# Zadatak 52
# list = [1, 2, 3]

# max = 0
# i = 0
# sbir = 0

# for i in range(i, len(list)):
#     if max < list[i]:
#         max = list[i]
#         sbir += 1

# print(f"max: {max} : output : {sbir-1}")

# Zadatak 55
"""
ocene = [5, 5, 4, 5, 4, 3, 3, 3, 5, 3, 3]

br_3 = 0
br_4 = 0
br_5 = 0

for ocena in ocene:
    if ocena == 3:
        br_3 += 1
    elif ocena == 4:
        br_4 += 1
    elif ocena == 5:
        br_5 += 1

print(f"5-{br_5} 4-{br_4} 3-{br_3}")
"""

# Zadatak 56

# visited = [232, 2322, 3232, 121, 232, 445, 767, 878, 564, 65]
# max = 0
# index = 0

# for i in range(len(visited)):
#     if max < visited[i]:
#         max = visited[i]
#         index = i

# print(f"max: {max} : day : {index+1}")


# Zadatak 57

# payment = [300, 599, 600, 700, 200, 500, 300, 800, 200, 741]
# i = 0
# sbir = 0

# for i in range(i, len(payment)):
#     if payment[i] >= 700:
#         sbir += 1

# print(f"sbir: {sbir}")


# zadatak 58

payment = [500, 300, 599, 600]
i = 0
sbir = 0

sorted_salaries = sorted(payment, reverse=False)

print(f"sbir: {sorted_salaries}")
print(f"sbir: {sorted_salaries[1]}")
