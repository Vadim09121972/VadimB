class Animal:
    alive = True    
    fed = False     
    def __init__(self, name):
        self.name = name

class Plant:
    edible = False  
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
            
class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Flower(Plant):
    pass
edible = True

class Fruit(Plant):
    edible = True


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