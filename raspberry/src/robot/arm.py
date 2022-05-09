

from .logs import Logs, LogComponent

class Arm(LogComponent):
    """
    A class representing a physical arm controlled by a servo motor.
    """

    def __init__(self, logs: Logs = Logs()) -> None:
        super().__init__(logs)

    def _log(self) -> None:
        pass

    def hide(self) -> None:
        """
        This method hides the arm if it is not hidden.
        """
        self._log()
        pass

    def extend(self) -> None:
        """
        This method extends the arm if it is not extended.
        """
        self._log()
        pass

    def _rotate(self, degrees: int) -> None:
        """
        This method rotates the arm by a certain amount of degrees.
        """
        pass