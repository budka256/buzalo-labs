from math import asin, exp, log, fabs
x = float(input("Введите значение x = "))
y = float(input("Введите значение y = "))
msg = "Выберите вид функции f(x): arcsin(y/x) = 1, e^y = 2, ln(x*y) = 3 "
f = int(input(msg))
if f == 1:
    if fabs(y) <= fabs(x):
        fx = asin(y / x)
    else:
        print("Значение для arcsin недопустимо.")
        exit()
elif f == 2:
    fx = exp(y)
elif f == 3:
    if x * y > 0:
        fx = log(x * y)
    else:
        print("Значение для логарифма недопустимо.")
        exit()
else:
    print("Неверный выбор")
    exit()
print(f"Результат: {fx}")
