import json

class Magza_Sistemi():
    def __init__(self):
        print("Mağazamıza Hoşgeldiniz")
        print("hesabınız varsa giriş yazınız yoksa kayıt yazınız")
        self.islem=input("işlem: ")

        if self.islem=="giriş":
                self.giris()

        
        elif self.islem=="kayıt":
                self.kayit() 
        

    def kayit(self):
        print("kayıt sayfasındasınız"
              "Lütfen bilgilerinizi giriniz")

        self.ad = input("adınız ve soyadınız : ")
        self.Sifre = input("şifreniz : ")

        with open("kullanıcı.json","r+",encoding="utf-8") as file:
             file_data=json.load(file)
             file_data["kullanıcılar"].append({"ad":self.ad,"şifre":self.Sifre})
             file.seek(0)
             file.write(json.dumps(file_data,ensure_ascii=False,indent=4))
             print("kayıt işlemi başarılı")
        file.close()
        print("giriş sayfasına yönlendiriliyorsunuz")
        self.giris()
    
    def giris(self):
        
               print("giriş sayfasındasınız" \
               "nLütfen bilgilerinizi giriniz" \
               "görevliiseniz 1'e müşteriyseniz 2'ye basınız")
               self.giris=int(input("işlem "))

               if self.giris ==1:
                    print("görevli girişi")
                    self.ad=input("adınız ve soyadınız : ")
                    self.Sifre=input("şifreniz : ")
                    with open("görevli.json","r",encoding="utf-8") as file:
                         data=json.load(file)
                         for i in data["görevli"]:
                                if self.ad==i["ad"] and self.Sifre==i["şifre"]:
                                    print("giriş başarılı")
                                    Gorevli()
                                    break
                                else:
                                    print("bilgileriniz hatalı")
                    file.close()
                
               elif self.giris==2:
                     print("müşteri girişi")
                     self.ad=input("adınız ve soyadınız : ")
                     self.Sifre=input("şifreniz : ")
                     with open("kullanıcı.json","r",encoding="utf-8") as file:
                           data=json.load(file)
                           for i in data["kullanıcılar"]:
                                 if self.ad==i["ad"] and self.Sifre==i["sifre"]:
                                        print("giriş başarılı")
                                        Musteri()
                                        break

                                 else:
                                        print("bilgileriniz hatalı")


class Gorevli():
      def __init__(self):
            print("görevli sayfasındasınız")
            print("yapmak istediğiniz işlemi seçiniz" \
                                    "1-ürün ekleme" \
                                    "2-ürün silme" \
                                    "3-ürün listeleme")
            self.islem=int(input("işlem: "))

            if self.islem== 1:
                  with open("urunler.json","r+",encoding="utf-8") as file:
                        file_data=json.load(file)
                        self.id=input("ürün id: ")
                        self.ad=input("ürün adı: ")
                        self.fiyat=input("ürün fiyat: ")
                        self.stok=input("ürün stok: ")
                        file_data["ürünler"].append({"id":self.id,"ad":self.ad,"fiyat":self.fiyat,})
                        file.seek(0)
                        file.write(json.dumps(file_data,ensure_ascii=False,indent=4))
                        print("ürün eklendi")
                  file.close()
            elif self.islem==2:
                  with open("urunler.json","r+",encoding="utf-8") as file:
                        file_data=json.load(file)
                        silinecek_id=input("silinecek ürün id: ")
                        for i in file_data["ürünler"]:
                               if silinecek_id==i["id"]:
                                     file_data["ürünler"].remove(i)
                                     file.seek(0)
                                     file.write(json.dumps(file_data,ensure_ascii=False,indent=4))
                                     print("ürün silindi")
                  file.close()


            elif self.islem== 3:
                  with open("urunler.json","r",encoding="utf-8") as file:
                        data=json.load(file)
                        for i in data["ürünler"]:
                              print(f"ürün id: {i['id']} ürün adı: {i['ad']} ürün fiyat: {i['fiyat']} ürün stok: {i['stok']}")
                  file.close()

class Musteri():
    def __init__(self):
        print("müşteri sayfasındasınız")
        print("yapmak istediğiniz işlemi seçiniz" \
              "1-ürün sorgulama" \
              "2-ürün satın alma")
        self.islem = int(input("işlem: "))

        if self.islem == 1:
            print("ürün sorgulama sayfasındasınız")
            self.aranan_urun = input("aranan ürün adı: ")
            self.aranan_urun_id=input("aranan ürün id: ")
            with open("urunler.json", "r", encoding="utf-8") as file:
               data=json.load(file)
               for i in data["ürünler"]:
                     if self.aranan_urun==i["ad"] and self.aranan_urun_id==i["id"]:
                           print(f"ürün id: {i['id']} ürün adı: {i['ad']} ürün fiyat: {i['fiyat']} ürün stok: {i['stok']}")
                           print("ürün bulundu")
                           print("satın almak isterseniz 2'ye basınız")
                     else:
                           print("ürün bulunamadı")
            file.close()

        elif self.islem== 2:
              print("ürün satın alma sayfasındasınız")
              self.satın_alınacak_urun=input("satın alınacak ürün adı: ")
              self.satın_alınacak_urun_id=input("satın alınacak ürün id: ")
              with open("urunler.json","r+",encoding="utf-8") as file:
                    file_data=json.load(file)
                    for i in file_data["ürünler"]:
                            if self.satın_alınacak_urun==i["ad"] and self.satın_alınacak_urun_id==i["id"]:
                                    print(f"ürün id: {i['id']} ürün adı: {i['ad']} ürün fiyat: {i['fiyat']} ürün stok: {i['stok']}")
                                    print("ürün satın alındı")
                                    file_data["ürünler"].remove(i)
                                    file.seek(0)
                                    file.write(json.dumps(file_data,ensure_ascii=False,indent=4))
                                    print("stoktan düşüldü")
                            else:
                                    print("ürün bulunamadı")

              file.close()


                  
