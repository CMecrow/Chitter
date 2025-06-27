from lib.user import User

class LoginSystem:
    def __init__(self):
        self.users = []

    def register(self, user):
        errors = []
        password = user.password
        username = user.username
        if any(existing_user.username == username for existing_user in self.users):
            errors.append("Username already taken.")
        if errors:
            return ", ".join(errors)
        self.users.append(User(username, password))
        return True

    def login(self, user):
        errors = []
        password = user.password
        username = user.username
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        errors.append("Invalid username or password.")
        if errors:
            return ", ".join(errors)
        return False