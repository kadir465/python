import pandas as pd

class PaandasLesson(object):
    def __init__(self):
        self.data={
            "name":[" ali","veli","ayşe","fatma"],
            "age":[20,30,25,35],
            "city":["istanbul","ankara","izmir","bursa"]
        }
        self.df=pd.DataFrame(self.data, index=[1,2,3,4])
        print(self.df)
        print("-------------------")
        self.line=self.df.head(2)
        print(self.line)
        print("-------------------")
        self.name_age=self.df[["name","age"]]
        print(self.name_age)
        print("-------------------")
        self.average_age=self.df["age"].mean()
        print("Ortalama yaş:",self.average_age)
        print("-------------------")
        self.filtre=self.df[self.df["age"] >27]
        print(self.filtre)

PaandasLesson()

