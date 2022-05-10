from datetime import datetime
from abc import ABC, abstractmethod


from .config import Config as config

LOG_COUNTER = 0


class Log:
    def __init__(self, component_name: str, _type: str, description: str, time: datetime) -> None:
        self.id = self.get_id()
        self.component_name = component_name
        self.type = _type
        self.description = description
        self.time = time

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