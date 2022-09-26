from mimetypes import init


class Position:

    def __init__(self) -> None:
        self._x = 0
        self._y = 0

    def __init__(self, x:int, y:int) -> None:
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, x:int):
        self._x = x

    _x = property(get_x, set_x)


