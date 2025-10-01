# Singleton Pattern
class SingletonMeta(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Logger(metaclass=SingletonMeta):
    def log(self, msg):
        print(f"[LOG]: {msg}")

logger1 = Logger()
logger2 = Logger()
assert logger1 is logger2 
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_factory(animal_type: str) -> Animal:
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()
    raise ValueError("Unknown animal type")

pet = animal_factory("dog")
print(pet.speak())  
