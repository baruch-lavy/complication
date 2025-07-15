class myClass:
    def __init__(self,num,name) -> None:
        self.number = num
        self.name = name

object1 = myClass(5,'effi')
# object2 = myClass(6)
# print(object1.number,object1.name)
# print(object1)

class Animal:
    def __init__(self,name,age,children) -> None:
        self.name = name
        self.age = age
        self.children = children

    def add_tail(self,color,lenght):
        self.tail = Tail(color,lenght)
        
class Tail:
    def __init__(self,color,length) -> None:
        self.color = color
        self.lenght = length

class Cat(Animal):
    def __init__(self, name, age, children,color) -> None:
        super().__init__(name, age, children)
        self.color = color
    
    def get_hunted_mice(self):
        return self.hanted

    def hunt_mouse(self,num_of_mice):
        self.hanted = num_of_mice
        
    

cat1 = Cat('bobi',5,2,'black')
cat1.add_tail('white',5)
cat1.hunt_mouse(15)
print(cat1.get_hunted_mice())


