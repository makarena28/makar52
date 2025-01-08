class UserAccaunt:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def set_password(self, new_password):
        self.new_password = new_password
    def check_password(self, password):
        self.password = password
        if self.new_password == self.password:
            return True
        else:
            return False

user1 = UserAccaunt("Makar", "makarka2000@gmail.com", "psrkwk331.wrd")
user1.set_password("new_makarka")
print(user1.check_password("new_makarka"))









