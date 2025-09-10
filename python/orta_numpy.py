import numpy as np

class LessonNumpy(object):
    def __init__(self):
        self.array0=np.random.randint(0,50,10)
        print(self.array0)
        print("------------------------")
        self.array1=np.arange(0,100,2)
        print(self.array1)
        print("\n")
        print("------------------------")
        self.array2 = np.random.randint(25, size=(5,5))
        self.array2[np.arange(5), np.arange(5)] = 1
        print(self.array2)
        print("------------------------")
        self.array3=np.array([1,2,3,4,5,])
        for i in self.array3:
            self.array3[i-1]=self.array3[i-1]**2
        print(self.array3)
        print("------------------------")
        array4=np.array([1,2,3,4,5])
        print(array4.sum())
        print("------------------------")
        array5=(np.random.randn(10)*100).astype(int)
        en_buyuk=array5.max()
        en_kucuk=array5.min()
        print(array5,en_buyuk,en_kucuk)
        print("------------------------")
        array6=(np.random.randn(6)*100).astype(int)
        array7=(np.random.randn(6)*100).astype(int)
        print(array6)
        print(array7)
        print(array6*array7)
        print("------------------------")
        array8=(np.random.rand(4,4)*10).astype(int)
        print(array8)
        print(array8.transpose())
        print("------------------------")
        array9=(np.random.randn(5,5)*10).astype(int)
        sum=array9[np.arange(5), np.arange(5)].sum()
        print(array9)
        print(sum)
        print("------------------------")
        array10=np.array([1,2,0,0,4,0])
        
        for i in range(len(array10)):
            if array10[i]!=0:
                print(array10[i])

LessonNumpy()