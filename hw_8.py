

m = int(input("Введите ширину шоколадки" ))
n = int(input("Введите длинну шоколадки" ))
k = int(input("Введе скок отломов надо сделать"))
if k<=n+(m-2):
    print("yes")
else:
    print("no")