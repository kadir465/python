import pandas as pd

class PandasLesson1:
    def __init__(self):
        self.data={# dictionary tipinde verileri veriyoruz
          
                "isim": ["Ali", "Veli", "Ayşe", "Fatma", "Ahmet", "Zeynep", "Can", "Ece", "Deniz", "Bora"],
                "departman": ["IT", "Muhasebe", "IT", "Pazarlama", "Muhasebe", "IT", "Pazarlama", "Muhasebe", "IT", "Pazarlama"],
                "maas": [8000, 12000, 9500, 11000, 15000, 12500, 9000, 11500, 13000, 9500],
                "yil": [2024, 2024, 2025, 2024, 2025, 2025, 2025, 2024, 2025, 2025],
                "performans": [70, 85, 90, 60, 95, 80, 75, 88, 92, 77]
     }
        self.df=pd.DataFrame(self.data,index=[1,2,3,4,5,6,7,8,9,10])# DataFrame oluşturuyoruz ve index veriyoruz
        print(self.df)
        print("\n")
        print("-------------------")

        self.departman_maas_rank=self.df.groupby("departman")["maas"].rank(method="dense", ascending=False)#departmanlara göre maaş sıralaması yapıyoruz her departman kendi içinde sıralanır
        self.df["departman_maas_rank"]=self.departman_maas_rank
        print(self.df)
        print("\n")
        print("-------------------")
        self.maas_katagori=self.df["maas"].apply(lambda x: "düşük" if x<10000 else("orta" if 10000<=x<12000 else "yüksek"))# maaş kategorisi oluşturuyoruz fltreleme yapıyoruz
        self.df["maas_katagori"]=self.maas_katagori
        print(self.df)
        print("\n")
        print("-------------------")

        self.performans_ort = self.df.groupby("departman")["performans"].transform("mean")#departmanlara göre performans ortalaması alıyoruz
        self.yuksek_perf = self.df[self.df["performans"] > self.performans_ort]#performans ortalamsı üztünü alıyoruz
        print(self.yuksek_perf)

        print("\n")
        print("-------------------")
        self.df["cum_employe"]=self.df.groupby("departman").cumcount()+1#depaertmanlara göre çalışan sayısını veriyor cumcount aynı stringin kaçtane olduğunu bulur
        print(self.df)

PandasLesson1()
