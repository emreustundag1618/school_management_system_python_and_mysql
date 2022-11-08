from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class
import mysql.connector

class DbManager:

    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self, id):
        sql = "SELECT * FROM Students WHERE id = %s"
        value = (id,)
        self.cursor.execute(sql, value)

        try:
            obj = self.cursor.fetchone()
            print(obj)
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error: ', err)

    def getStudentsByClassId(self, classid):
        sql = "SELECT * FROM Students WHERE classid = %s"
        value = (classid,)
        self.cursor.execute(sql, value)

        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error: ', err)

    def addStudent(self, student: Student):
        sql = "INSERT INTO Students(StudentNumber, Name, Surname, Birthdate, Gender, ClassId) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender, student.classid)

        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
            print(f'Son eklenen kaydın id: {self.cursor.lastrowid}.')
        except mysql.connector.Error as err:
            print("Hata: ", err)

    def editStudent(self, student: Student):
        sql = "UPDATE Students SET Name = %s, Surname = %s, StudentNumber = %s, BirthDate = %s, Gender = %s, ClassId = %s WHERE Id = %s"
        params = (student.name, student.surname, student.studentNumber, student.birthdate, student.gender, student.classid, student.id)

        self.cursor.execute(sql, params)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} adet kayıt güncellendi')
        except mysql.connector.Error as err:
            print("Hata: ", err)

    def deleteStudent(self, id):
        sql = "DELETE FROM Students WHERE Id = %s"
        params = (id,)

        self.cursor.execute(sql, params)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} adet kayıt silindi')
        except mysql.connector.Error as err:
            print("Hata: ", err)

        
    def getTeacherById(self, id):
        sql = "SELECT * FROM Teachers WHERE id = %s"
        value = (id,)
        self.cursor.execute(sql, value)

        try:
            obj = self.cursor.fetchone()
            print(obj)
            return Teacher.CreateTeacher(obj)
        except mysql.connector.Error as err:
            print('Error: ', err)

    def addTeacher(self, teacher: Teacher):
        sql = "INSERT INTO Teacher(Branch, Name, Surname, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
        values = (teacher.branch, teacher.name, teacher.surname, teacher.birthdate, teacher.gender)

        self.cursor.execute(sql, values)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
            print(f'Son eklenen kaydın id: {self.cursor.lastrowid}.')
        except mysql.connector.Error as err:
            print("Hata: ", err)

    def editTeacher(self, teacher: Teacher):
        sql = "UPDATE Teachers SET Name = %s, Surname = %s, Branch = %s, BirthDate = %s, Gender = %s WHERE Id = %s"
        params = (teacher.name, teacher.surname, teacher.branch, teacher.birthdate, teacher.gender, teacher.id)

        self.cursor.execute(sql, params)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} adet kayıt güncellendi')
        except mysql.connector.Error as err:
            print("Hata: ", err)

    def getClasses(self):
        sql = "SELECT * FROM Classes"
        self.cursor.execute(sql)

        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error: ', err)

    def __del__(self):
        self.connection.close()
        print("DB bağlantı kapandı.")


db = DbManager()

