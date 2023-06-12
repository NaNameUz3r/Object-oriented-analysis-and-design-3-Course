from abc import ABCMeta, abstractmethod
from typing import Optional, Any
from ..station_components.astronaut_adt import BaseAstronaut


class AstronautStateMachine(metaclass=ABCMeta):
    CHANGE_STATE_NIL: int = 0
    CHANGE_STATE__OK: int = 1
    CHANGE_STATE_ERR: int = 2

    GET_ASTRONAUT_NIL: int = 0
    GET_ASTRONAUT_OK: int = 1
    GET_ASTRONAUT_ERR: int = 2

    @abstractmethod
    def __init__(self, astronaut: Optional['BaseAstronaut'] = None):
        """
        Initialize the AstronautStateMachine.

        Preconditions:
        - If astronaut is provided, it must be an instance of BaseAstronaut or its subclass.

        Postconditions:
        - AstronautStateMachine is initialized with the given astronaut object.
        """
        self._astronaut = astronaut

    # TODO: Describe ATD for astronaut state
    @abstractmethod
    def change_state(self, new_state: Any) -> None:
        """
        Change the state of the astronaut.

        Preconditions:
        - new_state is a valid state (one of STATE_READY, STATE_BUSY, STATE_RESTING).

        Postconditions:
        - The state of the astronaut is changed to the new_state.
        """

    @abstractmethod
    def get_astronaut(self) -> Optional['BaseAstronaut']:
        """
        Get the astronaut object.

        Postconditions:
        - The astronaut object is returned.
        """
        return self._astronaut

    @abstractmethod
    def get_change_state_status(self) -> str:
        """
        Get the current state of the astronaut.

        Returns:
            str: The current state of the astronaut.

        Postconditions:
        - The current state of the astronaut is returned.
        """