from collections import UserDict

class Field:
    def __init__(self, value): 
        self.value = value

    def __str__(self):
        return str(self.value) 
    
    def __repr__(self):
        return str(self.value)
    

class Name(Field):
    def __init__(self, name=None):
        if name is None:
            raise ValueError
        super().__init__(name) 


class Phone(Field):
    def __init__(self, phone): 
        if len(phone) != 10 or not phone.isdigit():
            raise ValueError("Incorrect phone number!")
        super().__init__(phone)


class Record:
    def __init__(self, name): 
        self.name = Name(name)
        self.phones = list()

    def add_phone(self, phone_number): 
        if self.find_phone(phone_number):
            return
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number): 
        phone_number = self.find_phone(phone_number)
        if phone_number:
            self.phones.remove(phone_number)
            return
        raise ValueError("Phone number not found!")
    
    def edit_phone(self, old_phone_number, new_phone_number):
        phone_number = self.find_phone(old_phone_number)
        if phone_number:
            phone_number.value = new_phone_number
            return
        raise ValueError("Phone number not found!")

    def find_phone(self, phone_number): 
        for p in self.phones:
            if p.value == phone_number:
                return p

    def __str__(self):
        return f'Record(Name: {self.name} Phones: {self.phones})'
    
    def __repr__(self):
        return f'Record(Name: {self.name} Phones: {self.phones})'

class AddressBook(UserDict): 
    def add_record(self, record: Record): 
        name = record.name.value
        self.data.update({name: record}) 

    def find(self, name): 
        return self.get(name) 
    
    def delete(self, name):
        del self[name]


if __name__ == '__main__':
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
    print('Printing all records')
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print('Printing John record')
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    print('Printing find by phone')
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

