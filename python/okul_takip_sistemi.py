class OkulSistem:
    def __init__(self):
        print("Okul sistemine giriş yapıldı")
        print("Göreviniz nedir? Görevli ise-1, Öğrenci ise-2, Öğretmen ise-3 yazınız")
        
        try:
            self.gorev = int(input("Numaralandırma yapınız: "))
            
            if self.gorev == 1:
                Gorevli()
            elif self.gorev == 2:
                Ogrenci()
            elif self.gorev == 3:
                Ogretmen()
            else:
                print("Hatalı giriş yaptınız")
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")

class Gorevli:
    def __init__(self):
        print("Görevli kısmına giriş yaptınız")
        self.ogrenci_listesi = []
        self.dosya_adi = "ogrenci.txt"
        
        self.adet = int(input("Kaç öğrenci kaydı yapmak istiyorsunuz: "))
        
        for i in range(self.adet):
            isim = input("Öğrenci ismini girin: ")
            soyisim = input("Öğrenci soyismini girin: ")
            numara = input("Öğrenci numarasını girin: ")
            
            self.ogrenci_listesi.append(f"{isim} {soyisim} {numara}\n")

        with open(self.dosya_adi, "a", encoding="utf-8") as file:
            file.writelines(self.ogrenci_listesi)
            print("Öğrenci kaydı başarıyla yapıldı")

        self.menu()

    def menu(self):
        while True:
            print("\nYapmak istediğiniz işlemi giriniz:")
            print("Öğrenci listeleme-1, Öğrenci silme-2, Öğrenci güncelleme-3, Çıkış-4")
            
            try:
                islem = int(input("İşlem numarasını giriniz: "))
                
                if islem == 1:
                    self.ogrenci_listele()
                elif islem == 2:
                    self.ogrenci_sil()
                elif islem == 3:
                    self.ogrenci_guncelle()
                elif islem == 4:
                    print("Çıkış yapılıyor...")
                    break
                else:
                    print("Geçersiz işlem numarası!")
            except ValueError:
                print("Lütfen geçerli bir sayı girin!")

    def ogrenci_listele(self):
        print("Öğrenci listesi:")
        try:
            with open(self.dosya_adi, "r", encoding="utf-8") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("Öğrenci dosyası bulunamadı!")

    def ogrenci_sil(self):
        silinecek_numara = input("Silmek istediğiniz öğrencinin numarasını girin: ")
        yeni_liste = []
        silindi = False
        
        try:
            with open(self.dosya_adi, "r", encoding="utf-8") as file:
                satirlar = file.readlines()
                
            for satir in satirlar:
                if silinecek_numara not in satir.split()[-1]:
                    yeni_liste.append(satir)
                else:
                    silindi = True
                    
            if silindi:
                with open(self.dosya_adi, "w", encoding="utf-8") as file:
                    file.writelines(yeni_liste)
                print("Öğrenci silme işlemi başarılı")
            else:
                print("Öğrenci bulunamadı")
                
        except FileNotFoundError:
            print("Öğrenci dosyası bulunamadı!")

    def ogrenci_guncelle(self):
        aranan_numara = input("Güncellemek istediğiniz öğrencinin numarasını girin: ")
        yeni_liste = []
        guncellendi = False
        
        try:
            with open(self.dosya_adi, "r", encoding="utf-8") as file:
                satirlar = file.readlines()
                
            for satir in satirlar:
                if aranan_numara in satir.split()[-1]:
                    print("Yeni bilgileri girin:")
                    yeni_isim = input("Yeni isim: ")
                    yeni_soyisim = input("Yeni soyisim: ")
                    yeni_numara = input("Yeni numara: ")
                    yeni_liste.append(f"{yeni_isim} {yeni_soyisim} {yeni_numara}\n")
                    guncellendi = True
                else:
                    yeni_liste.append(satir)
                    
            if guncellendi:
                with open(self.dosya_adi, "w", encoding="utf-8") as file:
                    file.writelines(yeni_liste)
                print("Öğrenci güncelleme işlemi başarılı")
            else:
                print("Öğrenci bulunamadı")
                
        except FileNotFoundError:
            print("Öğrenci dosyası bulunamadı!")

class Ogretmen:
    def __init__(self):
        print("Öğretmen kısmına giriş yaptınız")
        self.dosya_adi = "notlar.txt"
        self.menu()

    def menu(self):
        while True:
            print("\nÖğrenci not girişi yapmak için-1, Öğrenci listeleme için-2, Çıkış için-3")
            
            try:
                islem = int(input("İşlem numarasını giriniz: "))
                
                if islem == 1:
                    self.not_girisi()
                elif islem == 2:
                    self.not_listele()
                elif islem == 3:
                    print("Çıkış yapılıyor...")
                    break
                else:
                    print("Geçersiz işlem numarası!")
            except ValueError:
                print("Lütfen geçerli bir sayı girin!")

    def not_girisi(self):
        adet = int(input("Kaç öğrenci notu girmek istiyorsunuz: "))
        not_listesi = []
        
        for i in range(adet):
            isim = input("Öğrenci ismini girin: ")
            soyisim = input("Öğrenci soyismini girin: ")
            numara = input("Öğrenci numarasını girin: ")
            notu = input("Öğrenci notunu girin: ")
            not_listesi.append(f"{isim} {soyisim} {numara} {notu}\n")

        with open(self.dosya_adi, "a", encoding="utf-8") as file:
            file.writelines(not_listesi)
        print("Öğrenci not girişi başarıyla yapıldı")

    def not_listele(self):
        print("Öğrenci not listesi:")
        try:
            with open(self.dosya_adi, "r", encoding="utf-8") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("Not dosyası bulunamadı!")

class Ogrenci:
    def __init__(self):
        print("Öğrenci sistemine giriş yaptınız")
        self.dosya_adi = "notlar.txt"
        self.menu()

    def menu(self):
        while True:
            print("\nÖğrenci not görüntüleme için-1, Çıkış için-2")
            
            try:
                islem = int(input("İşlem numarasını giriniz: "))
                
                if islem == 1:
                    self.not_goruntule()
                elif islem == 2:
                    print("Çıkış yapılıyor...")
                    break
                else:
                    print("Geçersiz işlem numarası!")
            except ValueError:
                print("Lütfen geçerli bir sayı girin!")

    def not_goruntule(self):
        numara = input("Öğrenci numaranızı giriniz: ")
        bulundu = False
        
        try:
            with open(self.dosya_adi, "r", encoding="utf-8") as file:
                for satir in file:
                    if numara in satir.split()[2]:
                        print(satir.strip())
                        bulundu = True
                        break
            if not bulundu:
                print("Böyle bir öğrenci bulunamadı")
        except FileNotFoundError:
            print("Not dosyası bulunamadı!")

if __name__ == "__main__":
    okul = OkulSistem()