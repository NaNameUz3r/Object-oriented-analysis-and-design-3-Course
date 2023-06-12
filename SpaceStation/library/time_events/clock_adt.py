from abc import ABCMeta, abstractmethod


class Clock(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, hours: int, minutes: int, seconds: int):
        """
        Initialize the Clock object.

        Args:
            hours (int): The hours component of the time.
            minutes (int): The minutes component of the time.
            seconds (int): The seconds component of the time.

        Preconditions:
        - hours is a non-negative integer.
        - minutes is an integer between 0 and 59.
        - seconds is an integer between 0 and 59.

        Postconditions:
        - A StationTime object is initialized with the specified hours, minutes, and seconds.
        """

    @abstractmethod
    def start_ticking(self) -> None:
        """
        Start the time ticker loop.

        Postconditions:
        - The time ticker loop is started and the time on the station is continuously updated.
        """

    @abstractmethod
    def stop_ticking(self) -> None:
        """
        Stop the time ticker

        Precondition:
        - The time ticker is active.

        Postconditions:
        - The time ticker loop is stopped and the time on the station is freezed.
        """

    @abstractmethod
    def advance_time(self, hours: int, minutes: int, seconds: int) -> None:
        """
        Advance the time on the station.

        Args:
            hours (int): The number of hours to advance.
            minutes (int): The number of minutes to advance.
            seconds (int): The number of seconds to advance.

        Preconditions:
        - hours is a non-negative integer.
        - minutes is an integer between 0 and 59.
        - seconds is an integer between 0 and 59.

        Postconditions:
        - The time on the station is advanced by the specified hours, minutes, and seconds.
        """

    @abstractmethod
    def revert_time(self, hours: int, minutes: int, seconds: int) -> None:
        """
        Revert the time on the station to a previous state.

        Args:
            hours (int): The number of hours to revert.
            minutes (int): The number of minutes to revert.
            seconds (int): The number of seconds to revert.

        Preconditions:
        - hours is a non-negative integer.
        - minutes is an integer between 0 and 59.
        - seconds is an integer between 0 and 59.

        Postconditions:
        - The time on the station is reverted to the previous state by the specified hours, minutes, and seconds.
        """


    @abstractmethod
    def get_hours(self) -> int:
        """
        Get the hours component of the time.

        Returns:
            int: The hours component of the time.

        Postconditions:
        - The hours component of the time is returned.
        """

    @abstractmethod
    def get_minutes(self) -> int:
        """
        Get the minutes component of the time.

        Returns:
            int: The minutes component of the time.

        Postconditions:
        - The minutes component of the time is returned.
        """

    @abstractmethod
    def get_seconds(self) -> int:
        """
        Get the seconds component of the time.

        Returns:
            int: The seconds component of the time.

        Postconditions:
        - The seconds component of the time is returned.
        """

    @abstractmethod
    def __str__(self) -> str:
        """
        Get a string representation of the time.

        Returns:
            str: The string representation of the time.

        Postconditions:
        - The string representation of the time is returned.
        """
