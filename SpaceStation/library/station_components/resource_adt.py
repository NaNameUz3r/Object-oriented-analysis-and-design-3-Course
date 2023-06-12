from abc import ABCMeta, abstractmethod


class BaseResource(metaclass=ABCMeta):

    USE_RESOURCE_NIL: int = 0
    USE_RESOURCE_OK: int = 1
    USE_RESOURCE_ERR: int = 2

    REFILL_RESOURCE_NIL: int = 0
    REFILL_RESOURCE_OK: int = 1
    REFILL_RESOURCE_ERR: int = 2


    @abstractmethod
    def __init__(self):
        """Initialize the Resource instance."""

    @abstractmethod
    def use_resource(self):
        """
        Use the resource.
        Postconditions:
            - The resource has been used.
        """

    @abstractmethod
    def refill(self):
        """
        Refill the resource.
        Postconditions:
            - The resource has been refilled.
        """

    @abstractmethod
    def get_use_status(self) -> int:
        """Get the status of the last use_resource() call."""

    @abstractmethod
    def get_refill_status(self) -> int:
        """Get the status of the last use_resource() call."""
