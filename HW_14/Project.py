# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.

# Создайте класс Project, содержащий атрибуты –
# список пользователей проекта и
# админ проекта. Класс имеет следующие методы:

# Классовый метод загрузки данных из JSON файла
# (из второй задачи 8 семинара)

# Метод входа в систему – требует указать
#   имя и
#   id пользователя.

# Далее метод создает пользователя и проверяет
# есть ли он в списке пользователей проекта.
# Если в списке его нет, то вызывается исключение доступа.
# Если пользователь присутствует в списке пользователей проекта,
# то пользователь, который входит получает его уровень доступа и становится администратором.

# Метод добавление пользователя в список пользователей. Если уровень пользователя меньше, чем уровень админа, вызывайте исключение уровня доступа.
# * метод удаления пользователя из списка пользователей проекта
# * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера

import json
import sys

from MyExceptions import MyExceptionErrorAccess, MyExceptionErrorAdmLevel
from User import User


class Project:

    @classmethod
    def read_json_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as f_1:
            user_data = json.load(f_1, object_hook=lambda d: {int(k) if k.isdigit() else k: v for k, v in d.items()})
            u_list = []
            for user_level, users in user_data.items():
                for user_id, user_name in users.items():
                    u_list.append(User(user_name, user_id, user_level))
            return Project(u_list)

    def __init__(self, u_list=None):
        if u_list is None:
            self.u_list = []
        self.u_list = u_list
        self.adm = None

    def show_menu(self, menu_dct):
        for n, v in menu_dct.items():
            print(f'{n} - {v}')

    def main_menu(self):
        input_user = User(input('Enter user name: '), int(input('Enter user id: ')))
        Project.auth_user(self, input_user)
        print('Пользователь успешно авторизирован')
        menu_low_adm = {
            '1': 'Вывести всех пользователей',
            '2': 'Добавить пользователя',
            '3': 'Удалить пользователя',
            '0': 'Выход'
        }

        while True:
            self.show_menu(menu_low_adm)
            choise = input('Выберите действие: ')
            match choise:
                case '1':
                    print(f'СПИСОК ПОЛЬЗОВАТЕЛЕЙ:')
                    for user, number in enumerate(self.u_list, 1):
                        print('{0}. {1}'.format(user, number))
                case '2':
                    print('ДОБАВИТЬ ПОЛЬЗОВАТЕЛЯ')
                    new_user = User(input('Enter user name: '),
                                    int(input('Enter user id: ')),
                                    int(input('Enter user level: ')))
                    Project.add_new_user(self, new_user)
                    print(f'Пользователь {new_user} успешно добавлен')
                case '3':
                    print('УДАЛИТЬ ПОЛЬЗОВАТЕЛЯ')
                    del_user = User(input('Enter user name: '),
                                    int(input('Enter user id: ')),
                                    int(input('Enter user level: ')))
                    Project.remove_user(self, del_user)
                    print(f'Пользователь {del_user} успешно удалён')
                case '0':
                    print('ВЫХОД ИЗ СИСТЕМЫ')
                    sys.exit()
                case _:
                    print('Ошибка выбора меню')

    def auth_user(self, other):
        for user in self.u_list:
            if user == other:
                other.u_level = user.u_level
                self.adm = other
                break
        else:
            raise MyExceptionErrorAccess(other.u_name, other.u_id)

    def add_new_user(self, other):
        if other.u_level < self.adm.u_level:
            raise MyExceptionErrorAdmLevel(other.u_level)
        self.u_list.append(other)

    def remove_user(self, other):
        if other not in self.u_list:
            raise MyExceptionErrorAccess(other.u_name, other.u_id)
        elif other.u_level < self.adm.u_level:
            raise MyExceptionErrorAdmLevel(other.u_level)
        self.u_list.remove(other)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('user.json', 'w', encoding='utf-8') as f_2:
            user_data = {}
            for user in self.u_list:
                if user.u_level not in user_data:
                    user_data[user.u_level] = {}
                user_data[user.u_level][user.u_id] = user.u_name
            json.dump(user_data, f_2, ensure_ascii=False, indent=4)

    def __str__(self):
        return f'class Project() __dict__: {self.__dict__}'


# with Project.read_json_file('user.json') as f:
#     f.main_menu()


