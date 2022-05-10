
class Config:
    """
    This class contains the configurable variables used all over the robot package.
    """

    # Logs options
    USE_LOGS = True
    PRINT_LOGS = True
    LOG_DATETIME_STR = "%H:%M:%S.%f"
    
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
    