class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def __eq__(self, other):
        return (
            isinstance(other, User) and
            self.username == other.username and
            self.password == other.password
        )

    def __repr__(self):
        return f"User(username='{self.username}', password='{self.password}')"
    
    def is_valid(self):
        if self.username == None or self.username == "":
            return False
        if self.password == None or self.password == "":
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.username == None or self.username == "":
            errors.append("You can't leave username blank!")
        if self.password == None or self.password == "":
            errors.append("You can't leave password blank!")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)

