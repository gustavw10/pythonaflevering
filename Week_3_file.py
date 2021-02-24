import random
import csv
import matplotlib.pyplot as plt

def createStudents(amount):
    courses = createCourses()
    persons = []
    names = ["Tom", "Lis", "Bet", "Andreas", "Andra", "Lilleth", "Dia", "Ek"]
    genders = ['Male', 'Female']
    maxA=151

    for i in range(amount):
        data = DataSheet("0")
        pers = Student(random.choice(names), random.choice(genders), data, "img")
        
        while pers.datasheet.get_ects_total() < 150:
            selected = (random.choice(courses))
            if selected.ECTS + pers.datasheet.get_ects_total() < maxA:
                pers.datasheet.courses.append(selected)

        persons.append(pers)
        
    for i in persons:
        for e in i.datasheet.courses:
            with open('/home/jovyan/python_handin_template/week3_writeToFile.csv', 'a') as file_object:
                csv = 'Stud_name: {name},course_name: {course_name},teacher: {teacher},ects: {ects},classroom: {classroom},grade: {grade}'.format(
                    name=i.name, course_name=e.name, teacher=e.teacher, ects=e.ECTS, classroom=e.classroom, grade=e.grade)
                file_object.write(csv + '\n')
    
def readStudents():
    with open('/home/jovyan/python_handin_template/week3_writeToFile.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        
        return data


def createCourses():
    course1 = Course("Java", "Room23", "Thomas", 30)
    course2 = Course("Python", "Room47", "Thomas", 30)
    course3 = Course("Algos", "Room12", "Al", 20)
    course4 = Course("Java Advanced", "Room15", "Al", 15)
    course5 = Course("Python Advanced", "Room88", "Thomas", 10)
    course6 = Course("Discrete Math", "Room39", "Eko", 15)
    course7 = Course("Systems", "Room04", "Eko", 5)
    course8 = Course("TypeScript", "Room04", "Eko", 5)
    courses = [course1, course2, course3, course4, course5, course6, course7, course8]
    return courses

class Student():

    def __init__(self, name, gender, datasheet, image_url):
        self.name = name
        self.gender = gender
        self.datasheet = datasheet
        self.image_url = image_url

    def __str__(self):
        return 'The person is: {name}'.format(
            name=self.name)

    def get_avg_grade(self):
        return sum(self.datasheet.get_grades_as_list()) / (len(self.datasheet.get_grades_as_list()))
    
    def set_grade(self):
        self.datasheet.courses


class DataSheet():
    def __init__(self, name, courses=[]):
        self.courses = courses
        self.name = name
    
    def get_grades_as_list(self):
        return [item.grade for item in self.courses]

    def get_ects_total(self):
        total = 0
        for i in self.courses:
            total = total + int(i.ECTS)
        return total
    
    
class Course():

    def __init__(self, name, classroom, teacher, ECTS):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        possibleScores = [2, 4, 7, 10, 12]
        self.grade = random.choice(possibleScores)

        