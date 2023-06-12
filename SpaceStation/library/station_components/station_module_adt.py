from abc import ABCMeta, abstractmethod
from typing import Any


class BaseStationModule(metaclass=ABCMeta):
    GET_STATE_NIL: int = 0
    GET_STATUS_OK: int = 1
    GET_STATUS_ERR: int = 2

    INSERT_EVENT_NIL: int = 0
    INSERT_EVENT_OK: int = 1
    INSERT_EVENT_ERR: int = 2

    DELETE_NIL: int = 0
    DELETE_OK: int = 1
    DELETE_ERR: int = 2

    @abstractmethod
    def __init__(self, name: str):
        """
        Creates a new StationModule object.

        Preconditions:
            - name is a non-empty string.

        Postconditions:
            - Creates a new StationModule object with the specified name.
            - The module components of the space station are uninitialized.
        """

    @abstractmethod
    def get_state(self):
        """
        Get the current state of the StationModule.
        Postconditions:
            - The state object of station module returned.
        """

    @abstractmethod
    def insert_event(self, event: Any):
        """
        Insert an item into the StationModule.
        Preconditions:
            - The item is not None.
        Postconditions:
            - The item has been inserted into the StationModule.
        """

    @abstractmethod
    def delete_event(self, event: Any):
        """
        Delete an item from the StationModule.
        Preconditions:
            - The item is not None.
        Postconditions:
            - The item has been deleted from the StationModule if it exists.
        """

    @abstractmethod
    def change_state(self, new_state: str):
        """
        Change the state of the station module.
        Preconditions:
            - new_state: The new state of the station module is valid state.
        Postconditions:
            - The state of the station module has been changed.
        """

    @abstractmethod
    def __len__(self) -> int:
        """Get the number of active events in the StationModule."""

    @abstractmethod
    def is_empty(self) -> bool:
        """Check if the StationModule has no events."""

    @abstractmethod
    def clear(self):
        """Remove all events from the StationModule."""

    @abstractmethod
    def get_insert_event_status(self) -> int:
        """Get the status of the last insert() call."""

    @abstractmethod
    def get_delete_event_status(self) -> int:
        """Get the status of the last delete() call."""

    @abstractmethod
    def get_get_state_status(self) -> int:
        """Get the status of the last get_item() call."""
