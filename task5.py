def my_func():
    result = 0
    while True:
        exit_val = False
        my_list = input("Введите строку чисел разделенных пробелами для выхода символ * ").split()
        if my_list.count("*") > 0:
            my_list.remove("*")
            exit_val = True
        try:
            my_list_int = [int(item) for item in my_list]

            print(f"Предыдущая сумма чисел = {result}")
            result += sum(my_list_int)
            print(f"Сумма чисел итого = {result}")
            if exit_val:
                break

        except ValueError:
            print("В строке содержатся не только цифры повторите ввод")


my_func()
