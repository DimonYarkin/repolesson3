def my_div(arg1, arg2):
    return arg1 / arg2


while True:
    try:
        arg1 = int(input("Введите делимое целое число"))
        arg2 = int(input("Введите делитель целое число"))
        print(f"Результат деления ({arg1} на {arg2}) = {my_div(arg1, arg2):.2}")
        break
    except ZeroDivisionError:
        print("Делитель равен нулю, на 0 делить нельзя. Повторите ввод")
    except ValueError:
        print("Один из аргументов не число повторите ввод")
