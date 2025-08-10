class Monster :
    color = "Black"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sound(self):
        print("Grrrr")
    def __move(self): #the leading uderscore indicates this method is private
        print(self.name + "is moving")

Monster1 = Monster("Dracula",50)
Monster1.sound()

print(Monster1.name)
print(Monster1.age)