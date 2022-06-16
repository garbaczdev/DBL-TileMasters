
class Config:
    """
    This class contains the configurable variables used all over the robot package.
    """

    INSTRUCTION_MODE = "instruction"
    MANUAL_MODE = "manual"

    # Variable indicating whether the robot is in artificial environment testing mode.
    # In this mode, the robot will not perform real word actions.
    # This mode can be changed only by the Robot upon its creation.
    ARTIFICIAL_ENVIRONMENT_TESTING = False

    # Logs options
    USE_LOGS = True
    PRINT_LOGS = True
    LOG_DATETIME_STR = "%H:%M:%S.%f"
    LOG_DATE_STR_FORMAT = "%d-%m-%Y"
    LOG_TIME_STR_FORMAT = "%H:%M:%S"
    # Logs printing options
    LOG_ID_SPACE = 10
    LOG_TIME_SPACE = 12
    LOG_COMPONENT_NAME_SPACE = 25
    GET_LOGS_DEFAULT_AMOUNT = 50
    
    # Arm config
    ARM_GPIO_PIN = 17
    ARM_PUSH_TIMEOUT = 0.5

    # Timeout for each main loop execution in seconds
    MAIN_LOOP_TIMEOUT = 0.05

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

    # Event config
    EVENT_TIME_STR = "%H:%M:%S.%f"
    EVENT_TIME_STR_SPACE = LOG_TIME_SPACE

    # Scanner timeout in ms.
    # This indicates for how long should the scanner sleep after scanning the tile
    SCANNER_TIMEOUT = 0.5

    # This indicates in what time the tile will appear
    # in front of the arm after scanning it.
    SCANNER_TILE_EVENT_TIMEOUT = 1.3

    # Minimum amount of readings for a scanner to consider the reading finished
    MIN_SCANNER_READINGS = 10

    # Time that e2e test should wait before starting in s.
    E2E_TESTING_START_TIMEOUT = 0.5
    