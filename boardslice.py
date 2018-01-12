from constants import point_symbol, PointState


class BoardSlice(object):
    def __init__(self, row_offset, column_offset, slice2d, row_labels, parent):
        self._slice2d = slice2d
        self._row_offset = row_offset
        self._column_offset = column_offset
        self._row_labels = row_labels
        self._height = len(slice2d)
        self._width = len(slice2d[0]) if self._height > 0 else 0
        self._parent = parent

    def __repr__(self):
        column_labels = [i + self._column_offset for i in range(0, self._height)]
        ret = '  ' + ' '.join([str(int((i/10) % 10)) for i in column_labels]) + '\n'
        ret += '  ' + ' '.join([str(i % 10) for i in column_labels]) + '\n'
        rows = []
        for i in range(0, len(self._slice2d)):
            row_text = self._row_labels[i] + ' '
            row_text += '|'.join([point_symbol(point) for point in self._slice2d[i]])
            rows.append(row_text)
        ret += '\n'.join(rows)

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @property
    def parent(self):
        return self.parent

    def _assert_is_rectangle(self):
        lengths = [len(row) for row in self._slice2d]
        if len(lengths) <= 1:
            return
        for i in range(1, len(lengths)):
            assert lengths[i] == lengths[0]

    def create_slice(self, row_offset, column_offset, height, width):
        self._assert_is_rectangle()
        assert row_offset + height <= len(self._slice2d)
        assert len(self._slice2d) == 0 or column_offset + width <= len(self._slice2d[0])
        slice2d = [[self._slice2d[row_i][col_i]
                    for col_i in range(column_offset, column_offset + width)]
                   for row_i in range(row_offset, row_offset + height)]
        return BoardSlice(row_offset, column_offset, slice2d, self._row_labels[row_offset:row_offset + width], self)
