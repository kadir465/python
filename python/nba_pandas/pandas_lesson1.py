import pandas as pd

class PandasLesson1(object):
    def __init__(self):
        self.data = pd.read_csv("nba_pandas/practice_nba.csv")# veri setini okuyo
        
        # 1) Her sezonun en yüksek 3 PTS_per_game oyuncusu
        print("1) Her sezonun en yüksek 3 PTS_per_game oyuncusu")
        self.top3 = (
            self.data
            .sort_values(["Season","PTS_per_game"], ascending=[True,False])#büyükten küçüğe sıralıyor
            .groupby("Season")# sezonlara göre grupluyor
            .head(3)[["Season","Player","Team","PTS_per_game"]]#guruplanan her sezon da ilk 3 oyuncuyu alıyor
        )
        print(self.top3)
        print("\n--------------------------------------------------------------\n")

        # 2) Sezonlar boyunca PTS_per_game değişimi (en fazla artış gösteren)
        print("2) Sezonlar boyunca en fazla PTS artışı gösteren oyuncu")
        self.diff_pts = (
            self.data
            .groupby(["Player","Season"])["PTS_per_game"].mean()#sezon ve oyuncu bazında ortalama puan
            .groupby("Player").diff()# oyuncu bazında farkını alıyor (yani bir önceki sezona göre farkı diff yapıyor
        )
        self.data["PTS_diff1"] = (#PTS_diff1 adında yeni bir kolon oluşturdu
            self.data.groupby("Player")["PTS_per_game"]#Player ve PTS_per_game e göre grupladı PTS_diff1 e atadı
            .transform(lambda x: x.diff())
             )

        best_increase = (
            self.data.groupby("Player")["PTS_diff1"]#oluşturduğu PTS_diff1 den player a göre en üksek 5 değeri alıyor
            .max()
            .sort_values(ascending=False)
            .head(5)
        )
        print(best_increase)
        print("\n--------------------------------------------------------------\n")

        # 3) Takım bazında Efficiency değişimi (2014–2019 arasındaki artışlar)
        print("3) 2014–2019 Efficiency artışları")
        self.team_eff = (
            self.data.groupby(["Season","Team"])["Efficiency"].mean().reset_index()#sezon ve takım bazında Efficiency ortalaması alıyor
        )
        pivot_eff = self.team_eff.pivot(index="Team", columns="Season", values="Efficiency")#pivot tablo oluşturuyor satunlar sezon satırlar takım değerler efficiency atıyor
        pivot_eff["increase"] = pivot_eff["2018-2019"] - pivot_eff["2014-2015"]#2014-2015 ile 2018-2019 arasındaki farkı increase kolonuna atıyor
        print(pivot_eff["increase"].sort_values(ascending=False).head(5))#büyükten küçüğe sıralayıp ilk 5 i alıyor
        print("\n--------------------------------------------------------------\n")

        # 4) Efficiency_per_36 hesapla
        print("4) Efficiency per 36 dakika (ilk 10)")
        self.data["dk"] = self.data["Minutes"] / self.data["Games"]# dk kolonu oluşturuyor ve maç başına düşen dakika hesabı yapıyor
        self.data["Efficiency_per_36"] = self.data["Efficiency"] / self.data["dk"] * 36#
        top_eff36 = (
            self.data[self.data["Games"] >= 40]
            .sort_values(["Season","Efficiency_per_36"], ascending=[True,False])
            .groupby("Season")
            .head(10)[["Season","Player","Efficiency_per_36"]]#Games 40 tan büyük olanlar arasından sezon bazında efficiency_per_36 ya göre sıralayıp ilk 10 u alıyor
        )
        print(top_eff36.head(20))#20 tane yazdırıyo
        print("\n--------------------------------------------------------------\n")

        # 5) FG% ve 3P% kırılımı
        print("5) FG% ve 3P% gruplarına göre PTS ve Efficiency ortalamaları")
        self.data["FG_cat"] = pd.qcut(self.data["FG%"], 2, labels=["Düşük FG","Yüksek FG"])#*FG% yi iki gruba ayırıyor düşük ve yüksek olarak
        self.data["TP_cat"] = pd.qcut(self.data["3P%"], 2, labels=["Düşük 3P","Yüksek 3P"])#*3P% yi iki gruba ayırıyor düşük ve yüksek olarak
        summary = (
            self.data.groupby(["FG_cat","TP_cat"])[["PTS_per_game","Efficiency"]]
            .mean()
            .round(2)#2 ondalık basamağa yuvarlıyor
        )
        print(summary)
        print("\n--------------------------------------------------------------\n")

        # 6) En tutarlı oyuncular (std düşük olanlar)
        print("6) En tutarlı oyuncular (PTS std en düşük)")
        self.consistent_player = (
            self.data.groupby("Player")["PTS_per_game"]# oyuncu bazında puan ortalaması alıyor
            .agg(["std","count"])#std ve count hesaplıyor
            .query("count>=2")#en az 2 sezon oynamış oyuncuları filtreliyor
            .sort_values("std")#std ye göre sıralıyor
            .head(10)
        )
        print(self.consistent_player)
        print("\n--------------------------------------------------------------\n")

        # 7) AST ve TOV korelasyonu
        print("7) AST - TOV korelasyonu")
        corr_all = self.data["AST_per_game"].corr(self.data["TOV_per_game"])# koerlasyon hesabı yapıyor
        print("Genel korelasyon:", corr_all)
        corr_season = self.data.groupby("Season").apply(
            lambda g: g["AST_per_game"].corr(g["TOV_per_game"])# sezon bazında korelasyon hesabı yapıyor ve eklem yapıyor
        )
        print("Sezon bazında korelasyon:")
        print(corr_season)
        print("\n--------------------------------------------------------------\n")

        # 8) En çok yükü 5 oyuncuya yükleyen takım
        print("8) En çok yükü 5 oyuncuya yükleyen takım")
        team_load = self.data.groupby(["Season","Team"]).apply(
            lambda g: g.nlargest(5,"Minutes")["PTS_per_game"].sum() / g["PTS_per_game"].sum()# her takım için en çok dakika oynayan 5 oyuncunun puan toplamını takımın toplam puanına bölüyor
        )
        print(team_load.sort_values(ascending=False).head(10))
        print("\n--------------------------------------------------------------\n")

        # 9) Efficiency outlier (z-score > 3)
        print("9) Efficiency outlier oyuncular")
        mean_eff = self.data["Efficiency"].mean()# efficiency ortalamasını alıyor
        std_eff = self.data["Efficiency"].std()# efficiency standart sapmasını alıyor
        self.data["z_eff"] = (self.data["Efficiency"] - mean_eff) / std_eff# z skorunu hesaplıyor
        outliers = self.data[abs(self.data["z_eff"]) > 3][["Season","Player","Efficiency","z_eff"]]# z skoru 3 ten büyük olanları alıyor
        print(outliers)
        print("\n--------------------------------------------------------------\n")

        # 12) Bir oyuncu için PTS trendi
        print("12) Örnek oyuncu PTS trendi")
        sample_player = self.data["Player"].value_counts().index[0]# en çok sezon oynamış oyuncuyu alıyor
        trend = self.data[self.data["Player"] == sample_player][["Season","PTS_per_game","dk"]]# bu oyuncunun sezon bazında puan ve dakika bilgilerini alıyor
        print("Oyuncu:", sample_player)
        print(trend)

PandasLesson1()
