def reverse_lookup(phonebook, name):
    for phone, person in phonebook.items():
        if person == name:
            return phone
    else:
        return "Нет данных"

phonebook = {
    "+7 705 994 7363":"Лёша",
    "+7 771 456 3837":"Асанали",
    "+7 707 675 8760":"Чингиз"
}

name = input("Введите имя пользователя: ")
phone_number = reverse_lookup(phonebook, name)
print(phone_number)