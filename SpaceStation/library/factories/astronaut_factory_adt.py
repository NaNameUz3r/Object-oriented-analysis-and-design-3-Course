from abc import ABCMeta, abstractmethod
from typing import Optional
from ..station_components.astronaut_adt import BaseAstronaut


class AstronautFactory(metaclass=ABCMeta):

    CREATE_ASTRONAUT_NIL: int = 0
    CREATE_ASTRONAUT_OK: int = 1
    CREATE_ASTRONAUT_ERR: int = 2

    @abstractmethod
    def __init__(self):
        """Initialize the AstronautFactory instance."""

    @abstractmethod
    def create_astronaut(self, name: str, age: int, gender: str) -> Optional[BaseAstronaut]:
        """
        Create a new astronaut.
        Preconditions:
            - name: The name of the astronaut.
            - age: The age of the astronaut.
            - gender: The gender of the astronaut.
            - there is enough space for new astronaut in space station.
        Postcondition:
            - New Astronaut instance created with initial states.
        """

    @abstractmethod
    def get_status(self) -> int:
        """Get the status of the last create_astronaut() call."""
