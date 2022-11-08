class Student:

    def __init__(self, id, studentNumber, name, surname, birthdate, gender, classid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        if len(name) > 45:
            raise Exception("name için maksimum 45 karakter girmelisiniz")
        else:
            self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.classid = classid

    @staticmethod
    def CreateStudent(obj):
        list_ = []

        if isinstance(obj, tuple):  # obj nesnesi bir tuple örneği ise
            return Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6])
        else:
            for i in obj:
                list_.append(Student(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        return list_

