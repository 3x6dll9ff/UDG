import math


#----------------------------------------------------------------

# def solve_circle_in_rectangle():
#     radius = 4

#     #a
#     x1 = 2
#     y1 = 4
#     #B
#     x2 = 4
#     y2 = 6

#     circle = 2 * radius 


#     d = abs(x2-x1)
#     b = abs(y2-y1) 

#     if (circle < d and circle < b):
#         return True
#     else:
#         return False

# print(solve_circle_in_rectangle())

#----------------------------------------------------------------

# def task_22(n, k2, p1, p2):

#     k1 = n - k2

#     summ_points_p1 = p1 * k1
#     summ_points_p2 = p2 * k2

#     result = (summ_points_p1 + summ_points_p2) / n
#     print(round(result, 2))


# task_22(
#     int(input("Enter N: ")),
#     int(input("Enter K2: ")),
#     float(input("Enter p1: ")),
#     float(input("Enter p2: ")),
# )


#----------------------------------------------------------------

# def task_19(sum, points, reward):

#     if points == 5.0:
#         print(f"Discount 40%")
#         sum = sum - (sum * 0.40)
#         print(f'You need to pay : {sum}')
#     elif 4.0 <= points < 5.0:
#         if reward == 1:
#             print(f"Discount 30%")
#             sum = sum - (sum * 0.30)
#             print(f'You need to pay : {sum}')
#         else:
#             print(f"Discount 20%")
#             sum = sum - (sum * 0.20)
#             print(f'You need to pay : {sum}')
#     elif 3.0 <= points < 4.0:
#         if reward == 1:
#             print(f"Discount 30%")
#             sum = sum - (sum * 0.30)
#             print(f'You need to pay : {sum}')
#         else:
#             print(f"Discount 10%")
#             sum = sum - (sum * 0.10)
#             print(f'You need to pay : {sum}')


# task_19(
#     float(input("Enter school sum :")),
#     float(input("Enter student middle point (2.0 - 5.0) :")),
#     int(input("Enter reward (1- Yes , 0 -No) :")),
# )

# ----------------------------------------------------------------      
 
# list = []
# def cvadrat(start,end):
#     sum = 0
#     for i in range (start,end+1):
#         print(i)
#         new_var = i * i
#         if new_var % 9 == 0:
#             list.append(new_var)
#             sum = sum + new_var
#     list.append(sum)
        
# cvadrat(1,10)
# print(list)

# ----------------------------------------------------------------      

# def solve_povrshina(lista):
#     max_povrshina = 0
#     dimecija = None

#     for i in lista:
#         povrshina = i[0] * i[1]
#         if povrshina > max_povrshina:
#             max_povrshina = povrshina
#             dimecija = i

#     print(dimecija)



# solve_povrshina([(4,5),(5,6),(6,7),(7,8)])


# f = open('/Users/danilakardashevkii/Developer/Python/UDG/Coloquium/text.txt')
# saderzaj = f.read()

# redovi = saderzaj.split('\n')
# print(redovi)

# max_pople = 0
# for red in redovi:
#     stranice = red.split(',')
#     people = int(stranice[2])

#     if max_pople < people:
#         max_pople = people
#         r = red.split(',')
    
# print("Строка с наибольшим количеством жителей:")
# print(r[1])  

def count_of_sets():

    a = [1, 2, 2, 2, 4, 4]

    max_product = 1
    max_repeat_count = 1
    number = 0

    for i in range(len(a)):
        repeat_count = 1
        for k in range(i+1, len(a)):
            if a[k] == a[i]:
                repeat_count += 1
                number = a[k]
            else:
                break
        product = pow(a[i],repeat_count)
        if product > max_product:
            max_product = product
            max_repeat_count = repeat_count

    print("Max product:", max_product)
    print("Number of repetitions:", max_repeat_count," Number : ", number)


count_of_sets()
