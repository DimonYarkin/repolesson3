def hascyr(s):
    lower = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    return lower.intersection(s.lower()) != set()


def int_func(str_arg_list):
    my_list = str_arg_list.split()
    my_list_int = [item.lower().title() for item in my_list]
    return " ".join(my_list_int)


while True:
    exit_val = True
    user_srt = input("Введите строку латинских букв разделенных пробелами: ")
    for item in user_srt:
        if hascyr(item):
            exit_val = False
            print("Строка содержет кирилические символы повторите ввод")
            break
    # int_func(input("Введите строку латинских букв: "))
    if exit_val:
        print(int_func(user_srt))
        break
