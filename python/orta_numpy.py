import numpy as np

class LessonNumpy(object):
    def __init__(self):
        self.array0=np.random.randint(0,50,10)#0-50 arası 10 tane rastgele sayı üretir
        print(self.array0)
        print("------------------------")
        self.array1=np.arange(0,100,2)#0 dan 100 e kadar 2 şer 2 şer artan dizi
        print(self.array1)
        print("\n")
        print("------------------------")
        self.array2 = np.random.randint(25, size=(5,5))#25 elemanlı 5x5 lik bir matris oluşturur ve random elemanlar atar
        self.array2[np.arange(5), np.arange(5)] = 1#köşe elemanlarına 1 atar
        print(self.array2)
        print("------------------------")
        self.array3=np.array([1,2,3,4,5,])
        for i in self.array3:
            self.array3[i-1]=self.array3[i-1]**2#elemanların karesini alır
        print(self.array3)
        print("------------------------")
        array4=np.array([1,2,3,4,5])
        print(array4.sum())#elemanların toplamını verir
        print("------------------------")
        array5=(np.random.randn(10)*100).astype(int)#-100 ile 100 arasında 10 tane rastgele sayı üretir int e çevrildi
        en_buyuk=array5.max()#dizinin en büyük elemanını verir
        en_kucuk=array5.min()#dizinin en küçük elemanını verir
        print(array5,en_buyuk,en_kucuk)
        print("------------------------")
        array6=(np.random.randn(6)*100).astype(int)
        array7=(np.random.randn(6)*100).astype(int)#-100 ile 100 arasında 6 tane rastgele sayı üretir int e çevrildi
        print(array6)
        print(array7)
        print(array6*array7)#iki dizinin elemanlarını çarpar aynı indeksteki elemanlar çarpılır
        print("------------------------")
        array8=(np.random.rand(4,4)*10).astype(int)#4x4 lük matris oluşturur ve 0-10 arası rastgele sayılar atar
        print(array8)
        print(array8.transpose())#dizinin matrisin transpozunu alır
        print("------------------------")
        array9=(np.random.randn(5,5)*10).astype(int)#5x5 lük matris oluşturur ve -10 ile 10 arasında rastgele sayılar atar
        sum=array9[np.arange(5), np.arange(5)].sum()#köşe elemanlarının toplamını verir
        print(array9)
        print(sum)
        print("------------------------")
        array10=np.array([1,2,0,0,4,0])
        
        for i in range(len(array10)):
            if array10[i]!=0:
                print(array10[i])#dizinin sıfır olmayan elemanlarını yazdırır

LessonNumpy()
