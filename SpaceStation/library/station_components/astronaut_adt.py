from abc import ABCMeta, abstractmethod


class BaseAstronaut(metaclass=ABCMeta):

    # Status codes for methods
    CHANGE_STATE_NIL: int = 0
    CHANGE_STATE_OK: int = 1
    CHANGE_STATE_ERR: int = 2

    MISSION_NIL: int = 0
    MISSION_OK: int = 1
    MISSION_ERR: int = 2

    @abstractmethod
    def __init__(self, name: str, age: int, gender: str):
        """Initialize the Astronaut instance with all initial statuses and state"""

    @abstractmethod
    def change_state(self, new_state: str):
        """
        Change the state of the astronaut.
        Preconditions:
            - new_state: The new state of the astronaut.
        Postconditions:
            - The state of the astronaut has been changed.
        """

    @abstractmethod
    def perform_mission(self):
        """
        Perform a mission, e.g. Dealing with events on station.
        Preconditions:
            - astronaut status is valid for mission (astronaut does not busy, alive, has needed perks)
        Postconditions:
            - The mission has been performed.
        """


    @abstractmethod
    def get_change_state_status(self) -> int:
        """Get the status of the last astronaut change_state() call."""

    @abstractmethod
    def get_state(self) -> object:
        """Get the state of the astronaut."""

