import pytest
import json
import io
from User import User
from Project import Project


# определяем фикстуру, которая читает файл JSON
@pytest.fixture
def user_data():
    # открываем файл JSON с данными о пользователях
    with open("user.json", "r", encoding="utf-8") as f_1:
        # загружаем данные из файла в словарь user_data
        user_data = json.load(f_1, object_hook=lambda d: {int(k) if k.isdigit() else k: v for k, v in d.items()})
        # возвращаем словарь user_data
        return user_data


# определяем тестовую функцию, которая использует фикстуру user_data
def test_read_json_file(user_data):
    project = Project.read_json_file("user.json")
    # проверяем, что атрибут u_list является списком
    assert isinstance(project.u_list, list)


def test_init():
    # создаем список из трех объектов User
    u_list = [User("Глеб", 1, 1), User("Ольга", 2, 2), User("Дмитрий", 3, 3)]
    # создаем объект класса Project с аргументом u_list
    project_1 = Project(u_list)
    # проверяем, что атрибут u_list равен переданному списку
    assert project_1.u_list == u_list
    # проверяем, что атрибут adm равен None
    assert project_1.adm is None


# определяем тестовую функцию для метода show_menu
def test_show_menu():
    project = Project()
    # создаем словарь с пунктами меню и их описаниями
    menu_dct = {
        "1": "Вывести всех пользователей",
        "2": "Добавить пользователя",
        "3": "Удалить пользователя",
        "0": "Выход"
    }

    output = io.StringIO()

    @pytest.mark.parametrize("key, value", menu_dct.items())
    # определяем вложенную тестовую функцию, которая принимает параметры key и value
    def test_show_menu_item(key, value):
        with pytest.monkeypatch.context() as m:
            m.setattr("sys.stdout", output)
            project.show_menu(menu_dct)
        result = output.getvalue()
        # проверяем, что строка содержит пункт меню с ключом и значением из параметров
        assert f"{key} - {value}" in result
