# 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран 
# их сумму.

n = int(input('Enter number of members: '))
sum = 0
my_list = []
for i in range(1, n + 1):
    my_list.append(round((1+1/i) ** i, 2))
    sum = sum + my_list[i-1]
print(my_list)
print(sum)
