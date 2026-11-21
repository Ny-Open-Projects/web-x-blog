from typing import Generic, TypeVar, Protocol

class Animal:
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "woof"

T_co = TypeVar("T_co", covariant=True)               # 协变:只出不进
T_contra = TypeVar("T_contra", contravariant=True)   # 逆变:只进不出

class Shelter(Generic[T_co]):
    def __init__(self, animal: T_co) -> None:
        self.animal = animal

    def adopt(self) -> T_co:
        return self.animal

class Feeder(Protocol[T_contra]):
    def feed(self, animal: T_contra) -> None:
        """协议方法:能喂更宽的类型,就能喂更窄的类型"""

class AnimalFeeder:
    def feed(self, animal: Animal) -> None:
        print("fed", animal.speak())

if __name__ == "__main__":
    dog_shelter: Shelter[Dog] = Shelter(Dog())
    wider: Shelter[Animal] = dog_shelter   # 协变:Dog 容器可当 Animal 容器读
    print(wider.adopt().speak())

    feeder: Feeder[Dog] = AnimalFeeder()   # 逆变:能喂 Animal 就能喂 Dog
    feeder.feed(Dog())
