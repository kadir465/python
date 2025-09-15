import matplotlib.pyplot as plt
import numpy as np
from veri_analizi1 import Veri_Analizi1

class VeriAnalzi1_1:
    def __init__(self):
        self.NumpyExsample()

    def NumpyExsample(self):
        analiz = Veri_Analizi1()      
        print(analiz.df.head())     
     
        for col in ["yagis", "nem", "sicaklik"]:
              his, bin_edges = np.histogram(analiz.df[col], bins=10)
              print(f"{col} histogramı:", his)
        
        x=analiz.df["sicaklik"]
        x1=analiz.holiday_day_heat_mean


        plt.plot(x , color="b"  ,label="sıcaklık")
        plt.plot(x1, color="red",marker="o",label="tatiller ortalama sıcaklığı")
        plt.legend()
        plt.savefig("foto1.png")
        plt.show()

        y=analiz.df["nem"]
        y1=analiz.holiday_day_moisture_mean

        plt.plot(y, color="green",label="nem")
        plt.plot(y1,color="red",marker="o",label="tatillerde ortalama nem")
        plt.legend()
        plt.savefig("foto2.png")
        plt.show()

        z=analiz.df["yagis"]
        z1=analiz.holiday_day_rain_mean

        plt.plot(z,color="b",label="yağış")
        plt.plot(z1, color="red",marker="o",label="tatillerde ortalama yağış")
        plt.legend()
        plt.savefig("foto3.png")
        plt.show()

        plt.hist(x, bins=15, color='skyblue', edgecolor='black')  # bins: kaç aralık
        plt.xlabel("Sıcaklık (°C)")
        plt.ylabel("Frekans")
        plt.title("Sıcaklık Dağılımı")
        plt.savefig("foto4.png")
        plt.show()

        plt.hist(y,bins=10, color="green",edgecolor="black")
        plt.xlabel("nem")
        plt.ylabel("frekans")
        plt.title("nem dağılımı")
        plt.savefig("foto5.png")
        plt.show()

        plt.hist([x, y, z], bins=20, label=["Sıcaklık", "Nem", "Yağış"], edgecolor='black')
        plt.xlabel("Değer")
        plt.ylabel("Frekans")
        plt.title("Sıcaklık, Nem ve Yağış Dağılımı")
        plt.legend()
        plt.savefig("foto6.png")
        plt.show()

        a=analiz.holiday_day
        
        a1=a["tatil"]
        a2=a["sicaklik"]
        a3=a["nem"]
        a4=a["yagis"]

        plt.bar(a1,a2 , edgecolor="black")
        plt.axhline(y=15.5, color="red", linewidth=3, linestyle="--", label='ortalam')
        plt.xticks(rotation=90) 
        plt.title("tatil günlerinin ortlama sıcaklık tablosu")
        plt.legend()
        plt.savefig("foto7.png")
        plt.show()

        plt.bar(a1,a3 , edgecolor="black")
        plt.axhline(y=61, color="red", linewidth=3, linestyle="--", label='ortalam')
        plt.xticks(rotation=90) 
        plt.title("tatil günlerinin ortlama nem tablosu")
        plt.legend()
        plt.savefig("foto8.png")
        plt.show()

        plt.bar(a1,a4 , edgecolor="black")
        plt.axhline(y=4, color="red", linewidth=3, linestyle="--", label='ortalam')
        plt.xticks(rotation=90) 
        plt.title("tatil günlerinin ortlama yağış tablosu")
        plt.legend()
        plt.savefig("foto9.png")
        plt.show()

        plt.bar(a2,a3, color=['red', 'blue'],edgecolor="black")
        plt.title("tatill günlerinde sıcaklık ve nem grafiği")
        plt.savefig("foto10.png")
        plt.show()

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 8))
        x.plot(ax=ax1, title='Sıcaklık Trendi')
        y.plot(ax=ax2, title='Nem Trendi')
        z.plot(ax=ax3, title='Yağış Trendi')
        plt.tight_layout()
        plt.savefig("foto11.png")
        plt.show()



VeriAnalzi1_1()
