# 5 Реализуйте алгоритм перемешивания списка.

import random

def mash_list(a):
    for i in range(len(a)):
        index = random.randrange(0, len(a))
        temp = a[i]
        a[i] = a[index]
        a[index] = temp
    return a

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mash_list(my_list))



