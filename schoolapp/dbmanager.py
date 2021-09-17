import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

class DbManager:

    def __init__(self):
        
        self.connection = connection
        self.cursor = self.connection.cursor()
        
    def getStudentById(self,id):

        sql = "select * from student where id =%s"
        value = (id,)

        self.cursor.execute(sql, value)

        try:
            obj = self.cursor.fetchone() #tuple
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Error", err)
        
    def getClasses(self):

        sql = "select * from class"
        self.cursor.execute(sql)

        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print("Error", err)


    def getStudentsByClassId(self,classid):

        sql = "select * from student where classid =%s"
        value = (classid,)

        self.cursor.execute(sql, value)

        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj) #student classı içerisinde oluşturduğumuz createStudent metodu çağrısı
        except mysql.connector.Error as err:
            print("Error", err)

    def addStudent(self, student: Student): #alcak olduğumuz parametrenin tipini yazdık
        sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender,Classid) VALUES(%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi. ')

        except mysql.connector.Error as err:
            print('Hata', err)
      

    def editStudent(self, student: Student):
        sql = "update student set studentnumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s, classid=%s where id=%s"
        value = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi. ')

        except mysql.connector.Error as err:
            print('Hata', err)
    
    def deleteStudent(self, studentid):
        sql = "delete from student where id = %s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt silindi. ')

        except mysql.connector.Error as err:
            print('Hata', err)
   
    def getTeacherById(self,id):
        sql = "select * from teacher where id = %s"
        value = (id,)

        self.cursor.execute(sql, value)

        try:
            obj = self.cursor.fetchone() #tuple
            return Teacher.CreateTeacher(obj)
        except mysql.connector.Error as err:
            print("Error", err)

    def addTeacher(self, teacher: Teacher):
        sql = "INSERT INTO teacher(branch,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        value = (teacher.branch,teacher.name,teacher.surname,teacher.birthdate,teacher.gender)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi. ')

        except mysql.connector.Error as err:
            print('Hata', err)

    def editTeacher(self, teacher: Teacher):
        sql = "update teacher set branch=%s, name=%s, surname=%s, birthdate=%s, gender=%s where id=%s"
        value = (teacher.branch,teacher.name,teacher.surname,teacher.birthdate,teacher.gender,teacher.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi. ')

        except mysql.connector.Error as err:
            print('Hata', err)



db = DbManager()

teacher = db.getTeacherById(4)
# print(teacher[0].name)
teacher[0].name = "Damla"
db.editTeacher(teacher[0])

# student = db.getStudentById(22)

# student[0].name = "Merve"
# db.editStudent(student[0])

# db.addStudent(student[0]) 
#getStudentById(7) diyerek name,surname,studentNumber harici bizim girmediğimiz verilerin otomatik olarak id numarası 7 olan kayıttan gelmesini sağladık


# print(student[0].name, student[0].surname) #studentin kendisi de bir liste olduğu için 0. elemanı üzerinden kontrol yapacağız

# students = db.getStudentsByClassId(1)
# print(students[0].name, students[0].surname)
# print(students[10].name, students[10].surname)
