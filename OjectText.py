class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self,song):
        # print("%s正在唱 %s"%(self.name, song))
        print(f'{self.name}正在唱{song}')
p = Person('小明', 20)
p.sing('朋友')
