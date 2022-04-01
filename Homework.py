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
            writer = csv.DictWriter(file, delimiter=',',
                                    fieldnames=self.columns)

            writer.writerow(user.get_information())

    def delete_user(self, id):
        line = []
        with open('messages.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                line.append(row)
                for field in row:
                    if field == id:
                        line.remove(row)
        with open('messages.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(line)


data_obj = UserData('messages.csv', ['id', 'name', 'age', 'sex', 'time'])

user1 = User(1, 'Marat', 18, 'male')
user2 = User(2, 'Dayana', 18, 'female')

# data_obj.add_user(user1)
data_obj.add_user(user2)
#data_obj.delete_user("2")

