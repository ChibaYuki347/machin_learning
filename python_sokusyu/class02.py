# class02.py

# Personクラスの定義
class Person:
    def __init__(self):                  
        self.name = ""

    def getName(self):                   
        return self.name

    def setName(self, name):             
        self.name = name


#インスタンスの生成と実行
p1 = Person()
p2 = Person()
p1.setName("Tom")
p2.setName("Bob")
print(p1.getName())
print(p2.getName())


