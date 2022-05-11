from datetime import datetime
from abc import ABC, abstractmethod


from .config import Config as config


# This is used for a log id. It is incremented every time the Log class is made.
LOG_COUNTER = 0


class Log:
    """
    A class representing a log object.
    """
    def __init__(self, component_name: str, _type: str, description: str, time: datetime, additional_data: dict = dict()) -> None:
        # Id of the log
        self.id = self.get_id()
        # Name of the component that created that log
        self.component_name = component_name
        # Type of the log: for now it can be either "error" or "action"
        self.type = _type
        # Description of the log
        self.description = description
        # Time of the log
        self.time = time
        # Additional data
        self.additional_data = additional_data

    def __str__(self) -> str:
        return f'[{self.id}]: ({self.get_date_as_str()}) [{self.component_name}]: {self.description}'
    
    def get_date_as_str(self) -> str:
        return datetime.strftime(self.time, config.LOG_DATETIME_STR)

    @classmethod
    def get_id(cls) -> None:
        global LOG_COUNTER

        id = LOG_COUNTER
        LOG_COUNTER += 1
        
        return id


class Logs:

    def __init__(self) -> None:
        self._logs: list[Log] = list()

    def print(self, amount: int = 0) -> None:
        for log in self._logs[-amount:]:
            print(log)

    def add(self, log: Log) -> None:
        if config.USE_LOGS:
            self._logs.append(log)

            if config.PRINT_LOGS:
                print(log)

    def add_multiple(self, logs: list[Log]) -> None:
        for log in logs:
            self.add_log(log)


class LogComponent(ABC):

    def __init__(self, logs: Logs) -> None:
        self.logs = logs

    @property
    @abstractmethod
    def COMPONENT_NAME(self) -> str:
        pass

    def _log_action(self, description: str) -> None:
        self._add_log("action", description)

    def _log_error(self, description: str) -> None:
        self._add_log("error", description)

    def _add_log(self, _type: str, description: str) -> None:
        log = Log(
            self.COMPONENT_NAME,
            _type,
            description,
            datetime.now()
        )

        self.logs.add(log)