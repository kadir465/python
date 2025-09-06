import pandas as pd

class PandasLesson1:
    def __init__(self):
        self.url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        self.data=pd.read_csv(self.url)# data yüklemesi yapıldı
        self.df=pd.DataFrame(self.data)
       
        self.nan_value=self.df.isna().sum()# eksik değerlerin sayısı
        print(self.nan_value)
        self.age_mean=self.df["Age"].mean()# yaş ortalaması alındı
        print(self.age_mean)
        self.df["Age"].fillna(self.age_mean, inplace=True)# yaş sütunundaki eksik değerler yaş ortalaması ile dolduruldu
        self.df["Cabin"].fillna("Unknown",inplace=True)# kabin sütunundaki eksik değerler "Unknown" ile dolduruldu
        self.df["Embarked"].fillna("S",inplace=True)# Embarked sütunundaki eksik değerler "S" ile dolduruldu
        self.new_nan_value=self.df.isna().sum()# eksik değerlerin sayısı
        print(self.new_nan_value)
        print("\n")
        print("---------------------------------------")
        self.df["AgeGroup"]=self.df["Age"].apply(lambda x: "Child" if 0<=x<=12 else("Teen" if 13<=x<=19 else("Adult" if 20<=x<=59 else "Senior")))# yaşa göre gruplandırma yapıldı
        print(self.df[["Age","AgeGroup"]].head(10))#yaş ve yaş grubu sütunların ilk 10 satırı yazılır yazdırıldı
        print("\n")
        print("---------------------------------------")
        self.df["FamilySize"]=self.df["SibSp"]+self.df["Parch"]+1# aile büyüklüğü hesaplandı
        print(self.df.head(5))# ilk 5 satır yazdırıldı
        print("\n")
        print("---------------------------------------")
        survival_rate =self.df.groupby("Sex")["Survived"].mean()#cinsiyete göre hayatta kalma oranı hesaplaması
        print(survival_rate)
        print("\n")
        print("---------------------------------------")

        self.Travel_mean=self.df.groupby("Pclass")[["Fare","Age"]].mean()# yolculuk sınıfına göre ücret ve yaş ortalaması
        print(self.Travel_mean)
        print("\n")
        print("---------------------------------------")

        self.pivot_table=self.df.pivot_table(index="Sex", columns="Pclass", values="Survived", aggfunc="mean")#pivot tablosu oluşturuldu pclass süun adlları sex de satır adları oldu ortalama değerleri de elemanlar oldu
        print(self.pivot_table)
        print("\n")
        print("---------------------------------------")
        self.df["FareCategory"]=self.df["Fare"].apply(lambda x: "low" if x<=10 else("medium" if 10<x<=50 else("high" if 50<x<=100 else "very high")))# ücrete göre kategori oluşturuldu
        print(self.df.head(10))# ilk 10 satır yazdırıldı
        print(self.df.tail(10))# son 10 satır yazdırıldı


      
        
        

PandasLesson1()
