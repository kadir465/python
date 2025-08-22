class Website(object):
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname

        name=input("Adınızı giriniz: ")
        surname=input("Soyadınızı giriniz: ")
        print("websitesine giriş yapıyorsunuz...")


class Website2(Website):
    def __init__(self,name,surname,age,id):
        super().__init__(name,surname)
        self.age=age
        self.id=id

        age=int(input("Yaşınızı giriniz: "))
        id=int(input("size verilen ID yi giriniz: "))
        print("Website2  giriş yapıldı...")

class Website3(Website):
    def __init__(self,name,surname,mail,id):
        super().__init__(name,surname)
        self.mail=mail
        self.id=id

        mail=input("Mail adresinizi giriniz: ")
        id=int(input("size verilen ID yi giriniz: "))
        print("Website3  giriş yapıldı...")


w1 = Website("Kadir", "Yücel")
w2 = Website2("Kadir", "Yücel", 20, 123)
w3 = Website3("Kadir", "Yücel", "kadir@mail.com", 456)
