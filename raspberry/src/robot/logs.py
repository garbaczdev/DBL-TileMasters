from abc import ABC, abstractmethod

class Logs:
    pass


class Log:
    pass


class LogComponent(ABC):

    def __init__(self, logs: Logs) -> None:
        self._logs = logs

    @property
    def logs(self) -> Logs:
        return self._logs

    @abstractmethod
    def _log(self, *args) -> None:
        pass