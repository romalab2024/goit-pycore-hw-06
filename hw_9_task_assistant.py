from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # Клас для зберігання імені контакту
    pass

class Phone(Field):
    # Клас для зберігання номера телефону з валідацією
    def __init__(self, value):
        self.value = self.validate(value)

    @staticmethod
    def validate(value):
        if re.fullmatch(r"\d{10}", value):
            return value
        else:
            raise ValueError("Phone number must be exactly 10 digits")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        # Додавання нового номера телефону до списку
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        # Видалення номера телефону з запису
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        # Редагування існуючого номера телефону
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                break

    def find_phone(self, phone):
        # Пошук номера телефону в записі
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self):
        # Форматований вивід інформації про контакт
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        # Додавання запису до адресної книги
        self.data[record.name.value] = record

    def find(self, name):
        # Пошук запису за ім'ям
        return self.data.get(name, None)

    def delete(self, name):
        # Видалення запису за ім'ям
        if name in self.data:
            del self.data[name]
            
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

# Видалення запису Jane
book.delete("Jane")
