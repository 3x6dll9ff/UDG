list = {'abc', "ABC", "AbC", "ABc"}


def recursion_find_upper(list):
    if len(list) == 0:
        return 0
    elif list[0].isupper():
        return 1 + recursion_find_upper(list[1:])
    else:
        return recursion_find_upper(list[1:])
    

recursion_find_upper(list)