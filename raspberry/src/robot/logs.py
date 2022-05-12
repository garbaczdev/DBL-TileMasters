from datetime import datetime
from abc import ABC, abstractmethod


from .config import Config as config
from .utils import Utils as utils


# This is used for a log id. It is increased by 1 every time the Log class is made.
LOG_COUNTER = 0


class Log:
    """
    A class representing a log object.
    """
    def __init__(self, component_name: str, _type: str, description: str, time: datetime, additional_data: dict = dict()) -> None:
        # Id of the log
        self.id = self._get_id()
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
        """
        This returns the string representation of an object.
        """
        # Its in the utils.py!
        return utils.get_log_format_str(self.id, self.get_date_as_str(), self.component_name, self.description)

    def get_date_as_str(self) -> str:
        """
        Returns the log date as a string.
        """
        return datetime.strftime(self.time, config.LOG_DATETIME_STR)[:config.LOG_TIME_SPACE]

    @classmethod
    def _get_id(cls) -> None:
        """
        Returns the id of the log. Everytime this method is called it increases the counter by 1.
        """
        global LOG_COUNTER

        id = LOG_COUNTER
        LOG_COUNTER += 1
        
        return id


class Logs:
    """
    Logs representation, which holds the info about actions and errors that occured in components.
    """

    def __init__(self) -> None:
        # List of logs.
        self._logs: list[Log] = list()
        # This is used so that the header is printed the first time a log is printed.
        self.header_printed = False

    def print(self, amount: int = 0) -> None:
        """
        Prints the logs. If given the amount, it will print last amount of logs.
        If amount is 0, it will print all of the logs.
        """
        self.print_header()
        for log in self._logs[-amount:]:
            print(log)

    def print_header(self) -> None:
        """
        Prints the log header.
        """
        header = utils.get_log_format_str("ID", "HH:MM:SS:mmm", "COMPONENT_NAME", "DESCRIPTION")
        print(header)

    def add(self, log: Log) -> None:
        """
        Adds a given log to the internal logs.
        """
        # If the logs should be used:
        if config.USE_LOGS:

            # Add the log to the internal logs
            self._logs.append(log)

            # If the logs should be printed
            if config.PRINT_LOGS:
                if not self.header_printed:
                    self.print_header()
                    self.header_printed = True
                # Print the logs.
                print(log)

    def add_multiple(self, logs: list[Log]) -> None:
        """
        Add multiple logs to the internal logs.
        """
        for log in logs:
            self.add_log(log)


class LogComponent(ABC):
    """
    Abstract class for a component that can log its actions.
    """

    def __init__(self, logs: Logs) -> None:
        self.logs = logs

    @property
    @abstractmethod
    def COMPONENT_NAME(self) -> str:
        """
        This should return the component name.
        """
        pass

    def _log_action(self, description: str) -> None:
        """
        Saves the log of type "action" with the given description and current time.
        """
        self._add_log("action", description)

    def _log_error(self, description: str) -> None:
        """
        Saves the log of type "error" with the given description and current time.
        """
        self._add_log("error", description)

    def _add_log(self, _type: str, description: str) -> None:
        """
        Saves the log of given type, description and current time.
        """
        # Create a log object.
        log = Log(
            self.COMPONENT_NAME,
            _type,
            description,
            datetime.now()
        )
        # Save the log object.
        self.logs.add(log)