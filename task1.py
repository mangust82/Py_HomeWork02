# Напишите программу, которая принимает на вход вещественное число и показывает сумму 
# его цифр.

num = input('Enter the real number ')
glue_list = ''.join(num.split('.'))
if not glue_list.isdigit():
    print('You entered uncorrect number')
else:
    sum = 0 
    for i in glue_list:
        sum = sum + int(i)
print(sum)


