import re

class User:
    def __init__(self, user_id, name, password):
        self.id = user_id
        self.name = name
        self.password = password

class Student(User):
    def __init__(self, user_id, name, password):
        super().__init__(user_id, name, password)
        self.courses = set()

class Professor(User):
    def __init__(self, user_id, name, password):
        super().__init__(user_id, name, password)
        self.courses = set()

class Course:
    def __init__(self, course_id, name, capacity):
        self.id = course_id
        self.name = name
        self.capacity = capacity
        self.students = set()

class UniversitySystem:
    def __init__(self):
        self.users = {}
        self.professors = {}
        self.students = {}
        self.courses = {}
        self.current_user = None

    def sign_up(self, user_type, user_id, name, password):
        if user_id in self.users:
            print("id already exists")
        elif not user_id.isdigit():
            print("invalid id")
        elif ' ' in name:
            print("invalid name")
        elif len(password) < 4 or ' ' in password or not any(char in "*!@$%^&()" for char in password):
            print("invalid password")
        else:
            if user_type == 'S':
                self.students[user_id] = Student(user_id, name, password)
            elif user_type == 'P':
                self.professors[user_id] = Professor(user_id, name, password)
            self.users[user_id] = User(user_id, name, password)
            print("signed up successfully!")

    def log_in(self, user_id, password):
        if user_id not in self.users:
            print("incorrect id")
        elif self.users[user_id].password != password:
            print("incorrect password")
        else:
            self.current_user = self.users[user_id]
            print("logged in successfully!")
            if isinstance(self.current_user, Student):
                print("entered student menu")
            elif isinstance(self.current_user, Professor):
                print("entered professor menu")

    def log_out(self):
        print("logged out successfully!")
        print("entered log in/sign up menu")
        self.current_user = None

    def show_course_list(self):
        print("course list:")
        for course_id, course in self.courses.items():
            print(f"{course.id} {course.name} {len(course.students)}/{course.capacity}")

    def add_course(self, course_name, course_id, capacity):
        if course_id in self.courses:
            print("course id already exists")
        elif ' ' in course_name:
            print("invalid course name")
        elif not course_id.isdigit():
            print("invalid course id")
        elif not capacity.isdigit():
            print("invalid course capacity")
        else:
            course = Course(course_id, course_name, int(capacity))
            self.courses[course_id] = course
            self.professors[self.current_user.id].courses.add(course)
            print("course added successfully!")

    def get_course(self, course_id):
        if course_id not in self.courses:
            print("incorrect course id")
        elif self.current_user.id in self.courses[course_id].students:
            print("you already have this course")
        elif len(self.courses[course_id].students) == self.courses[course_id].capacity:
            print("course is full")
        else:
            self.students[self.current_user.id].courses.add(self.courses[course_id])
            self.courses[course_id].students.add(self.current_user.id)
            print("course added successfully!")

    def process_command(self, command):
        command_parts = command.split()
        if command_parts[0] == "edu" and command_parts[2] == "menu" and command_parts[4] == "edu":
            print("current menu:", command_parts[3])
        elif command_parts[0] == "edu" and command_parts[2] == "up" and command_parts[3] == "-S":
            self.sign_up("S", command_parts[7], command_parts[9], command_parts[11])
        elif command_parts[0] == "edu" and command_parts[2] == "up" and command_parts[3] == "-P":
            self.sign_up("P", command_parts[7], command_parts[9], command_parts[11])
        elif command_parts[0] == "edu" and command_parts[2] == "in":
            self.log_in(command_parts[5], command_parts[7])
        elif command_parts[0] == "edu" and command_parts[2] == "out" and command_parts[4] == "edu":
            self.log_out()
        elif command_parts[0] == "edu" and command_parts[2] == "course" and command_parts[4] == "list" and command_parts[6] == "edu":
            self.show_course_list()
        elif command_parts[0] == "edu" and command_parts[2] == "course" and command_parts[4] == "-c":
            self.add_course(command_parts[7], command_parts[9], command_parts[11])
        elif command_parts[0] == "edu" and command_parts[2] == "course" and command_parts[4] == "-i":
            self.get_course(command_parts[7])
        else:
            print("invalid command")