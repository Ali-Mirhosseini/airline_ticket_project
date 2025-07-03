class UserDa:
    def save(self, user):
        print("User saved to database", user.id, user.name, user.family)

    def edit(self, user):
        print("User edited in database", user.id, user.name, user.family)

    def remove(self, user):
        print("User Removed from database", user.id, user.name, user.family)

    def find_by_name_and_family(self, name, family):
        pass

    def find_by_user_name(self, user_name):
        pass

    def find_by_role(self, role):
        pass
