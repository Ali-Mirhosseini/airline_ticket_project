from model.tools.user_validation import UserValidation

class User:
    def __init__(self, id, name, famaliy, birth_date, user_name, password, role):
        self.id = id
        self.name = name
        self.famaliy = famaliy
        self.birth_date = birth_date
        self.user_name = user_name
        self.password = password
        self.role = role

    def to_tuple(self):
        return (self.id, self.name, self.famaliy, self.birth_date, self.user_name, self.password, self.role)

    def validate(self):
        validator = UserValidation()
        return validator.user_validator_name(self)