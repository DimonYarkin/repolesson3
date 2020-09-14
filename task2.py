def my_func(**kwargs):
    print(" ".join(kwargs.values()))


my_func(first_name="Иванов", last_name="Иван", year_of_birth="1977", city="Москва", email="admin@yandex.ru",
        phone="8-965-77-777-77")
