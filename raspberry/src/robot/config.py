
class Config:
    """
    This class contains the configurable variables used all over the robot package.
    """

    # Variable indicating whether the robot is in artificial environment testing mode.
    # In this mode, the robot will not perform real word actions.
    # This mode can be changed only by the Robot upon its creation.
    ARTIFICIAL_ENVIRONMENT_TESTING = False

    # Logs options
    USE_LOGS = True
    PRINT_LOGS = True
    LOG_DATETIME_STR = "%H:%M:%S.%f"
    
    # Timeout for each main loop execution in seconds
    MAIN_LOOP_TIMEOUT = 0.1

    # Intigers that indicate the tile colors.
    BLACK_TILE = 0
    WHITE_TILE = 1
    NO_TILE = 2
    UNDEFINED_TILE = 3

    # Dictionary for color names of tiles.
    TILE_COLOR_DICT = {
        BLACK_TILE: "Black",
        WHITE_TILE: "White",
        UNDEFINED_TILE: "Undefined"
    }

    # Scanner timeout in ms.
    # This indicates for how long should the scanner sleep after scanning the tile
    SCANNER_TIMEOUT = 500

    # This indicates in what time the tile will appear
    # in front of the arm after scanning it.
    SCANNER_TILE_EVENT_TIMEOUT = 2000
    