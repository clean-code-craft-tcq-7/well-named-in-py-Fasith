from config import MAJOR_COLORS, MINOR_COLORS
from prettytable import PrettyTable


def get_color_manual():
    pair_number = 0
    table = PrettyTable(['MAJOR COLOR', 'MINOR COLOR', 'PAIR NUMBER'])
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            pair_number += 1
            table.add_row([major_color, minor_color, pair_number])
    return table
