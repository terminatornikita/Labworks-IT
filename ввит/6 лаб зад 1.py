a = input('Введите username: ')
b = input('Введите email: ')
c = input('Введите пароль: ')

class UserAccount:
    def __init__(self, username, email, _password): 
        self.username = username
        self.email = email
        self._password = hash(_password)

    def set_password(self, _new_password):
        self._password = hash(_new_password)
        print("Пароль успешно изменен.")

    def check_password(self, password):
        return hash(password) == self._password

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

user = UserAccount(a, b, c)
user.display_info()
password_check = input('Введите пароль для проверки: ')
if user.check_password(password_check):
    print("Пароль верный.")
else:
    print("Неверный пароль.")
    _new_password = input('Введите новый пароль: ')
    user.set_password(_new_password)

 

