from typing import Tuple
from math import ceil

def mag_number(info: Tuple[str, int]) -> int:
    weapons = {"PT92":17, "M4A1":30, "M16A2":30, "PSG1":5}
    weapon = info[0]
    streets_count = info[1]
    weapon_bullets_count = weapons[weapon]
    bullets_needed_count = streets_count * 3
    magazines_count = bullets_needed_count / weapon_bullets_count
    return ceil(magazines_count)