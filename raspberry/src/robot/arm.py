

from .logs import Logs, LogComponent

class Arm(LogComponent):
    """
    A class representing a physical arm controlled by a servo motor.
    """


    @property
    def COMPONENT_NAME(self) -> str:
        return "Arm"

    def push(self, log: bool = True) -> None:
        """
        This method hides the arm if it is not hidden.
        """

        # If should log
        if log:
            self._log_action("Push called")

        # Physically hide the arm
        self._extend_motor()
        self._hide_motor()
    
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

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Variable used for determining whether the arm has been pushed since the last time checked.
        self._has_pushed = False
    
    @property
    def COMPONENT_NAME(self) -> str:
        return "TestingArm"

    def push(self) -> None:
        super().push()
        self._has_pushed = True

    def has_pushed(self) -> bool:
        """
        Returns whether the arm has pushed the tile since the last time checked.
        """
        # Save the has_pushed info
        has_pushed = self._has_pushed
        # Set has_pushed info to false
        self._has_pushed = False
        # Return the initial has_pushed info
        return has_pushed

    def _hide_motor(self) -> None:
        # Do nothing
        pass

    def _extend_motor(self) -> None:
        # Do nothing
        pass

    def _rotate(self, degrees: int) -> None:
        # Do nothing
        pass
