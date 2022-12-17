# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите 
# произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной 
# строке одно число.

import random

N = int(input('Enter the number: '))
a = []
for i in range(-N, N+1):
    a.append(i)
print(a)

############## Write position in file.txt #############################
my_file = open('file.txt', 'w+')
for i in range(3):
    my_file.writelines(str(random.randrange(0, 2 * N)) + '\n')

############## Read position from file.txt and multiply #############################
mulpl = 1
my_file = open('file.txt')
for i in my_file:
    memb1 = int(i)
    mulpl = mulpl * a[memb1]
my_file.close()

print(mulpl)
