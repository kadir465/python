class Islemler(object):
    def __init__(self):
        self.islem = input("Yapmak istediğiniz işlemi giriniz: "
                           "1-toplama, 2-çıkarma, 3-çarpma, 4-bölme: ")
        
        self.dizi = []

        while True:
            eleman = input("Diziye eklemek istediğiniz sayıyı giriniz (bitirmek için '=' ya basın): ")
            if eleman == '=':
                break
            else:
                self.dizi.append(int(eleman))

        if self.islem == "1":
            self.topla()
        elif self.islem == "2":
            self.cikar()
        elif self.islem == "3":
            self.carp()
        elif self.islem == "4":
            self.bol()
        else:
            print("Geçersiz işlem seçtiniz.")
    
    def topla(self):
        sonuc = 0
        for i in self.dizi:
            sonuc += i
        print("Toplam:", sonuc)
    
    def carp(self):
        sonuc = 1
        for i in self.dizi:
            sonuc *= i
        print("Çarpım:", sonuc)

    def cikar(self):
        if not self.dizi:
            print("Dizi boş.")
            return
        sonuc = self.dizi[0]
        for i in self.dizi[1:]:
            sonuc -= i
        print("Fark:", sonuc)
    
    def bol(self):
        if not self.dizi:
            print("Dizi boş.")
            return
        sonuc = self.dizi[0]
        for i in self.dizi[1:]:
            sonuc /= i
        print("Bölüm:", sonuc)


Islemler()
