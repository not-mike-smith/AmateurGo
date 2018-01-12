from constants import PointState, row_names, point_symbol
from boardslice import BoardSlice


class GoBoard(object):
    def __init__(self, other=None, size=19):
        self._row_labels = None
        if other is None:
            row_prototype = [PointState.Empty for _ in range(0, size)]
            self._board = [row_prototype for _ in range(0, size)]
        else:
            self._board = other.board

    @property
    def board(self):
        return [self.board[i].copy() for i in range(0, len(self._board))]

    @property
    def row_labels(self):
        if self._row_labels is None:
            self._row_labels = row_names[0:len(self._board)][::-1]
        return self._row_labels

    def _assert_is_square(self):
        height = len(self._board)
        for row in self._board:
            assert len(row) == height, 'Board is not square'

    def __repr__(self):
        ret = '  ' + ' '.join([str(int(((i+1) / 10) % 10)) for i in range(0, len(self._board))]) + '\n'
        ret += '  ' + ' '.join(str((i+1) % 10) for i in range(0, len(self._board))) + '\n'
        rows = []
        count = 0
        for row in self._board:
            row_text = self.row_labels[count] + ' '
            row_text += '|'.join([point_symbol(point) for point in row])
            rows.append(row_text)
            count += 1
        ret += '\n'.join(rows)
        return ret

    def create_slice(self, row_offset, column_offset, height, width):
        self._assert_is_square()
        assert row_offset + height <= len(self._board)
        assert column_offset + width <= len(self._board)
        slice2d = [[self._board[row_i][col_i]
                    for col_i in range(column_offset, column_offset + width)]
                   for row_i in range(row_offset, row_offset + height)]
        return BoardSlice(row_offset, column_offset, slice2d, self.row_labels[row_offset:row_offset + width], self)
