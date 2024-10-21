class Animal:
    def __init__(self, name):
        self.alive = True    
        self.fed = False     
        self.name = name
    
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
            
class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name
    
class Mammal(Animal):
    pass
                
class Predator(Animal):
    pass
   
class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        self.edible = True
        self.name = name
      
animal1 = Predator('Лев')
animal2 = Mammal('Заяц')
plant1 = Plant('Борщевик')
plant2 = Fruit('Мандарин')

print(animal1.name)
print(plant1.name)

print(animal1.alive)
print(animal2.fed)

animal1.eat(plant1)
animal2.eat(plant2)
print(animal1.alive)
print(animal2.fed)