import hashlib
import random
import string

class UserAuthentication:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        hashed_password = self._hash_password(password)
        self.users[username] = hashed_password

    def login_user(self, username, password):
        if username in self.users:
            stored_password = self.users[username]
            if self._hash_password(password) == stored_password:
                return True
        return False

    def _hash_password(self, password):
        salt = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        salted_password = password + salt
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
        return hashed_password
