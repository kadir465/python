class Magza(object):
    def __init__(self,urun_adi,urun_fiyat,urun_adet):
        self.urun_adi=urun_adi
        self.urun_fiyat=urun_fiyat
        self.urun_adet=urun_adet

        self.magza_listesi =[]
        print("Mağaza listesi oluşturuluyor...")
        print("bitirmek için '=' ya basın")
        while True:
            urun_adi=input("Ürün adı giriniz: ")
            if urun_adi == '=':
                break
            urun_adet_str=input("Ürün adedi giriniz: ")
            if urun_adet_str == '=':
                break
            urun_adet = int(urun_adet_str)
            urun_fiyat_str=input("Ürün fiyatı giriniz: ")
            if urun_fiyat_str == '=':
                break
            urun_fiyat = float(urun_fiyat_str)

            self.magza_listesi.append(urun_adi)
            self.magza_listesi.append(urun_adet)
            self.magza_listesi.append(urun_fiyat)

        print("Mağaza listeniz oluşturuldu...")
        print("Mağaza listeniz: ",self.magza_listesi)



    def İslemler(self,güncelleme,ekle,):
        self.güncelleme=güncelleme
        self.ekle=ekle
   

        self.islem=input("Yapmak istediğiniz işlemi giriniz: "
                         "1-güncelleme, 2-ekleme ")
        
        if self.islem == "1":
            self.güncelleme()
        elif self.islem == "2":
            self.ekle()
        

    def güncelleme(self):
        print("Güncelleme işlemi seçildi...")
        urun_adi=input("güncellemek istediğiniz ürün aadını giriniz: ")
        yeni_urun_adi=input("yeni ürün adını giriniz: ")
    
        if urun_adi in self.magza_listesi:
             index=self.magza_listesi.index(urun_adi)
             self.magza_listesi[index]=yeni_urun_adi
             print("Güncelleme işlemi başarılı...") 

        urun_adet=int(input("güncellemek istediğiniz ürün adedini giriniz: "))
        yeni_urun_adet=int(input("yeni ürün adedini giriniz: "))

        if urun_adet in self.magza_listesi:
             index=self.magza_listesi.index(urun_adet)
             self.magza_listesi[index]=yeni_urun_adet
             print("Güncelleme işlemi başarılı...")
        
        urun_fiyat=float(input("güncellemek istediğiniz ürün fiyatını giriniz: "))
        yeni_urun_fiyat=float(input("yeni ürün fiyatını giriniz: "))
         
        if urun_fiyat in self.magza_listesi:
            index=self.magza_listesi.index(urun_fiyat)
            self.magza_listesi[index]=yeni_urun_fiyat
            print("Güncelleme işlemi başarılı...")

        print("Güncellenmiş mağaza listeniz: ",self.magza_listesi)


    def ekle(self):
        print("ekleme işlemi seçildi...")
        adet=int(input("kaç ürün eklemek istiyorsunuz: "))

        for i in range(adet):
            self.urun_adi=input("Ürün adı giriniz: ")
            self.urun_adet=int(input("Ürün adedi giriniz: "))
            self.urun_fiyat=float(input("Ürün fiyatı giriniz: "))
            self.magza_listesi.append(self.urun_adi)
            self.magza_listesi.append(int(self.urun_adet))
            self.magza_listesi.append(float(self.urun_fiyat))
        print("Ekleme işlemi başarılı...")
n=Magza("urun_adi","urun_adet","urun_fiyat")
n.İslemler(n.güncelleme,n.ekle)

