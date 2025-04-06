import unittest
from models.owner import Owner
from models.dog import Dog
from models.cat import Cat
from models.parrot import Parrot

class TestPets(unittest.TestCase):
    def setUp(self):
        self.owner = Owner("Test Owner", "000", "Test City")

    def test_dog(self):
        dog = Dog("Buddy", 2, self.owner)
        self.assertEqual(dog.speak(), "Gâu gâu!")

    def test_cat(self):
        cat = Cat("Kitty", 3, self.owner)
        self.assertEqual(cat.speak(), "Meo meo~")

    def test_parrot(self):
        parrot = Parrot("Polly", 1, self.owner)
        self.assertEqual(parrot.speak(), "Meo meo~")
