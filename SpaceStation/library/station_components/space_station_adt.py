from abc import ABCMeta, abstractmethod
from typing import Any


class SpaceStation(metaclass=ABCMeta):
    REMOVE_MODULE_NIL: int = 0
    REMOVE_MODULE_OK: int = 1
    REMOVE_MODULE_ERR: int = 2

    GET_MODULE_COUNT_NIL: int = 0
    GET_MODULE_COUNT_OK: int = 1
    GET_MODULE_COUNT_ERR: int = 2

    GET_MODULE_BY_INDEX_NIL: int = 0
    GET_MODULE_BY_INDEX_OK: int = 1
    GET_MODULE_BY_INDEX_ERR: int = 2

    GET_TOTAL_RESOURCE_COUNT_NIL: int = 0
    GET_TOTAL_RESOURCE_COUNT_OK: int = 1
    GET_TOTAL_RESOURCE_COUNT_ERR: int = 2

    @abstractmethod
    def __init__(self, name: str, initial_modules: []):
        """
        Creates a new SpaceStation object.

        Preconditions:
            - name is a non-empty string.

        Postconditions:
            - Creates a new SpaceStation object with the specified name.
            - The initial module components of the space station are added in modules storage of SpaceStation object.
        """
        pass

    @abstractmethod
    def add_module(self, module: object):
        """
        Adds a module to the space station.

        Preconditions:
            - module is an instance of the StationModule class.
            - module does not exist in SpaceStation
            - resource and technology requirements for module creation are met

        Postconditions:
            - The specified module is added to the space station.
        """
        pass

    @abstractmethod
    def remove_module(self, module: object):
        """
        Removes a module from the space station.

        Preconditions:
            - module is an instance of the StationModule class.
            - The specified module is currently attached to the space station.

        Postconditions:
            - The specified module is removed from the space station.
        """
        pass

    @abstractmethod
    def get_module_count(self) -> int:
        """
        Returns the number of library in the space station.

        Postconditions:
            - Returns the total count of library in the space station.
        """
        pass

    @abstractmethod
    def get_module_by_index(self, index: int) -> Any:
        """
        Returns the module at the specified index.

        Preconditions:
            - index is a valid index within the range of library.

        Postconditions:
            - Returns the module at the specified index.
        """
        pass

    @abstractmethod
    def get_total_resource_count(self, resource_type: str) -> int:
        """
        Returns the total count of a specific resource type in all library.

        Preconditions:
            - resource_type is a valid resource type string.

        Postconditions:
            - Returns the total count of the specified resource type across all library.
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """Get the number of modules in the SpaceStation."""

    @abstractmethod
    def is_empty(self) -> bool:
        """Check if the SpaceStation is empty."""

    @abstractmethod
    def clear(self):
        """Remove all modules from the SpaceStation."""

    @abstractmethod
    def get_add_module_status(self) -> int:
        """Get the status of the last add_module() call."""

    @abstractmethod
    def get_remove_module_status(self) -> int:
        """Get the status of the last remove_module() call."""

    @abstractmethod
    def get_get_module_status(self) -> int:
        """Get the status of the last get_module() call."""
