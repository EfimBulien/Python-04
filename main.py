import database
from user import User

data = {}
db = database.Database()
user_obj = User(0, '', '', '', '', '')

def main_menu():
    while True:
        print("1. Регистрация пользователя")
        print("2. Авторизация пользователя")
        print("3. Добавить данные")
        print("4. Изменить данные")
        print("5. Удалить данные")
        print("6. Фильтрация данных")
        print("7. Вывести данные из таблицы")
        print("8. Добавить стандартные данные")
        print("9. Выход")

        choice = int(input("Выберите операцию: "))

        if choice == 1:
            register_user()
        elif choice == 2:
            authenticate_user()
        elif choice == 3:
            add_data()
        elif choice == 4:
            modify_data()
        elif choice == 5:
            delete_data()
        elif choice == 6:
            filter_data()
        elif choice == 7:
            db.display_table_data()
        elif choice == 8:
            db.default_data()
        elif choice == 9:
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

def register_user():
    name = input("Введите имя: ")
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    address = input("Введите адрес: ")
    email = input("Введите email: ")

    if user_obj.validate_email(email) and user_obj.validate_password(password):
        user_data = {"name": name, "login": login, "password": password, "address": address, "email": email}
        user_obj.reg(user_data)
        print("Регистрация прошла успешно!")
    else:
        print("Ошибка валидации данных. Попробуйте еще раз.")

def authenticate_user():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    user_id = user_obj.auth({"login": login, "password": password})
    if user_id:
        print(f"Авторизация успешна. ID пользователя: {user_id}")
    else:
        print("Неверные логин или пароль. Попробуйте еще раз.")

def add_data():
    table = input("Введите таблицу, в которую вы хотите добавить данные (users, books, employee, lendings): ")
    data = {}

    if table == 'users':
        data["name"] = input("Введите имя: ")
        data["login"] = input("Введите логин: ")
        data["password"] = input("Введите пароль: ")
        data["address"] = input("Введите адрес: ")
        data["email"] = input("Введите email: ")
    elif table == 'books':
        data["title"] = input("Введите название книги: ")
        data["author"] = input("Введите автора книги: ")
        data["year"] = input("Введите год издания: ")
        data["genre"] = input("Введите жанр книги: ")
    elif table == 'employee':
        data["login"] = input("Введите логин: ")
        data["name"] = input("Введите имя сотрудника: ")
        data["password"] = input("Введите пароль: ")
        data["wage"] = input("Введите заработную плату сотрудника: ")
    elif table == 'lendings':
        data["book_id"] = input("Введите ID книги: ")
        data["users_id"] = input("Введите ID пользователя: ")
        data["lend_date"] = input("Введите дату выдачи: ")
        data["return_date"] = input("Введите дату возврата (если есть): ")

    db.insert(table, data)
    print("Данные успешно добавлены!")

def modify_data():
    table = input("Введите таблицу, в которой вы хотите изменить данные (users, books, employee, lendings): ")

    if table == 'users':
        user_id = input("Введите ID пользователя: ")
        data_type = input("Введите тип данных для изменения (name, login, password, address, email): ")
        new_value = input(f"Введите новое значение для {data_type}: ")
        db.update({data_type: new_value}, table, {'id': user_id})
        print("Данные обновлены успешно!")
    elif table == 'books':
        book_id = input("Введите ID книги: ")
        data_type = input("Введите тип данных для изменения (title, author, year, genre): ")
        new_value = input(f"Введите новое значение для {data_type}: ")
        db.update({data_type: new_value}, table, {'id': book_id})
    elif table == 'employee':
        employee_id = input("Введите ID сотрудника: ")
        data_type = input("Введите тип данных для изменения (login, name, password, wage): ")
        new_value = input(f"Введите новое значение для {data_type}: ")
        db.update({data_type: new_value}, table, {'id': employee_id})
    elif table == 'lendings':
        lending_id = input("Введите ID выдачи: ")
        data_type = input("Введите тип данных для изменения (book_id, users_id, lend_date, return_date): ")
        new_value = input(f"Введите новое значение для {data_type}: ")
        db.update({data_type: new_value}, table, {'id': lending_id})
        print("Данные обновлены успешно!")


def delete_data():
    table = input("Введите таблицу, из которой вы хотите удалить данные (users, books, employee, lendings): ")
    condition_type = input("Введите тип условия для удаления (например, id): ")
    condition_value = input(f"Введите значение для условия {condition_type}: ")
    
    db.delete(table, {condition_type: condition_value})
    print("Данные успешно удалены!")

def filter_data():
    table = input("Введите таблицу, из которой вы хотите получить отфильтрованные данные (users, books, employee, lendings): ")
    condition_type = input("Введите тип условия для фильтрации (например, name): ")
    condition_value = input(f"Введите значение для условия {condition_type}: ")

    result = db.filter(table, {condition_type: condition_value})
    print("Результаты фильтрации:")
    for item in result:
        print(item)
    
main_menu()