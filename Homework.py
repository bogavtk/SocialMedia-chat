import csv
from datetime import datetime


class User:
    def __init__(self, id, name, age, sex):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.time_now = datetime.now()

    def get_information(self):
        return {'id': self.id, 'name': self.name, 'age': self.age,
                'sex': self.sex, 'time': self.time_now}

    def __repr__(self):
        return self.name


class UserData():
    def __init__(self, path, columns):
        self.path = path
        self.columns = columns

    def add_user(self, user):
        with open(self.path, 'a') as file:
            writer = csv.DictWriter(file, delimiter=';',
                                    fieldnames=self.columns)

            writer.writerow(user.get_information())

    def delete_user(self, id):
        reader = open(self.path, 'rb')





    def get_user(self, user_id):
        with open(self.path, 'r') as file:
            user_o = None
            reader = csv.DictReader(file, delimiter=';',
                                    fieldnames=self.columns)
            for user_csv in reader:
                if user_csv['id'] == user_id:
                    user_o = user_csv
            return user_csv


data_obj = UserData('messages.csv', ['id', 'name', 'age', 'sex', 'time'])

user1 = User(1, 'Marat', 18, 'male')
user2 = User(2, 'Dayana', 18, 'female')

data_obj.add_user(user1)
data_obj.add_user(user2)
print(data_obj.get_user(1))
data_obj.delete_user(2)
