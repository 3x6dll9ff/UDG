import math 
from functools import reduce


#task1 ________________________________________________________________
# def fivr_digit_number(number):

#     local_a = int(number[1]) + int(number[2])
#     local_b = math.sqrt(int(number[0]) * int(number[3]) * int(number [4]))

#     if local_a > local_b:
#         print('True')
#     else:
#         print('False')
    

# fivr_digit_number('551511')

#task2 ________________________________________________________________

# list = []
# def task_2(start,end,first,last):
#     product = 1
#     for i in range (start,end+1):
#         if (i % first == 0) and not(i % last == 0):
#             new_var = pow(i,3)
#             list.append(new_var)

#     for i in range(len(list)):
#         product = product * list[i]
#     list.append(product)

# task_2(1,10,3,2)
# print(list)


#task3 ________________________________________________________________


# students_list = [
#     {'ime': "Milosh", 'Prisutstan': 10, 'odustan': 2},
#     {'ime': "Marija", 'Prisutstan': 8, 'odustan': 6},
#     {'ime': "Nikola", 'Prisutstan': 11, 'odustan': 1},
# ]

# for student in students_list:
#     prisutnost = student['Prisutstan']
#     odsustvo = student['odustan']
#     procenat_prisustva = (prisutnost / (prisutnost + odsustvo)) * 100
    
#     if procenat_prisustva > 75:
#         print(f"{student['ime']} Prisutstvo > 75% ({procenat_prisustva:.2f}%)")



#task4 ________________________________________________________________

# f = open('/Users/danilakardashevkii/Developer/Python/UDG/Coloquium/marketi.txt')
# saderzaj = f.read()

# redovi = saderzaj.split('\n')
# print(redovi)

# sum_voli = 0
# sum_Aroma = 0
# sum_idea = 0
# profit =''

# for red in redovi:
#     stranice = red.split(',')
#     print(stranice)
#     if stranice[0] == 'Voli1' or stranice[0] == 'Voli2':
#         sum_voli += int(stranice[1])
#     if stranice[0] == 'Aroma1' :
#         sum_Aroma += int(stranice[1])
#     if stranice[0] == 'Idea1' or stranice[0] == 'Idea2':
#         sum_idea += int(stranice[1])


# if sum_voli > sum_Aroma and sum_voli > sum_idea:
#     profit = 'Voli'

# if sum_Aroma > sum_voli and sum_Aroma > sum_idea:
#     profit = 'Aroma'

# if sum_idea > sum_voli and sum_idea > sum_Aroma:
#     profit = 'Idea'

# print(f'Voli: {sum_voli} Aroma: {sum_Aroma} , Idea: {sum_idea}', f' Profitnee je {profit}')
    
                    
    
