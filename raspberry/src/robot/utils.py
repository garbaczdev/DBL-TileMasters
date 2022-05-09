
from datetime import datetime, timedelta

class Utils:
    @staticmethod
    def get_time_after_ms(milliseconds: int) -> datetime:
        """
        Return the datetime object of the time after the given milliseconds have passed.
        """
        return datetime.now() + timedelta(milliseconds=milliseconds)
    