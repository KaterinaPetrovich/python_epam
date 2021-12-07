import pytest

from homework6.task1 import User


@pytest.fixture
def create_users():
    user, _, _ = User(), User(), User()
    return user


def test_get_null_created_instances():
    assert User.get_created_instances() == 0


def test_get_created_instances(create_users):
    assert create_users.get_created_instances() == 3


def test_reset_instances_counter(create_users):
    create_users.reset_instances_counter()
    assert create_users.get_created_instances() == 0


def test_return_reset_instances_counter(create_users):
    assert create_users.reset_instances_counter() == 3
