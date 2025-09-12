import numpy as np

class LessonNumpy(object):
    def __init__(self):
        self.arry0=np.array([1,2,3,4,5,6,7,8,9])#dizi oluşturuldu numpy kullanılarak
        print(self.arry0)
        print("------------------------")
        self.arry1=np.random.randint(0,10,10)#0-10 arası 10 tane rastgele sayı üretir
        print(self.arry1)
        print("------------------------")
        self.arry2=np.zeros(10)#10 tane 0 lardan oluşan dizi
        print(self.arry2)
        print("------------------------")
        self.arry3=np.ones(5)#5 tane 1 lerden oluşan dizi
        print(self.arry3)
        print("------------------------")
        self.arry4=np.arange(1,20,2)#1 den 20 ye kadar 2 şer 2 şer artan dizi
        print(self.arry4)
        print("------------------------")
        self.arry5=np.array([10,20,30,40,50]).mean()#dizinin ortalamasını verir
        print(self.arry5)
        print("------------------------")
        self.arry6=np.array([5,15,25,35,45]).std()#dizinin standart sapmasını verir
        print(self.arry6)
        print("------------------------")
        self.arry7=np.array([2,4,6,8])
        self.arry8=np.array([1,3,5,7])
        print(self.arry7+self.arry8)#iki dizinin elemanlarını toplar
        print("------------------------")
        self.arry9=np.zeros((3,3))#3x3 lük matris oluşturu ve tüm elemanlara 0 atar
        print(self.arry9)
        print("------------------------")
        self.arry10=np.ones((3,3))#3x3 lük matris oluşturu ve tüm elemanlara 1 atar
        print(self.arry10)


l=LessonNumpy()
