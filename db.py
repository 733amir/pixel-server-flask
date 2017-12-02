from random import randrange

IP = '192.168.10.120'


class Database:
    count = 2
    reset_pass_code_digit_count = 5

    users = [
        {
            'id': 1,
            'username': 'usernamea',
            'fullname': 'امیر خزاعی',
            'email': 'a@b.c',
            'password': 'a',
            'profile': {
                'header': 'http://{}:5000/static/a-header.png'.format(IP),
                'image': 'http://{}:5000/static/a.jpg'.format(IP),
                'interest': ['ورزش', 'برنامه‌نویسی', 'مطالعه', 'فیلم سینمایی', 'رمان', 'ورزش', 'برنامه‌نویسی', 'مطالعه', 'فیلم سینمایی', 'رمان'],
                'bio': 'دانشجو کارشانسی‌ارشد در رشته هوش‌مصنوعی هستم و علاقه‌مند به برنامه‌نویسی'
            },
            'reset_code': '11111',
            'friends': [
                'usernameb',
                'usernameb',
                'usernameb',
                'usernameb',
                'usernameb',
                'usernameb',
                'usernameb',
                'usernameb',
                'usernameb'
            ],
            'posts': [
                {
                    'username': 'usernamea',
                    'image': 'http://{}:5000/static/posts/1.jpg'.format(IP),
                    'time': '۳ ساعت پیش',
                    'location': 'رهنما',
                    'comment_count': '28',
                    'like_count': '192',
                    'caption': 'شروع رهنما کالج :)'
                },
                {
                    'username': 'usernamea',
                    'image': 'http://{}:5000/static/posts/2.jpg'.format(IP),
                    'time': 'دیروز',
                    'location': 'دشت و دمن',
                    'comment_count': '112',
                    'like_count': '380',
                    'caption': 'جاتون خالی خیلی خوش میگذره.'
                },
                {
                    'username': 'usernamea',
                    'image': 'http://{}:5000/static/posts/3.jpg'.format(IP),
                    'time': 'هفته گذشته',
                    'location': 'مریخ',
                    'comment_count': '0',
                    'like_count': '34',
                    'caption': ''
                },
                {
                    'username': 'usernamea',
                    'image': 'http://{}:5000/static/posts/4.jpg'.format(IP),
                    'time': 'برج میلاد',
                    'location': 'رهنما',
                    'comment_count': '12',
                    'like_count': '65',
                    'caption': 'غروب غم انگیز تهرانه. دلم گرفته مرد و نامرد و خسته شدم. به هر دری میزنم بسته هست و حل نمیشه. برام دعا کنین.'
                },
                {
                    'username': 'usernamea',
                    'image': 'http://{}:5000/static/posts/5.jpg'.format(IP),
                    'time': 'ماه گذشته',
                    'location': '',
                    'comment_count': '15',
                    'like_count': '0',
                    'caption': ''
                },

            ]
        },
        {
            'id': 2,
            'username': 'usernameb',
            'fullname': 'پارسا حجابی',
            'email': 'b@b.c',
            'password': 'b',
            'profile': {
                'header': 'http://{}:5000/static/b-header.jpg'.format(IP),
                'image': 'http://{}:5000/static/b.jpg'.format(IP),
                'interest': ['Guitar', 'Off Road', 'Camping', 'Driving'],
                'bio': 'This is parsa bio.'
            },
            'reset_code': '22222',
            'friends': [
                'usernamea',
                'usernamea',
                'usernamea',
                'usernamea',
                'usernamea',
                'usernamea',
                'usernamea',
                'usernamea',
                'usernamea'
            ],
            'posts': [
                {
                    'username': 'usernamea',
                    'image': 'http://{}:5000/static/posts/1.jpg'.format(IP),
                    'time': '۳ ساعت پیش',
                    'location': 'رهنما',
                    'comment_count': '28',
                    'like_count': '192',
                    'caption': 'شروع رهنما کالج :)'
                },
                {
                    'username': 'usernamea',
                    'image': 'http://{}:5000/static/posts/2.jpg'.format(IP),
                    'time': 'دیروز',
                    'location': 'دشت و دمن',
                    'comment_count': '112',
                    'like_count': '380',
                    'caption': 'جاتون خالی خیلی خوش میگذره.'
                },
                {
                    'username': 'usernamea',
                    'image': 'http://{}:5000/static/posts/3.jpg'.format(IP),
                    'time': 'هفته گذشته',
                    'location': 'مریخ',
                    'comment_count': '0',
                    'like_count': '34',
                    'caption': ''
                },
                {
                    'username': 'usernamea',
                    'image': 'http://{}:5000/static/posts/4.jpg'.format(IP),
                    'time': 'برج میلاد',
                    'location': 'رهنما',
                    'comment_count': '12',
                    'like_count': '65',
                    'caption': 'غروب غم انگیز تهرانه. دلم گرفته مرد و نامرد و خسته شدم. به هر دری میزنم بسته هست و حل نمیشه. برام دعا کنین.'
                },
                {
                    'username': 'usernamea',
                    'image': 'http://{}:5000/static/posts/5.jpg'.format(IP),
                    'time': 'ماه گذشته',
                    'location': '',
                    'comment_count': '15',
                    'like_count': '0',
                    'caption': ''
                },

            ]
        }
    ]

    def add_user(self, username, fullname, email, password):
        code = str(randrange(10 ** (self.reset_pass_code_digit_count - 1), 10 ** self.reset_pass_code_digit_count))
        self.count += 1
        self.users.append({
            'id': self.count,
            'username': username,
            'fullname': fullname,
            'email': email,
            'password': password,
            'profile': {
                'header': '',
                'image': '',
                'interests': []
            },
            'reset_code': code
        })

    def get_user(self, username):
        for user in self.users:
            if user['username'] == username:
                return user

    def username_exists(self, username):
        for user in self.users:
            if user['username'] == username:
                return True
        return False

    def email_exists(self, email):
        for user in self.users:
            if user['email'] == email:
                return True
        return False

    def get_email(self, username):
        for user in self.users:
            if user['username'] == username:
                return user['email']

    def login(self, username, password):
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                return True
        return False

    def update_reset_code(self, email):
        code = str(randrange(10 ** (self.reset_pass_code_digit_count - 1), 10 ** self.reset_pass_code_digit_count))
        for user in self.users:
            if user['email'] == email:
                user['reset_code'] = code

    def get_reset_code(self, email):
        for user in self.users:
            if user['email'] == email:
                return user['reset_code']

    def reset_password(self, email, password):
        for user in self.users:
            if user['email'] == email:
                user['password'] = password
                return True
        return False

    def get_profile(self, username):
        for user in self.users:
            if user['username'] == username:
                return user['profile']
