from typing import Tuple
import math

def aspect_ratio(x: int, y: int) -> Tuple[int, int]:
    return math.ceil(y * 16/9), y

print(aspect_ratio(640,480))