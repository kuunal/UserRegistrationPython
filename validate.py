from abc import ABC, abstractmethod

class Validate(ABC):

    @abstractmethod
    def validate_input(self, user_input):
        pass