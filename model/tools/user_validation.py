import re
from datetime import datetime


class UserValidation:
    def user_validator_name(self, name):
        if not re.match(r"^[a-zA-Z/s]{3,30}$", name.name):
            raise ValueError("Name is not valid")

    def user_validator_family(self, user):
        if not re.match(r"^[a-zA-Z/s]{3,30}$", user.family):
            raise ValueError("Name is not valid")

    def user_validator_birth_date(self, user):
        return datetime.strptime(user.birth_date, "%Y-%m-%d")

    def user_validator_user_name(self, user):
        if not re.match(r"^[a-zA-Z0-9\S]{3,30}$", user.user_name):
            raise ValueError("Username is not valid")

    def user_validator_password(self, user):
        if not re.match(r"^[a-zA-Z0-9\S]{3,30}$", user.password):
            raise ValueError("Password is not valid")

    def user_validator_role(self, role):
        if role not in ["admin", "user"]:
            raise ValueError("Invalid role")

