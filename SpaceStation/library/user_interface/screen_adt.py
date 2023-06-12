from abc import ABCMeta, abstractmethod


class BaseScreen(metaclass=ABCMeta):
    DISPLAY_OK: int = 0
    DISPLAY_ERROR: int = 1

    @abstractmethod
    def display(self) -> None:
        """
        Display the content on the screen.

        Postconditions:
        - The content is displayed on the screen.
        """

    @abstractmethod
    def get_display_status(self) -> int:
        """
        Get the status of the screen.

        Postconditions:
        - The status of the last display() call is returned.
        """

    @abstractmethod
    def reset(self) -> None:
        """
        Reset the screen to its initial state.

        Postconditions:
        - The screen is reset to its initial state.
        """
