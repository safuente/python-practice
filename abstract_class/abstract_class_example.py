from abc import ABC, abstractmethod


# An abstract class in Python is a blueprint for other classes.
# It cannot be instantiated directly, and
# it defines methods that must be implemented by any subclass.
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def move(self):
        return "Runs on four legs"


class Bird(Animal):
    def make_sound(self):
        return "Tweet!"

    def move(self):
        return "Flies in the sky"
