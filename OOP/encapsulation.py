class Warrior :
    def __init__(self,name):
        self.name = name
        self._age = 0 #private attribute denoted by private attribute by convention

    #using a property decorator - getter function
    #setters and getters are defined using decorators
    #can add validation methods using setters and getters
    @property
    def age(self): #getter is defined with the same name as the private attribute without the leading underscore
        return self._age
    
    @age.setter #using a setter function @private_attribute.setter //the decorator
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Age must be greater than 0")

warrior1 = Warrior("Spider man")
warrior1.age = 25 #note that these getters and setter methods can be accessed without using paranthesis
print(warrior1.age)
