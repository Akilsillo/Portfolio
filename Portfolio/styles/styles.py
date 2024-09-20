import reflex as rx
from enum import Enum

MAX_WIDTH = "900px"
IMAGE_HEIGHT = "200px"

class EmSize(Enum):
    """Enum for different types of em sizes"""
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "2em"
    BIG = "4em"
    
class Size(Enum):
    """Enum for different types of sizes"""
    ZERO = "0"
    SMALL = "2"
    DEFAULT = "4"
    MEDIUM = "6"
    BIG = "8"
    
BASE_STYLE = {
    rx.button: {
        "--cursor-button": "pointer"
    }
}

STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
]