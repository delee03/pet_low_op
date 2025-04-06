from models.owner import Owner
from models.dog import Dog
from models.cat import Cat
from models.parrot import Parrot

def main():
    owner1 = Owner("Alice", "0123456789", "Hà Nội")
    owner2 = Owner("Bob", "0987654321", "Sài Gòn")

    # print(owner1._Owner__name)
    pets = [
        Dog("Milo", 2, owner1),
        Cat("Tom", 3, owner2),
        Parrot("Polly", 1, owner1)
    ]

    for pet in pets:
        print(pet.get_info())
        print("Pet says:", pet.speak())
        print("----")

if __name__ == "__main__":
    main()
