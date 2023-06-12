from abc import ABCMeta, abstractmethod
from typing import Any
from typing import Optional
from ..station_components.station_module_adt import BaseStationModule


class StationModuleFactory(metaclass=ABCMeta):
    CREATE_MODULE_NIL: int = 0
    CREATE_MODULE_OK: int = 1
    CREATE_MODULE_ERR: int = 2


    # TODO: Define atd from module_spec
    @abstractmethod
    def create_module(self, module_spec: Any) -> Optional[BaseStationModule]:
        """
        Create a station module of given spec

        Preconditions:
        - module spec is valid spec, and all creation req. are met (resources, technologies, etc)

        Postconditions:
        - module of provided module_spec has been created.
        """
        pass

    @abstractmethod
    def get_status(self) -> int:
        """
        Get the status code of the create_module() command.

        Postconditions:
        - Returns CREATE_MODULE_* status
        """
        pass
