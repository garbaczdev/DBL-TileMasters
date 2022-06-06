from typing import Union
from time import sleep
from threading import Thread

from .logs import Logs, LogComponent
from .config import Config as config


class Arm(LogComponent):
    """
    A class representing a physical arm controlled by a servo motor.
    """

    def __init__(self, gpio_pin: Union[int, None], logs: Logs = Logs()) -> None:
        super().__init__(logs)
        self.gpio_pin = gpio_pin
        self._servo = None

        if gpio_pin is not None:
            import RPi.GPIO as GPIO

            # Set GPIO numbering mode
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self.gpio_pin, GPIO.OUT)
            GPIO.setwarnings(False)

            self._servo = GPIO.PWM(self.gpio_pin, 50) # pin 11 for servo1, pulse 50Hz

            # Start PWM running, with value of 0 (pulse off)
            self._servo.start(0)

        self.is_pushing = False

    @property
    def COMPONENT_NAME(self) -> str:
        return "Arm"

    def push(self, tile: Union[int, None] = None, log: bool = True) -> None:
        """
        This method hides the arm if it is not hidden.
        """

        if self.is_pushing:
            return 

        # If should log
        if log:
            if tile is not None:
                tile_color = config.TILE_COLOR_DICT.get(tile)
                self.add_log("pushed", f"Pushed {tile_color} Tile")
                
            else:
                self.add_log("pushed", "Push called")

        self.is_pushing = True

        if self.gpio_pin is None:
            push_thread = Thread(target = self._testing_push_thread)
        else:
            push_thread = Thread(target = self._push_thread)
        
        push_thread.start()


    
    def _push_thread(self) -> None:
        """
        This physically extends and hides the motor
        """
        self._servo.ChangeDutyCycle(9)
        sleep(config.ARM_PUSH_TIMEOUT)
        self._servo.ChangeDutyCycle(4)
        self.is_pushing = False


    def _testing_push_thread(self) -> None:
        """
        This is a testing function that just waits.
        """
        sleep(config.ARM_PUSH_TIMEOUT)
        self.is_pushing = False


class TestingArm(Arm):
    """
    This class has the functionality of Arm but does not implement actual physical behavior.
    It can be used for the ARTIFICIAL_ENVIRONMENT_TESTING mode.
    """

    def __init__(self, gpio_pin: int = None, logs: Logs = Logs()) -> None:
        super().__init__(gpio_pin, logs)
        # Variable used for determining whether the arm has been pushed since the last time checked.
        self._has_pushed = False
    
    @property
    def COMPONENT_NAME(self) -> str:
        return "TestingArm"

    def push(self, tile: int) -> None:
        super().push(tile)
        self._has_pushed = True

    def has_pushed(self) -> bool:
        """
        Returns whether the arm has pushed the tile since the last time checked.
        """
        # If has_pushed is True, reset it to False.
        if self._has_pushed:
            # Set has_pushed info to false
            self._has_pushed = False
            return True

        return False


    def _hide_motor(self) -> None:
        # Do nothing
        pass

    def _extend_motor(self) -> None:
        # Do nothing
        pass

    def _rotate(self, degrees: int) -> None:
        # Do nothing
        pass
