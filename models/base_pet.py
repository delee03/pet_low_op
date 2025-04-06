from abc import ABC, abstractmethod
from .owner import Owner

class BasePet(ABC):
    def __init__(self, name: str, age : int , owner: Owner):
        self._name = name
        self._age = age
        self._owner = owner

    @abstractmethod
    def speak(self):
        pass
    
    
    def get_info(self):
        # return f"{self._name} ({self.__class__.__name__}), {self._age} years old - Owner: {self._owner._Owner__name}" Trick -- Don't need @property to get private prop like Name
        return f"{self._name} ({self.__class__.__name__}), {self._age} years old - Owner: {self._owner.name}" #Must have @property to get private property like name 
