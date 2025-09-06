import pandas as pd

class PaandasLesson(object):
    def __init__(self):
        self.data = {
            "isim": ["Ali", "Veli", "Ayşe", "Fatma", "Ahmet", "Zeynep"],
            "yas": [20, 30, 25, 35, 40, 30],
            "sehir": ["İstanbul", "Ankara", "İzmir", "Bursa", "İstanbul", "Ankara"],
            "maas": [8000, 12000, 9500, 11000, 15000, 12500]
        }
        self.df = pd.DataFrame(self.data)
        print(self.df)
        print("-------------")

        
        self.filtre1 = self.df[self.df["yas"] > 30]
        print(self.filtre1)
        print("-------------")

        
        self.filtre2 = self.df.sort_values("maas", ascending=False)
        print(self.filtre2)
        print("-------------")

       
        self.df["maas_kategori"] = self.df["maas"].apply(
            lambda x: "Düşük" if x < 10000 else ("Orta" if x < 12000 else "Yüksek")
        )
        print(self.df)
        print(self.df["maas_kategori"].value_counts())
        print("-------------")

        
        self.filtre4 = self.df.groupby("sehir")[["maas","yas"]].mean()
        print(self.filtre4)

PaandasLesson()





