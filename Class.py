class Class:

    def __init__(self, id, name, teacherid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.name = name
        self.teacherid = teacherid

    @staticmethod
    def CreateClass(obj):
        list_ = []

        if isinstance(obj, tuple):  # obj nesnesi bir tuple örneği ise
            return Class(obj[0], obj[1], obj[2])
        else:
            for i in obj:
                list_.append(Class(i[0], i[1], i[2]))
        return list_