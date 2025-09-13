import matplotlib.pyplot as plt#import edecen

class SimplePlot:
    def __init__(self):
        self.plot_example1()#fonksiyonlar çağırıldı
        self.plot_example2()
        self.plot_example3()
    

    def plot_example1(self):
        x=[1, 2, 3, 4, 5]
        y=[2,4,6,8,10]

        plt.xlabel("X Ekseni")# grafiğin x ekseninin adı
        plt.ylabel("Y Ekseni")#grafiğin y ekseninin adı
        plt.title("Basit Matplotlib Örneği")#graiğin başlığı 

        plt.plot(x,y)#çizgigrafiği oluşturur
        plt.show()#grafiği gösterir
    
    def plot_example2(self):
         katagori = ["elma", "muz", "çilek", "portakal"]
         deger = [23, 17, 35, 29]

         plt.bar(katagori, deger, label="Meyve miktarları")#bar , çubuk grafiği oluşturu iki parametreyi de alır
         plt.xlabel("Meyve Türleri")
         plt.ylabel("Miktar")
         plt.title("Meyve Miktarları")
         plt.legend()#legend oluşturur bilgilendirme yazısı gibi neyin ne olduğu 
         plt.show()
    def plot_example3(self):
        degerler=[5, 15, 25, 35, 45]
        plt.pie(degerler, labels=["A", "B", "C", "D", "E"], autopct="%1.1f%%",shadow=True, explode=
                (0, 0.1, 0, 0, 0))
        #pie --- pasta grafiği oluşturur /
        #labels --- pastanın her dilminin adını verir
        #autopct -- dilimlerin yüzdelik olmasını sağlar
        #shadow ---gölgelik oluşturu
        #explode --- dilimler arası boşlukları sağar
        plt.title("Basit Pasta Grafiği")
        plt.legend()
        plt.show()

SimplePlot()
