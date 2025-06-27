from lib.user import User
from lib.login import LoginSystem

def test_user_can_be_created_and_added():
    user1 = User('first_user', 'password')
    user2 = User('second_user', 'password')
    login = LoginSystem()
    login.register(user1)
    login.register(user2)
    assert login.users == [user1, user2]

def test_users_can_login():
    user1 = User('first_user', 'password')
    login = LoginSystem()
    login.register(user1)
    login.login(user1)

