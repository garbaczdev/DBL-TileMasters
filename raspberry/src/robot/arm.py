

from .logs import Logs, LogComponent

class Arm(LogComponent):
    """
    A class representing a physical arm controlled by a servo motor.
    """


    @property
    def COMPONENT_NAME(self) -> str:
        return "Arm"

    def hide(self, log: bool = True) -> None:
        """
        This method hides the arm if it is not hidden.
        """

        # If should log
        if log:
            self._log_action("Hide called")

        # Physically hide the arm
        self._hide_motor()


    def extend(self, log: bool = True) -> None:
        """
        This method extends the arm if it is not extended.
        """

        # If should log
        if log:
            self._log_action("Extend called")

        # Physically extend the arm
        self._extend_motor()

    
    def _hide_motor(self) -> None:
        """
        This physically moves the motor such that the arm is hidden.
        """
        pass

    def _extend_motor(self) -> None:
        """
        This physically moves the motor such that the arm is extended.
        """
        pass

    def _rotate(self, degrees: int) -> None:
        """
        This method rotates the arm by a certain amount of degrees.
        """
        pass


class TestingArm(Arm):
    """
    This class has the functionality of Arm but does not implement actual physical behavior.
    It can be used for the ARTIFICIAL_ENVIRONMENT_TESTING mode.
    """
    @property
    def COMPONENT_NAME(self) -> str:
        return "TestingArm"

    def _hide_motor(self) -> None:
        pass

    def _extend_motor(self) -> None:
        pass

    def _rotate(self, degrees: int) -> None:
        pass
