import math

# # Zadatak 1

# side_a = int(input("side_a: "))
# side_b = int(input("side_b: "))


# def main():
#     result = 2 * (side_a + side_b)
#     print(result)


# main()


# # Zadatak 2

# side_a = int(input("Enter perimeter: "))


# def main():
#     side = side_a / 4
#     result = pow(side, 2)
#     print(result)


# main()


# # Zadatak 3

# side_a = int(input("Enter circle distance: "))
# pi = 3.14


# def main():
#     side = pow(side_a,2)
#     result = side / (4 * pi)
#     print(result)


# main()


# # Zadatak 4

# a = int(input("Enter side a "))
# b = int(input("Enter side b "))


# def main():
#     side = (a + b) * 2
#     s = side * 9
#     print(s)


# main()

# # Zadatak 5

# d = int(input("Enter side width "))
# s = int(input("Enter side hight "))
# r = int(input("Enter sideb restojanije "))


# def main():
#     side = 2 * ((d + r * 2) + (s + r * 2))
#     print(side)


# main()

# # Zadatak 6

# d = input("Enter number 4 th: ")

# def main():
#     first = (int(d[1]) * int(d[3])) ** 0.5
#     print(first)


# main()


# # Zadatak 7

# x1 = int(input("Enter x1  "))
# y1 = int(input("Enter y2 "))
# x2 = int(input("Enter x2 "))
# y2 = int(input("Enter y2 "))

# def main():
#     a = x1 -x2
#     b = y2 - y1

#     p = (a + b) * 2
#     s = a * b
#     print(f'{p} : {s}')


# main()


# # Zadatak 8

# start_price = int(input("Enter start price  "))


# def main():
#     a = start_price + (start_price * 0.10)
#     last_price = a - (a * 0.10)
#     print(f" before {a} :  \n after {last_price}")


# main()

# Zadatak 9

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y2: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))


def main():
    x3 = x2 + 2
    y3 = y2 - 3

    x4 = abs(x1 - x2)
    y4 = abs(y1 - y2)

    s4 = (pow(x4, 2) + pow(y4, 2)) ** 0.5

    print(f"Coordinate : {x3,y3} \n  Distance : {s4} \n  ")


main()
