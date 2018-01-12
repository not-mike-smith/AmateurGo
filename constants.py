from enum import IntEnum


class PointState(IntEnum):
    Empty = 0,
    Black = 1,
    White = -1


row_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']


def point_symbol(point_state):
    if point_state == PointState.Empty:
        return '-'
    elif point_state == PointState.Black:
        return 'X'
    elif point_state == PointState.White:
        return 'O'
    return '?'
