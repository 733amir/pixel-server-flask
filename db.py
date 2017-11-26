from random import randrange

class Database:
    count = 2
    reset_pass_code_digit_count = 5
    users = [
        {
            'id': 1,
            'username': 'amirr',
            'fullname': 'امیر خزاعی',
            'password': 'a',
            'email': 'a@b.com'
        },
        {
            'id': 2,
            'username': 'parsa',
            'fullname': 'پارسا حجابی',
            'password': 'b',
            'email': 'p@b.com'
        }
    ]
    reset_pass_codes = [
        ('parsa', 12345)
    ]

    def username_exists(self, username):
        for user in self.users:
            if user['username'] == username:
                return True
        return False

    def add_user(self, username, fullname, email, password):
        self.count += 1
        self.users.append({
            'id': self.count,
            'username': username,
            'fullname': fullname,
            'email': email,
            'password': password
        })

    def check(self, username, password):
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                return True
        return False

    def email_exists(self, email):
        for user in self.users:
            if user['email'] == email:
                return True
        return False

    def add_reset_code(self, email):
        # Check for existing code.
        for (user_email, code) in self.reset_pass_codes:
            if email == user_email:
                return code

        # Generate and add new code.
        code = str(randrange(10**(self.reset_pass_code_digit_count-1), 10**self.reset_pass_code_digit_count))
        self.reset_pass_codes.append((email, code))
        return code

    def get_reset_code(self, email):
        for (user_email, code) in self.reset_pass_codes:
            if email == user_email:
                return code
        return None

    def remove_reset_code(self, email):
        for i in range(len(self.reset_pass_codes)):
            if self.reset_pass_codes[i][0] == email:
                del self.reset_pass_codes[i]

    def reset_password(self, email, password):
        for user in self.users:
            if user['email'] == email:
                user['password'] = password
                return True
        return False
