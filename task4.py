def my_func(x, y):
    return 1 / x ** abs(y)


def my_func_for(x, y):
    x_old = x
    for i in range(1,abs(y)):
        x *= x_old
        print(x)
    return 1 / x


print(f"Результат без цикла {my_func(2, -4):.2}")
print(f"Результат c циклом {my_func_for(2, -4):.2}")
