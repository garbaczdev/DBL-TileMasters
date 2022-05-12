

from .logs import Logs, LogComponent

class Arm(LogComponent):
    """
    A class representing a physical arm controlled by a servo motor.
    """

    def __init__(self, logs: Logs = Logs()) -> None:
        super().__init__(logs)

        # Variable indicating whether the arm is extended or not.
        self.extended = True
        # Hide the arm.
        self.hide(log=False)

    @property
    def COMPONENT_NAME(self) -> str:
        return "Arm"

    def hide(self, log: bool = True) -> None:
        """
        This method hides the arm if it is not hidden.
        """

        # If it is already extended
        if not self.extended:
            return

        # If should log
        if log:
            self._log_action("Hide called")

        # Physically hide the arm
        self._hide_motor()

        # Set variable indicating that the arm is hidden
        self.exteded = False


    def extend(self, log: bool = True) -> None:
        """
        This method extends the arm if it is not extended.
        """

        # If it is already extended
        if self.extended:
            return
        
        # If should log
        if log:
            self._log_action("Extend called")

        # Physically extend the arm
        self._extend_motor()

        # Set variable indicating that the arm is extended
        self.exteded = True

    
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
    def _hide_motor(self) -> None:
        pass

    def _extend_motor(self) -> None:
        pass

    def _rotate(self, degrees: int) -> None:
        pass
