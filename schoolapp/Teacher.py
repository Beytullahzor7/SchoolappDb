class Teacher:
  
    def __init__(self,id,branch,name,surname,birthdate,gender):

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
        list = []

        if isinstance(obj, tuple): #gelecek olan classın tipi tuple mı yoksa liste mi sorgusu yapar
            list.append(Teacher(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])) #tek bir öğrenci yani tek bir tuple gelmesi durumu 
        else:
            for i in obj:
                list.append(Teacher(i[0],i[1],i[2],i[3],i[4],i[5])) #birden fazla ögrencinin get fonksiyonunda olması durumunda liste döner
        return list