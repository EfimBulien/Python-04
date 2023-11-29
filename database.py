import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()

    def default_data(self):
        users_data = [
            {'name': 'Олег', 'login': 'oleG6', 'password': 'macm12019', 'address': 'no', 'email': 'oleg@example.com'},
            {'name': 'Виталя', 'login': 'VItalyaP', 'password': 'vip00', 'address': 'no', 'email': 'vip@example.com'},
        ]

        books_data = [
            {'title': 'Мишк Фреде', 'author': 'Семен', 'year': 2023, 'genre': 'комедия'},
            {'title': 'C#', 'author': 'Скорогудаева', 'year': 2023, 'genre': 'хоррор-ужастик'},
            {'title': 'ОМГ ПОКО', 'author': 'кнр', 'year': 2023, 'genre': 'бомба'},
        ]

        employee_data = [
            {'login': 'skeletonC++', 'name': 'Костя', 'password': 'stdcinintmain', 'wage': 137000},
            {'login': 'javatop', 'name': 'Муха', 'password': 'bimbimbambam', 'wage': 69000},
        ]

        lendings_data = [
            {'book_id': 1, 'users_id': 1, 'lend_date': '2023-01-01', 'return_date': '2023-01-10'},
            {'book_id': 2, 'users_id': 2, 'lend_date': '2023-02-01', 'return_date': '2023-02-10'},
        ]

        for data in users_data:
            self.insert('users', data)

        for data in books_data:
            self.insert('books', data)

        for data in employee_data:
            self.insert('employee', data)

        for data in lendings_data:
            self.insert('lendings', data)

        print("Таблицы заполнены стандартными значениями.")

    @staticmethod
    def get_condition(condition):
        if len(condition > 1):
            condition = ' AND '.join(f'{column}=?' for column in condition.keys())
        else:
            conditions = condition
            return conditions
    
    def execute_query(self, query, values=None):
        try:
            with self.conn:
                if values:
                    self.cursor.execute(query, values)
                else:
                    self.cursor.execute(query)
                return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f'Произошла ошибка: {e}')

    def display_table_data(self):
        table = input("Введите название таблицы, из которой вы хотите вывести данные: ")
        result = self.get_table(table)

        if result and len(result) > 0:
            print(f"Данные из таблицы {table}:")
            for row in result:
                print(row)
        else:
            print(f"Таблица {table} пуста.")

    def get_table(self, table):
        return self.execute_query(f'SELECT * FROM {table}')
        
    def get_id(self, table, condition):
        conditions = self.get_condition(condition)
        query=f'SELECT id FROM {table} WHERE {conditions}'
        self.execute_query(query, tuple(conditions.values()))
        
    def insert(self, table, data):
        columns = ', '.join(data.keys())
        pl_hs = ', '.join('?' for _ in data)
        query = f'INSERT INTO {table} ({columns}) VALUES ({pl_hs})'
        self.execute_query(query, tuple(data.values()))

    
    def filter(self, table, condition):
        conditions = self.get_condition(condition)
        query=f'SELECT id FROM {table} WHERE {conditions}'
        self.execute_query(query,tuple(conditions.values()))
    
    def update(self, data, table, condition):
        update_data = ', '.join(f'{column} = ?' for column in data.keys())
        query = f'UPDATE {table}, SET {update_data} WHERE {condition.keys()[0]} = ?'
        self.execute_query(query, tuple(data.values() + list(condition.values())[0]))
        
    def delete(self, table, condition):
        query = f'DELETE FROM {table} IF EXISTS WHERE {list(condition.keys())[0]} = ?'
        self.execute_query(query, tuple(list(condition.keys())[0]))
        