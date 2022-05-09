
class Config:
    # Intigers that indicate the tile colors.
    BLACK_TILE = 0
    WHITE_TILE = 1
    NO_TILE = 2
    UNDEFINED_TILE = 3

    # Scanner timeout in ms.
    # This indicates for how long should the scanner sleep after scanning the tile
    SCANNER_TIMEOUT = 1000

    # This indicates in what time the tile will appear
    # in front of the arm after scanning it.
    SCANNER_TILE_EVENT_TIMEOUT = 2000
    