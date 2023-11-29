import database

class User(database.Database):
    def __init__(self, id, name, login, password, address, email):
        super().__init__()
        self.table = 'users'
        self.__id = id
        self.__name = name
        self.login = login
        self.password = password
        self.address = address
        self.email = email
    
    def reg(self, data):
        super().insert('users', data)
        
    def auth(self, data):
        result = super().get_id('users', data)
        return result[0] if result else None
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if self.validate(value):
            self.__name = value.capitalize()
        else:
            print('Ошибка: Недопустимое значение')
            
    @staticmethod
    def validate_email(email):
        return "@" in email
    
    @staticmethod
    def validate_password(password):
        return len(password) >= 6  

    @staticmethod
    def validate(value):
        return type(value) is str and len(value) > 0 and len(value) <= 255
