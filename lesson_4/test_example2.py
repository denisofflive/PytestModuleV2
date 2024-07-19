from collections import namedtuple

UserData = namedtuple("_", ["login", "password"])

user = UserData(login="ak@ya.ru", password="123456789")
print(user.login)
