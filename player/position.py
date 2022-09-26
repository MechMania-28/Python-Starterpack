from mimetypes import init


class Position:
    x = 0
    y = 0
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

    def __init__(self) -> None:
        self.x = 0
        self.y = 0
