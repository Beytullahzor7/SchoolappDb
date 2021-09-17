#recieving all the information console and communication with the database
from dbmanager import DbManager #managaer.py dosyasındaki classı direkt olarak import ederek içerisindeki tüm referans bilgileri kullanabilmemiz sağlandı
import datetime
from Student import Student

class App:
    def __init__(self):

        self.db = DbManager()

    def initApp(self): #yapılabilecek işlemler gösterilecek
        msg = "*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış(E/Ç)"
        
        while True:
            print(msg)

            islem = input("Seçim: ")
            if islem == '1':
                self.displayStudents()
                
            elif islem == '2':
                self.addStudent()

            elif islem == '3':
                self.editStudent()
                pass

            elif islem == '4':
                self.deleteStudent()
                pass
            elif islem == 'E' or islem == 'Ç':
                break
            else:
                print("Yanlış Seçim")

                
    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input('Öğrenci id: '))

        self.db.deleteStudent(studentid)

    def editStudent(self):
        classid = self.displayStudents() #önce öğrenci bilgilerini gösterecegiz zaten bu özelliğin içinde sınıf bilgileri de otomatik olarak geliyor bunu ayarlamıştık
        studentid = int(input('Öğrenci id: '))

        student = self.db.getStudentById(studentid)

        student[0].name = input('Name: ') or student[0].name #kullanıcı farklı bir name bilgisi girerse güncellemiş olacak girmezse aynı name kalmaya devam edecek
        student[0].surname = input('Surname: ') or student[0].surname
        student[0].gender = input('Cinsiyet (E/K): ') or student[0].gender
        student[0].classid = input('Sınıf: ') or student[0].classid
      
        year = input("Yıl: ") or student[0].birthdate.year
        month = input("Ay: ") or student[0].birthdate.month
        day = input("Gün: ") or student[0].birthdate.day

        student[0].birthdate = datetime.date(year,month,day)
        self.db.editStudent(student[0])


    def addStudent(self):
        self.displayClasses()
        classid = int(input("Hangi Sınıf: "))

        number = input('Numara: ')
        name = input('Ad: ')
        surname = input('Soyad: ')
        year = int(input('Yıl: ')) 
        month = int(input('Ay: '))
        day = int(input('Gün: '))

        birthdate = datetime.date(year, month, day)
        gender = input('Cinsiyet (E/K)')

        student = Student(None, number, name, surname, birthdate, gender, classid)
        self.db.addStudent(student) #import ettiğimiz dbManager.py içerisindeki addStudent fonksiyonundan faydalandık

    def displayClasses(self): #bu işlemi birden fazla yerde kullanacagımız için ayrı bir method olarak tanımlayıp gereken yerde sadece çağırma işlemi yapacağız
        classes = self.db.getClasses()
        for i in classes:
            print(f'{i.id}: {i.name}')

    def displayStudents(self):
        self.displayClasses()            
        classid = int(input("Hangi Sınıf: "))

        students = self.db.getStudentsByClassId(classid)
        print("Öğrenci Listesi")

        for std in students:
            print(f'{std.id}-{std.name} {std.surname}')

        return classid

app = App()
app.initApp()

        
