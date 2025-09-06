import pandas as pd

class PaandasLesson(object):
    def __init__(self):
        self.data={#dictionary tipinde veriler tanımlandı
            "name":[" ali","veli","ayşe","fatma"],
            "age":[20,30,25,35],
            "city":["istanbul","ankara","izmir","bursa"]
        }
        self.df=pd.DataFrame(self.data, index=[1,2,3,4])#dataframe oluşturuldu ve index verildi
        print(self.df)#dataframe yazdırıldı
        print("-------------------")
        self.line=self.df.head(2)#ilk 2 satır alındı
        print(self.line)
        print("-------------------")
        self.name_age=self.df[["name","age"]]#sadece name ve age sütunları alındı
        print(self.name_age)
        print("-------------------")
        self.average_age=self.df["age"].mean()#age sütununun ortalaması alındı
        print("Ortalama yaş:",self.average_age)
        print("-------------------")
        self.filtre=self.df[self.df["age"] >27]#age sütunu 27 den büyük olanlar filtrelendi
        print(self.filtre)

PaandasLesson()

