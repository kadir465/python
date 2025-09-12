import numpy as np

class LessonNumpy(object):
    def __init__(self):
        # Sınıf çağrıldığında aşağıdaki örnek fonksiyonları çalıştırır
        self.example_array()
        self.example_matrix()
        self.example_multiplication()
        self.example_sqrt_array()
        self.example_min_tracking()

    def example_array(self):
        # Ortalama 0, standart sapması 1 olan normal dağılımdan
        # 100 rastgele sayı üret, sonra bunları 10 ile çarpıp integer yap
        array = (np.random.normal(loc=0, scale=1, size=100) * 10).astype(int)
        print("Rastgele Array (100 eleman):")
        print(array)
        print("-" * 30)

        # NumPy ile ortalama ve varyans hesaplama
        print("Ortalama:", np.mean(array))
        print("Varyans:", np.var(array))
        print("=" * 50)

    def example_matrix(self):
        # 10x10 boyutunda, normal dağılımlı rastgele sayılardan oluşan matris
        array2 = (np.random.randn(10, 10) * 10).astype(int)
        print("10x10 Matris:")
        print(array2)

        # Köşegen elemanları alır
        print("Köşegen (diagonal):", np.diagonal(array2))

        # Maksimum ve minimum değerleri bulur
        print("Maksimum:", np.max(array2), "Minimum:", np.min(array2))
        print("=" * 50)

    def example_multiplication(self):
        # 4x4 boyutunda iki farklı rastgele matris üret
        array3 = (np.random.randn(4, 4) * 10).astype(int)
        array4 = (np.random.randn(4, 4) * 10).astype(int)
        print("4x4 Matris A:")
        print(array3)
        print("4x4 Matris B:")
        print(array4)

        # İki matrisi eleman eleman çarpar (Hadamard product)
        print("Eleman Eleman Çarpım (A * B):")
        print(np.multiply(array3, array4))
        print("=" * 50)

    def example_sqrt_array(self):
        # 0'dan 99'a kadar olan sayıların kareköklerini hesapla
        array5 = np.sqrt(np.arange(100))
        print("0-99 arası sayıların karekökleri (NumPy array):")
        # İlk 10 elemanı gösterelim
        print(array5[:10], "...")
        print("=" * 50)

    def example_min_tracking(self):
        # 100 rastgele sayı üret
        array6 = (np.random.randn(100) * 10).astype(int)
        print("Array6 (100 eleman):")
        print(array6)

        # İlk elemanı başlangıç olarak al
        new_array6 = [array6[0]]
        min_value = array6[0]

        # Her bir elemanı sırayla dolaş
        for val in array6[1:]:
            # Eğer eleman mevcut minimumdan büyükse listeye ekle
            if val > min_value:
                new_array6.append(val)
                min_value = val

        # Listeyi NumPy array’e dönüştür
        new_array6 = np.array(new_array6)
        print("Artan minimumları takip eden yeni array:")
        print(new_array6)
        print("=" * 50)


# Sınıfı çağırarak tüm fonksiyonların çalışmasını sağlıyoruz
LessonNumpy()
