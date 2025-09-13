import matplotlib.pyplot as plt  # matplotlib'in pyplot modülünü 'plt' takma adıyla içe aktarır.
import numpy as np               # NumPy kütüphanesini 'np' olarak içe aktarır (sayısal işlemler için).

class MediumPlot:
    # class (sınıf): ilgili fonksiyonlar ve veriler etrafında mantıksal bir grup oluşturur.
    def __init__(self):
        """
        __init__ : Python'da sınıfın kurucusu (constructor). 
        self : oluşturulan örneği (instance) temsil eder; örneğe ait metod ve değişkenlere erişimi sağlar.
        Burada kurucu içinde üç farklı çizim metodunu çağırıyoruz.
        NOT: __init__ içinde otomatik gösterim (show) yaptığımız için sınıf örneği oluşturulduğunda
        figürler anında gösterilecektir. İstersen show çağrılarını dışarı alıp daha kontrollü davranabilirsin.
        """
        self.plot_example1()
        self.plot_example2()
        self.plot_example3()

    def plot_example1(self):
        # Yeni bir figure oluşturmak: her grafik için ayrı pencere/figure olmasını sağlar.
        plt.figure(figsize=(8, 4))  # figsize=(genişlik, yükseklik) in inches

        # np.linspace(start, stop, num) : belirtilen aralıkta eşit aralıklı 'num' adet değer üretir.
        x = np.linspace(0, 10, 100)   # 0 ile 10 arasında 100 nokta
        y = np.sin(x)                 # sin fonksiyonunu tüm x değerleri için uygular (eleman-elemana)
        y2 = np.cos(x)                # cos fonksiyonu

        # Eksen etiketleri ve başlık:
        plt.xlabel("X Ekseni")        # x ekseni yazısı
        plt.ylabel("Y Ekseni")        # y ekseni yazısı
        plt.title("Orta Seviye Matplotlib Örneği")  # grafik başlığı

        # plt.plot(x, y, ...) : x-y verisini çizmek için kullanılır.
        # önemli parametreler:
        #   color : çizgi rengi ("b"=blue, "r"=red vb.); burada kural olarak matplotlib renk isimleri veya hex kullanılabilir.
        #   marker : veri noktalarını işaretleme şekli ("o" daire, "s" kare vb.)
        #   linestyle : çizgi stili ("-" düz, "--" kesik, "-." noktalı çizgi vb.)
        #   linewidth : çizgi kalınlığı
        #   label : legend'de gösterilecek isim
        plt.plot(x, y, color="b", marker="o", linestyle="--", linewidth=2, label="sin(x)")
        plt.plot(x, y2, color="r", marker="o", linestyle="-.", linewidth=2, label="cos(x)")

        # plt.legend() : plotlarda label parametresi ile verilen isimleri gösterir.
        plt.legend()  

        # plt.grid() : arka plan ızgarasını açar; görsel okumayı kolaylaştırır.
        plt.grid()

        # plt.show() : oluşturulan figure'i gösterir (çoğu ortamda bloklayıcı olabilir).
        plt.show()

    def plot_example2(self):
        # Öğrenci isimleri (categorical / string) ve notlar (sayısal)
        ogrenvi = ["ali", "veli", "ayse", "fatma", "ahmet"]
        notlar = [55, 70, 65, 80, 90]

        # ort : notlar listesinin ortalaması
        ort = np.mean(notlar)  # np.mean(array) -> aritmetik ortalama

        # Yeni figure açıyoruz (her grafik için ayrı figure önerilir)
        plt.figure(figsize=(8, 4))

        # NOT: orijinal kodunda plt.plot(notlar, ogrenvi) vardı; bu hata verir çünkü
        # plot x ve y için sayısal değerler bekler. Kategorik isimler için daha uygun gösterim bar grafiktir.
        # Burada öğrenci isimlerini x eksenine koyup, notları bar yüksekliği olarak çiziyoruz.
        plt.bar(ogrenvi, notlar, label="Notlar", edgecolor="black")  
        # plt.bar(xlabels, heights, ...) : çubuk grafik; kategorik x için uygundur.

        plt.xlabel("Öğrenci İsimleri")
        plt.ylabel("Notlar")
        plt.title("Öğrenci Notları")

        # Ortalama çizgisi: notların ortalamasını yatay bir çizgi (axhline) ile gösteriyoruz.
        # plt.axhline(y=value, ...) : yatay çizgi; axvline ise dikey çizgidir.
        plt.axhline(ort, color="r", linestyle="--", label=f"Ortalama: {ort:.2f}")

        # Eğer isimler sıkışıyorsa xticks ile döndürme yapmak okunabilirliği artırır:
        plt.xticks(rotation=25)  # x ekseni etiketlerini 25 derece döndür

        plt.grid(axis="y", linestyle=":", alpha=0.7)  # sadece yatay ızgarayı açtık (axis="y")
        plt.legend()
        plt.show()

    def plot_example3(self):
        # Rastgele tamsayı verisi oluşturma:
        # np.random.randint(low, high, size) : low (dahil) ile high (hariç) arasında rastgele tamsayılar üretir
        numbers = np.random.randint(0, 50, 200)  # 0-49 arasında 200 rastgele sayı

        plt.figure(figsize=(8, 4))

        # plt.hist(data, bins=...) : histogram oluşturur
        # bins : sayıyı gruplara (aralıklara) ayırır; örn bins=20 -> 20 aralık
        # edgecolor : her bar'ın kenar rengini belirler
        # label : legend için etiket
        plt.hist(numbers, bins=20, color="b", edgecolor="black", label="veri dağılımı")

        plt.xlabel("Aralıklar")
        plt.ylabel("Frekans")
        plt.title("Histogram Grafiği")

        # plt.grid(color="gray") : ızgaranın rengini belirtme (isteğe bağlı)
        plt.grid(color="gray", linestyle="--", alpha=0.5)

        plt.legend()
        plt.show()


# Sınıfı örnekleyerek (instantiate) tüm grafikleri oluşturup gösteriyoruz.
# Çağrı yapıldığında __init__ içindeki plot fonksiyonları çalışır ve üç figure sırayla gösterilir.
MediumPlot()
