def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    my_list.remove(min(my_list))
    print(f"Сумма двух максимальных чисел = {sum(my_list)}")


my_func(1, 2, 3)
