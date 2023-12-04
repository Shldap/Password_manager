class PasswordStorage:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, username, password):
        if website in self.passwords:
            self.passwords[website][username] = password
        else:
            self.passwords[website] = {username: password}

    def get_password(self, website, username):
        if website in self.passwords and username in self.passwords[website]:
            return self.passwords[website][username]
        return None
