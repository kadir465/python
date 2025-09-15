import pandas as pd

class Veri_Analizi1:
    def __init__(self):
        self.df = pd.read_csv("hava_durumu_2024_zor.csv") 

        self.VeriToChange()
        self.DayCompareHoliday()

    def VeriToChange(self):

        self.heat_avarge=int(self.df["sicaklik"].mean())
        heat_median=int(self.df["sicaklik"].median())
        print(f"sıcaklık ortalaması : {self.heat_avarge} ve sıcaklık medyanı : {heat_median}")

        self.moisture_avarge=int(self.df["nem"].mean())
        moisture_median=int(self.df["nem"].median())
        print(f"nem ortalaması : {self.moisture_avarge} ve nem mediyanı : {moisture_median}")

        self.rain_avarge=int(self.df["yagis"].mean())
        rain_median=int(self.df["yagis"].median())
        print(f"yağış ortalaması : {self.rain_avarge} ve yağış medyanı {rain_median}")

        atama_nem=61
        atama_heat=15.5
        atama_rain=4

        # print("null değerler sayısı")
        # print(df["nem"].isnull().sum())
        # print(df["yagis"].isnull().sum())
        # print(df["sicaklik"].isnull().sum())

        self.df["nem"].fillna(value=atama_nem , inplace=True)
        self.df["sicaklik"].fillna(value=atama_heat, inplace=True)
        self.df["yagis"].fillna(value=atama_rain, inplace=True)

        # print("dolduruldu ve yeni null değer sayısı")
        # print(df["yagis"].isnull().sum())
        # print(df["nem"].isnull().sum())
        # print(df["sicaklik"].isnull().sum())


    
    def DayCompareHoliday(self):

        self.holiday_day=self.df[self.df["tatil"].notnull()]
        #print(self.holiday_day)
        self.holiday_day_sum=len(self.holiday_day)
        
        self.holiday_day_heat_mean=int(self.holiday_day["sicaklik"].mean())
        self.holiday_day_moisture_mean=int(self.holiday_day["nem"].mean())
        self.holiday_day_rain_mean=int(self.holiday_day["yagis"].mean())

        max_yagis_index = self.holiday_day['yagis'].idxmax()
        max_yagis_tarih = self.holiday_day.loc[max_yagis_index, 'tarih']
        max_yagis_deger = self.holiday_day.loc[max_yagis_index, 'yagis']
        max_tatil=self.holiday_day.loc[max_yagis_index,"tatil"]

        print(f"tatildeki En yüksek yağış: {max_yagis_deger} mm, Tarih: {max_yagis_tarih}, {max_tatil}")

        if self.holiday_day_heat_mean > self.heat_avarge:
            print("tatil gümleri sıcaklığı diğer günlerden daha sıcak")
        else:
            print("tatil günlerinin sıcaklığı diğer günlerden daha soğuk")

        if self.holiday_day_moisture_mean> self.moisture_avarge:
            print("tatil günlerindeki nem oranı diğer günlerden daha fazla")
        else:
            print("taril günlerindeki nem oranı diğer günlerden daha az")


Veri_Analizi1()
