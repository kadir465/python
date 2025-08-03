class Footballer:
    def __init__(self):# sınıftan her yeni nesne oluşturulduğunda bu metot çalışır
        self.isim = input("Oyuncu ismi giriniz: ")
        self.numara = input("Oyuncu numarası giriniz: ")
        self.club = input("Oyuncu kulübü giriniz: ")
        self.yas = input("Oyuncu yaşı giriniz: ")

# Futbolcu listesi oluştur birden fazla futbolcu ekleneceği için list kullanılır
futbolcular = []

adet = int(input("Kaç futbolcu gireceksiniz: "))
for i in range(adet):
    print(f"{i+1}. futbolcunun bilgilerini giriniz.")
    print("=====================================")
    f = Footballer()
    futbolcular.append(f) #oluşturulan futbolcuyu listesine ekleme yapar

# Tüm futbolcuları yazdır
for i, f1 in enumerate(futbolcular):
    print(f"\n{i+1}. Futbolcunun Bilgileri:")
    print(f"İsim: {f1.isim}")
    print(f"Numara: {f1.numara}")
    print(f"Kulüp: {f1.club}")
    print(f"Yaş: {f1.yas}")
