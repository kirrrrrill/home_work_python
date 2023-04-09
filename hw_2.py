number = int(input("Введите трехзначное число: "))

a = number % 10
number = number // 10
b = number % 10
number = number // 10
 
print("Сумма цифр числа:", number + a + b)



