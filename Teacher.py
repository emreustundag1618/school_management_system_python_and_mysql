class Teacher:

    def __init__(self, id, branch, name, surname, birthdate, gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.branch = branch
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    @staticmethod
    def CreateTeacher(obj):
        list_ = []

        if isinstance(obj, tuple):  # obj nesnesi bir tuple örneği ise
            return Teacher(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6])
        else:
            for i in obj:
                list_.append(Teacher(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        return list_