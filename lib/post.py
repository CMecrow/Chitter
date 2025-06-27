from datetime import datetime

class Post:

    def __init__(self, id, post_content, post_datetime):
        self.id = id
        self.post_content = post_content
        self.post_datetime = post_datetime

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Post({self.id}, {self.post_content}, {self.post_datetime})"
    
    def is_valid(self):
        if self.post_content == None or self.post_content == "":
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.post_content == None or self.post_content == "":
            errors.append("You can't make an empty post!")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)