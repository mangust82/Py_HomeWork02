# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений 
# чисел от 1 до N.
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


num = int(input('Enter the number '))
mult = 1
a = []
for num in range(1, num+1):
    mult *= num
    a.append(mult)
    print(mult, end = ", ")
print()
print(a)


