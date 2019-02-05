class RingBuffer:
    def __init__(self, size: int):
        if size < 0:
            raise ValueError('initializing with negative or zero size')

        self._index = 0
        self._count = 0
        self._buffer = [None] * size

    def write(self, data: list) -> int:
        res = min(len(self._buffer) - self._count, len(data))
        for i in range(0, res):
            self._push(data[i])

        return res

    def read(self) -> int:
        if self._count == 0:
            raise IndexError('read from empty buffer')

        value = int(self._buffer[self._index])
        self._index = self._normalize_index(self._index + 1)
        self._count -= 1
        return value

    def _push(self, item: int):
        self._buffer[self._get_last_index()] = item
        self._count += 1

    def _get_last_index(self) -> int:
        return self._normalize_index(self._index + self._count)

    def _normalize_index(self, index: int) -> int:
        return index % len(self._buffer)
