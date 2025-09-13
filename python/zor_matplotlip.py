import matplotlib.pyplot as plt
import numpy as np

class HardExsample:
    def __init__(self):
        # Sınıf çağrıldığında 3 farklı örnek otomatik çalışacak
        self.plot_exsample1()
        self.plot_exsample2()
        self.plot_exsample3()

    def plot_exsample1(self):
        """
        ÖRNEK 1: Karesi ve Küpü karşılaştırma grafikleri
        """
        array1 = np.array([1, 2, 4, 5, 6])   # Sayılardan oluşan bir numpy array
        y = array1**2   # Sayıların karesi
        y1 = array1**3  # Sayıların küpü (önceden ^ yanlış kullanılıyordu)

        # 2 alt grafik (subplot) oluşturuluyor (2 satır, 1 sütun)
        fig, axs = plt.subplots(2, 1, figsize=(6, 6))

        # İlk grafik: Kare değerleri
        axs[0].plot(array1, y, color="r", marker="o", label="Karesi")
        axs[0].set_title("Kare Grafiği")  # Grafik başlığı
        axs[0].legend()  # Açıklama kutusu

        # İkinci grafik: Küp değerleri
        axs[1].plot(array1, y1, color="b", marker="o", label="Küpü")
        axs[1].set_title("Küp Grafiği")
        axs[1].legend()

        # Grafikler arası boşlukları ayarlama
        plt.tight_layout()
        plt.show()  # Grafik ekranda gösterilir

    def plot_exsample2(self):
        """
        ÖRNEK 2: 2D Fonksiyon görselleştirme
        """
        # X ve Y eksenleri için -5 ile 5 arasında 100 nokta oluştur
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)

        # Meshgrid ile 2D koordinat sistemi (matris) oluştur
        # Örn: X matrisi tüm satırlarda x değerini tekrarlar
        #      Y matrisi tüm sütunlarda y değerini tekrarlar
        X, Y = np.meshgrid(x, y)

        # Her (x,y) noktası için sin(sqrt(x²+y²)) fonksiyonunu hesapla
        Z = np.sin(np.sqrt(X**2 + Y**2))

        # imshow ile 2D görselleştirme yapılır
        plt.imshow(Z, extent=[-5, 5, -5, 5], origin="lower", cmap="viridis")

        # Sağ tarafta renk skalası ekle
        plt.colorbar(label="sin(sqrt(x²+y²))")

        # Grafik açıklamaları
        plt.xlabel("X değerleri")
        plt.ylabel("Y değerleri")
        plt.title("2D Fonksiyon Görselleştirme")
        plt.show()

    def plot_exsample3(self):
        """
        ÖRNEK 3: Günlere göre sıcaklık grafiği
        """
        # 1'den 30'a kadar günler
        x = np.arange(1, 31)

        # Her gün için 15 ile 35 arasında rastgele sıcaklık değerleri üret
        y = np.random.randint(15, 35, 30)

        # Maksimum ve minimum sıcaklıkları bul
        max_val = y.max()
        min_val = y.min()

        # Günlere göre sıcaklık çizgisi
        plt.plot(x, y, color="b", linestyle="--", marker="o", label="Derece")

        # Maksimum nokta (kırmızı)
        plt.plot([x[np.argmax(y)]], [max_val], color="red", marker="o", label="Maksimum")

        # Minimum nokta (yeşil)
        plt.plot([x[np.argmin(y)]], [min_val], color="green", marker="o", label="Minimum")

        # Grafik açıklamaları
        plt.xlabel("Günler")
        plt.ylabel("Sıcaklık (°C)")
        plt.title("Sıcaklık Zaman Grafiği")
        plt.legend()   # Açıklama kutusu
        plt.grid(True) # Izgara çizgileri
        plt.show()


# Sınıf çağrılarak tüm fonksiyonlar otomatik çalıştırılır
HardExsample()
