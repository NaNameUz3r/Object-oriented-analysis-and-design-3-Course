from abc import ABCMeta, abstractmethod
from typing import Optional, Any


# TODO: Define an ADT for SpaceStationTimestamp
class BaseEvent(metaclass=ABCMeta):
    def __init__(self, timestamp: Any):
        """
        Initialize the BaseEvent.

        Args:
            timestamp (SpaceStationTimestamp): The timestamp of the event.

        Preconditions:
        - timestamp is a valid datetime object.

        Postconditions:
        - BaseEvent is initialized with the specified SpaceStationTimestamp.
        """
        self.timestamp = timestamp

    @abstractmethod
    def get_timestamp(self) -> Any:
        """
        Get the timestamp of the event.

        Returns:
            datetime: The timestamp of the event.

        Postconditions:
        - The timestamp of the event is returned.
        """

    @abstractmethod
    def process(self) -> None:
        """
        Process the event.

        Postconditions:
        - The event is processed.
        """
