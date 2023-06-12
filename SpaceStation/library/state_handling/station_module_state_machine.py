from abc import ABCMeta, abstractmethod
from typing import Any, Optional
from ..station_components.station_module_adt import BaseStationModule


class StationModuleStateMachine(metaclass=ABCMeta):
    CHANGE_STATE_NIL: int = 0
    CHANGE_STATE__OK: int = 1
    CHANGE_STATE_ERR: int = 2

    GET_ASTRONAUT_NIL: int = 0
    GET_ASTRONAUT_OK: int = 1
    GET_ASTRONAUT_ERR: int = 2

    @abstractmethod
    def __init__(self, module: Optional['BaseStationModule'] = None):
        """
        Initialize the StationModuleStateMachine.

        Preconditions:
        - If module is provided, it must be an instance of BaseStationModule or its subclass.

        Postconditions:
        - StationModuleStateMachine is initialized with the given module object.
        """
        self._module = module

    # TODO: Describe ATD for StationModule state
    @abstractmethod
    def change_state(self, new_state: Any) -> None:
        """
        Change the state of the module.

        Preconditions:
        - new_state is a valid state and met station requirements.

        Postconditions:
        - The state of the module is changed to the new_state.
        """

    @abstractmethod
    def get_module(self) -> Optional['BaseStationModule']:
        """
        Get the module object.

        Returns:
            Optional[BaseStationModule]: The module object, or None if not set.

        Postconditions:
        - The module object is returned.
        """

    @abstractmethod
    def get_change_state_status(self) -> str:
        """
        Get the current state of the module.

        Returns:
            str: The current state of the module.

        Postconditions:
        - The current state of the module is returned.
        """
