import json

class Magza_Sistemi():
    def __init__(self):
        print("Mağazamıza Hoşgeldiniz")
        print("hesabınız varsa 'giriş' yazınız, yoksa 'kayıt' yazınız")
        self.islem = input("işlem: ")

        if self.islem == "giriş":
            self.giris()
        elif self.islem == "kayıt":
            self.kayit()
        else:
            print("Geçersiz işlem, lütfen tekrar deneyin.")
            self.__init__()

    def kayit(self):
        print("Kayıt sayfasındasınız. Lütfen bilgilerinizi giriniz.")

        self.ad = input("Adınız ve soyadınız: ")
        self.Sifre = input("Şifreniz: ")

       
        try:
            with open("kullanicilar.json", "r", encoding="utf-8") as file:
                file_data = json.load(file)
        except FileNotFoundError:
            file_data = {"kullanıcılar": []}

        file_data["kullanıcılar"].append({"ad": self.ad, "şifre": self.Sifre})
        
        with open("kullanicilar.json", "w", encoding="utf-8") as file:
            json.dump(file_data, file, ensure_ascii=False, indent=4)
        
        print("Kayıt işlemi başarılı")
        print("Giriş sayfasına yönlendiriliyorsunuz")
        self.giris()
    
    def giris(self):
        print("Giriş sayfasındasınız")
        print("Lütfen bilgilerinizi giriniz")
        print("Görevli iseniz 1'e, müşteriyseniz 2'ye basınız")
        
        try:
            giris_secimi = int(input("işlem: "))
        except ValueError:
            print("Geçersiz giriş, lütfen 1 veya 2 yazın.")
            self.giris()
            return

        if giris_secimi == 1:
            print("Görevli girişi")
            self.ad = input("Adınız ve soyadınız: ")
            self.Sifre = input("Şifreniz: ")
            
            try:
                with open("görevli.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
            except FileNotFoundError:
                print("Görevli kaydı bulunamadı.")
                self.giris()
                return
            
            giris_basarili = False
            for i in data["görevli"]:
                if self.ad == i["ad"] and self.Sifre == i["şifre"]:
                    print("Giriş başarılı")
                    Gorevli()
                    giris_basarili = True
                    break
            
            if not giris_basarili:
                print("Bilgileriniz hatalı")
                self.giris()
                
        elif giris_secimi == 2:
            print("Müşteri girişi")
            self.ad = input("Adınız ve soyadınız: ")
            self.Sifre = input("Şifreniz: ")
            
            try:
                with open("kullanicilar.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
            except FileNotFoundError:
                print("Henüz hiç kullanıcı kaydı bulunmamaktadır.")
                self.giris()
                return
            
            giris_basarili = False
            for i in data["kullanıcılar"]:
                if self.ad == i["ad"] and self.Sifre == i["şifre"]:
                    print("Giriş başarılı")
                    Musteri()
                    giris_basarili = True
                    break
            
            if not giris_basarili:
                print("Bilgileriniz hatalı")
                self.giris()
        else:
            print("Geçersiz seçim")
            self.giris()

class Gorevli():
    def __init__(self):
        print("Görevli sayfasındasınız")
        print("Yapmak istediğiniz işlemi seçiniz")
        print("1-Ürün ekleme")
        print("2-Ürün silme")
        print("3-Ürün listeleme")
        
        try:
            self.islem = int(input("işlem: "))
        except ValueError:
            print("Geçersiz işlem")
            self.__init__()
            return

        if self.islem == 1:
            try:
                with open("urunler.json", "r", encoding="utf-8") as file:
                    file_data = json.load(file)
            except FileNotFoundError:
                file_data = {"ürünler": []}
            
            self.id = input("Ürün id: ")
            self.ad = input("Ürün adı: ")
            self.fiyat = input("Ürün fiyat: ")
            self.stok = input("Ürün stok: ")
            
            file_data["ürünler"].append({
                "id": self.id,
                "ad": self.ad,
                "fiyat": self.fiyat,
                "stok": self.stok
            })
            
            with open("urunler.json", "w", encoding="utf-8") as file:
                json.dump(file_data, file, ensure_ascii=False, indent=4)
            
            print("Ürün eklendi")
            
        elif self.islem == 2:
            try:
                with open("urunler.json", "r", encoding="utf-8") as file:
                    file_data = json.load(file)
            except FileNotFoundError:
                print("Henüz hiç ürün bulunmamaktadır.")
                self.__init__()
                return
            
            silinecek_id = input("Silinecek ürün id: ")
            urun_bulundu = False
            
            for i in file_data["ürünler"]:
                if silinecek_id == i["id"]:
                    file_data["ürünler"].remove(i)
                    urun_bulundu = True
                    print("Ürün silindi")
                    break
            
            if not urun_bulundu:
                print("Ürün bulunamadı")
            else:
                with open("urunler.json", "w", encoding="utf-8") as file:
                    json.dump(file_data, file, ensure_ascii=False, indent=4)
                    
        elif self.islem == 3:
            try:
                with open("urunler.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
                
                for i in data["ürünler"]:
                    print(f"Ürün id: {i['id']}, Ürün adı: {i['ad']}, Ürün fiyat: {i['fiyat']}, Ürün stok: {i['stok']}")
            except FileNotFoundError:
                print("Henüz hiç ürün bulunmamaktadır.")
        else:
            print("Geçersiz işlem")
            self.__init__()

class Musteri():
    def __init__(self):
        print("Müşteri sayfasındasınız")
        print("Yapmak istediğiniz işlemi seçiniz")
        print("1-Ürün sorgulama")
        print("2-Ürün satın alma")
        
        try:
            self.islem = int(input("işlem: "))
        except ValueError:
            print("Geçersiz işlem")
            self.__init__()
            return

        if self.islem == 1:
            print("Ürün sorgulama sayfasındasınız")
            self.aranan_urun = input("Aranan ürün adı: ")
            self.aranan_urun_id = input("Aranan ürün id: ")
            
            try:
                with open("urunler.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
                
                urun_bulundu = False
                for i in data["ürünler"]:
                    if self.aranan_urun == i["ad"] and self.aranan_urun_id == i["id"]:
                        print(f"Ürün id: {i['id']}, Ürün adı: {i['ad']}, Ürün fiyat: {i['fiyat']}, Ürün stok: {i['stok']}")
                        print("Ürün bulundu")
                        urun_bulundu = True
                        break
                
                if not urun_bulundu:
                    print("Ürün bulunamadı")
                    
            except FileNotFoundError:
                print("Henüz hiç ürün bulunmamaktadır.")
                
        elif self.islem == 2:
            print("Ürün satın alma sayfasındasınız")
            self.satın_alınacak_urun = input("Satın alınacak ürün adı: ")
            self.satın_alınacak_urun_id = input("Satın alınacak ürün id: ")
            
            try:
                with open("urunler.json", "r", encoding="utf-8") as file:
                    file_data = json.load(file)
                
                urun_bulundu = False
                for i in file_data["ürünler"]:
                    if self.satın_alınacak_urun == i["ad"] and self.satın_alınacak_urun_id == i["id"]:
                        print(f"Ürün id: {i['id']}, Ürün adı: {i['ad']}, Ürün fiyat: {i['fiyat']}, Ürün stok: {i['stok']}")
                        
                        if int(i["stok"]) > 0:
                            i["stok"] = str(int(i["stok"]) - 1)
                            print("Ürün satın alındı")
                            print("Stoktan düşüldü")
                        else:
                            print("Ürün stokta kalmamıştır")
                            
                        urun_bulundu = True
                        break
                
                if not urun_bulundu:
                    print("Ürün bulunamadı")
                else:
                    with open("urunler.json", "w", encoding="utf-8") as file:
                        json.dump(file_data, file, ensure_ascii=False, indent=4)
                        
            except FileNotFoundError:
                print("Henüz hiç ürün bulunmamaktadır.")
        else:
            print("Geçersiz işlem")
            self.__init__()

# Programı başlat
if __name__ == "__main__":
    Magza_Sistemi()
