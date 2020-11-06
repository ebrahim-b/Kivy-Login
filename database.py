import json
from pathlib import Path

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        path = Path('user.json')
        if (not path.exists()):
            with open('user.json', 'w') as db_file:
                db_file.write(json.dumps({}))
            data = path.read_text()
            self.users = json.loads(data)
        else:
            data = path.read_text()
            self.users = json.loads(data)

    def get_user(self, user_name):
        if user_name in self.users:
            return self.users[user_name]
        else:
            return -1

    def add_user(self, user_name, password):
        tmp = {}
        if user_name.strip() not in self.users:
            tmp[user_name.strip()] = password.strip()
            self.users.update(tmp)
            with open(self.filename, "w") as f:
                json.dump(self.users, f)
            return 1
        else:
            return -1

    def validate(self, user_name, password):
        if self.get_user(user_name) != -1:
            return self.users[user_name] == password
        else:
            return False

