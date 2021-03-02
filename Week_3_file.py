import random
import csv
import matplotlib.pyplot as plt

def createStudents(amount):
    courses = createCourses()
    persons = []
    names = ["Tom", "Lis", "Bet", "Andreas", "Andra", "Lilleth", "Dia", "Ek", "Abe", "Se", "Ta", "Bek", "Paul", "Po", "Che", "Lars", "Las", "Sva", "Bea", "Andrea", "Tony", "Sal", "Sally", "Somme"]
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
                csv = 'Stud_name: {name}, course_name: {course_name}, teacher: {teacher}, ects: {ects}, grade: {grade}, classroom: {classroom}'.format(
                    name=i.name, course_name=e.name, teacher=e.teacher, ects=e.ECTS, classroom=e.classroom, grade=e.grade)
                file_object.write(csv + '\n')

    # for i in persons:
    #     with open('/home/jovyan/python_handin_template/week3_writeToFile.csv', 'a') as file_object:
    #         csv = 'Stud_name: {name}, course_name: {course_name}, teacher: {teacher}, ects: {ects}, classroom: {classroom}, grade: {grade}'.format(
    #             name=i.name, course_name=e.name, teacher=e.teacher, ects=e.ECTS, classroom=e.classroom, grade=e.grade)
    #         file_object.write(csv + '\n')
    

def studentBar():
    students = readStudentsImprov()
    for student in students:
        print(student.name)
        print(student.datasheet.courses[0].classroom)
        #plt.bar([student.name], [student.get_avg_grade()],width=0.5, align='center')
        #plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')

def readStudents():
    with open('/home/jovyan/python_handin_template/week3_writeToFile.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        
        return data

def readStudentsImprov():
    names = []
    with open('/home/jovyan/python_handin_template/week3_writeToFile.csv', 'r') as file_object:
        lines = file_object.readlines()
        for i in lines:
            name = i.split('Stud_name: ')[1].split(', course_name')[0]
            names.append(name)
    
    returnnames = set(names)
    
    students = []
    for studentname in returnnames:

        data = DataSheet("0")
        student = Student(studentname, "male", data, "url")

        with open('/home/jovyan/python_handin_template/week3_writeToFile.csv', 'r') as file_object:
            lines = file_object.readlines()
            for i in lines:
                name = i.split('Stud_name: ')[1].split(', course_name')[0]
                
                if name == studentname:
                    
                    course_name = i.split('course_name: ')[1].split(', teacher')[0]
                    teacher = i.split('teacher: ')[1].split(', ects')[0]
                    ETCS = i.split('ects: ')[1].split(', grade')[0]
                    grade = i.split('grade: ')[1].split(', classroom')[0]
                    classroom = i.split('classroom: ')[1]
                    

                    print(grade)

                    course = Course(course_name, classroom, teacher, ETCS, grade)
                    data.courses.append(course)

        students.append(student)

    return students

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

    def __init__(self, name, classroom, teacher, ECTS, grade=0):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        possibleScores = [2, 4, 7, 10, 12]
        if grade == 0:
            self.grade = random.choice(possibleScores)

        