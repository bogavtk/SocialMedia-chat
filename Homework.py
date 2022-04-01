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

    def sent_message(self, message, to):
        UserData.sent_message(self, message, to)

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

    @staticmethod
    def sent_message(self, message, to):
        with open('chat.csv', 'a') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([self.name] + [to] + [message] + [datetime.now()])
            file.close()

    def delete_message(self, id):
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

    @staticmethod
    def get_all_messages(first_user, second_user):
        line = []
        with open('chat.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if str(first_user) in row and str(second_user) in row:
                    line.append(row)

        with open('between.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(line)

data_obj = UserData('users.csv', ['id', 'name', 'age', 'sex', 'time'])
user1 = User(1, 'Marat', 18, 'male')
user2 = User(2, 'Dayana', 18, 'female')
user3 = User(3, 'Linar', 20, 'male')

#user1.sent_message('Hello', user2)
#user2.sent_message('Hello', user1)
#user1.sent_message('Dick' , user3)
data_obj.get_all_messages(user1, user2)