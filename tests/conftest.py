import pytest

from src.user import User
from src.task import Task

@pytest.fixture
def first_user():
    return User(
        username="User",
        email="user@mail.ru",
        first_name="User",
        last_name="Userov",
        task_list=[
            Task('Купить огурцы', 'Купить огурцы для салата'),
            Task('Купить помидоры', 'Купить помидоры для салата'),
        ]
    )

@pytest.fixture
def second_user():
    return User(
        username="Jhon",
        email="Jhon@mail.ru",
        first_name="Jhon",
        last_name="Doe",
        task_list=[
            Task('Купить огурцы', 'Купить огурцы для салата'),
            Task('Купить перец', 'Купить перец для салата'),
            Task('Купить помидоры', 'Купить помидоры для салата'),
        ]
    )

@pytest.fixture
def task():
    return Task('Купить огурцы', 'Купить огурцы для салата', created_at="20.04.2024")