class Person:
    def __init__(self,title="default title"):
        self.name = None
        self.title = title

    def talk(self,words):
        print("talk1")

    def talk(self,words) :
        print("talk2")

class Employee(Person):
    # def __init__(self,id,title):
    #     super().__init__()
    #     self.id = id
    pass


person1 = Person()
person1.talk("Hello")