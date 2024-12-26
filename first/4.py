# zadatak 1.

# x = int(input("Insert 6 digit = "))

# x1 = x // 100000
# x2 = (x // 10000) % 10
# x3 = (x // 1000) % 10
# x4 = (x // 100) % 10
# x5 = (x // 10) % 10
# x6 = x % 10

# print(f"{x1,x2,x3,x4,x5,x6}")

# if (x1 * x3) + (2 * x6) == x2 + (x4 * x5):
#     print("True")
# else:
#     print("false")



# zadatak 2.
"""
people = int(input("How much peoples? - "))
Bodovi = {}

for i in range(people):
    all = 0
    bodovi_math = int(input(f"Insert how much math bodovi have people {i} - "))
    if 0 < bodovi_math < 50:
        math = bodovi_math
    else:
        print("wrong Value")
    bodovi_programming = int(
        input(f"Insert how much programming bodovi have people {i} - ")
    )
    if 0 < bodovi_programming < 50:
        programming = bodovi_programming
    else:
        print("wrong Value")
    all = math + programming
    Bodovi[i] = {"math": math, "programming": programming, "all_bodovi": all}
    print(
        f"people - {[i]} math - {[math]} programming - {[programming]} all_bodovi - {all}"
    )

duplicates = set()
seen = set()
winner = None
max_programming_score = 0

for key, value in Bodovi.items():
    current_all_bodovi = value["all_bodovi"]
    if current_all_bodovi in seen:
        duplicates.add(current_all_bodovi)
    else:
        seen.add(current_all_bodovi)

for key, value in Bodovi.items():
    if value["all_bodovi"] in duplicates:
        if value["programming"] > max_programming_score:
            max_programming_score = value["programming"]
            winner = key

if winner is not None:
    print(f"\nWinner - people: {winner} math: {Bodovi[winner]['math']} programming: {Bodovi[winner]['programming']} all_bodovi: {Bodovi[winner]['all_bodovi']}")
else:
    print("\nNo winner found.")
"""

# Zadatak 3
# n = float(input('insert'))
# if n >= 4.5:
#     print('odlican uspjeh')
# elif n < 4.5 and n >= 3.5:
#     print('vrlodobar uspeh')
# elif n < 3.5 and n >= 2.5:
#     print('dovoljan uspeh')
# elif n == 2 and n< 2.5:
#     print('bad')
# else:
#     print('ne dobijem uspeh ')


# Zadatak 33

# name_Mounth = str(input('insert name of Mounth: '))

# Mounth = {
#     'January' : '1',
#      'February' : '2',
#      'March' : '3',
#      'April' :'4',
#      'May' : '5',
#      'June' : '6',
#      'July' : '7',
#      'August' : '8',
#      'September' : '9',
#      'October' : '10',x1x1
#      'November' : '11',
#      'December' : '12',
#       }

# if name_Mounth in Mounth:
#     print(f'The numerical representation of {name_Mounth} is {Mounth[name_Mounth]}')
# else:
#     print('Invalid month name. Please enter a valid month.')



# zadatak 40

# tekst = str(input("input string: "))
# target = str(input("input target: "))

# if target == 'cd' and tekst.endswith(target):
#           print('DA')
# elif target == 'me' and tekst.endswith(target):
#       a = tekst.upper()
#       print(f'{a}')
# else:
#     print("Wrong target or text ")


# # Zadatak 41

# a = str(input("Input text: "))

# if a.count('0') + a.count('1') == len(a):
#     print("da")
# else:
#     print("no")


# Zadatak 43

n = int(input("enter number : "))
start = int(input("enter star : "))
end = int(input("enter end : "))

if (int(n[start:end:]) % 2 == 0) and (int(n[start:end:]) % 4 != 0):


# string = "For petlia"

# for elem in string:
#     print(elem)