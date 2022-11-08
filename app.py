from dbmanager import *
from dbmanager import DbManager
import datetime

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış(E)"
        while True:
            print(msg)
            islem = input("İşlem: ")
            if islem == "1":
                self.displayStudents()
            elif islem == "2":
                self.addStudent()
            elif islem == "3":
                self.editStudent()
            elif islem == "4":
                self.deleteStudent()
            elif islem == "5":
                pass
            elif islem == "6":
                pass
            elif islem == "E" or islem == "Ç":
                break
            else:
                print("Yanlış seçim...")

    def addStudent(self):
        self.displayClasses()

        classid = int(input('hangi sınıf?: '))
        studentNumber = input("numara: ")
        name = input("ad: ")
        surname = input("soyad: ")
        year = int(input("yıl: "))
        month = int(input("ay: "))
        day = int(input("gün: "))

        birthdate = datetime.date(year, month, day)

        gender = input('cinsiyet: ')

        student = Student(None, studentNumber, name, surname, birthdate, gender, classid)
        self.db.addStudent(student)

    def editStudent(self):
        
        classid = self.displayStudents()

        studentid = int(input("öğrenci id: "))
        student = self.db.getStudentById(studentid)

        student.name = input('ad: ') or student.name
        student.surname = input('soyad: ') or student.surname
        student.gender = input('cinsiyet: ') or student.gender
        student.classid = input('sınıf id: ') or student.classid
        student.studentNumber = input('Numara: ') or student.studentNumber

        year = int(input("yıl: ")) or student.birthdate.year
        month = int(input("ay: ")) or student.birthdate.month
        day = int(input("gün: ")) or student.birthdate.day

        student.birthdate = datetime.date(year, month, day)
        self.db.editStudent(student)

    def deleteStudent(self):

        classid = self.displayStudents()

        studentid = int(input("Silinecek öğrenci id: "))
        student = self.db.getStudentById(studentid)
        print("silinecek kayıt: ")
        check = input("Silinsin mi? (E/H)")
        if check == "E":
            self.db.deleteStudent(studentid)
            print("Kayıt silme işlemi başarılı.")
        else:
            print("Kayıt silinmedi.")


    def displayClasses(self):

        classes = self.db.getClasses()
        for i in classes:
            print(f'{i.id}: {i.name}')

    def displayStudents(self):

        self.displayClasses()

        classid = int(input('Hangi sınıf?'))

        students = self.db.getStudentsByClassId(classid)
        print("Öğrenci Listesi")
        for std in students:
            print(f'{std.id} {std.name} {std.surname}')

        return classid

         
app = App()
app.initApp()