

class Arm:
    """
    A class representing a physical arm controlled by a servo motor.
    """

    def hide(self) -> None:
        """
        This method hides the arm if it is not hidden.
        """
        print("Arm: Hidden")
        pass

    def extend(self) -> None:
        """
        This method extends the arm if it is not extended.
        """
        print("Arm: Extended")
        pass

    def _rotate(self, degrees: int) -> None:
        """
        This method rotates the arm by a certain amount of degrees.
        """
        pass