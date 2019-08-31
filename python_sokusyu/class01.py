# class01.py

# Personクラスの定義
class Person:
    def __init__(self):                  
        self.name = ""

    def getName(self):                   
        return self.name

    def setName(self, name):             
        self.name = name


#インスタンスの生成と実行
p = Person()
p.setName("Taro")
person_name = p.getName()
print(person_name)
