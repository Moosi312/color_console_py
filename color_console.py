import numbers


class Color:
    black = 0
    red = 1
    green = 2
    yellow = 3
    blue = 4
    pink = 5
    brown = 6
    white = 7

    color_dict = {
        "black": 0,
        "red": 1,
        "green": 2,
        "yellow": 3,
        "blue": 4,
        "pink": 5,
        "brown": 6,
        "white": 7
    }

    named_colors = {
        "error": [1, red, black],
        "success": [1, green, None],
        "warning": [1, green, None],
        "info": [1, blue, None]
    }

    _end_string = "\x1b[0m"

    def __init__(self, style=None, col=None, back=None, name=None):
        formats = self.named_colors.get(name, [None, None, None])

        if not isinstance(style, numbers.Integral):
            style = int(style)
        if not 0 <= style < 8:
            style = None
            print("\x1b[31mStyle has to be between 0 and 7. Value will be ignored")

        if isinstance(col, str):
            col = self.color_dict.get(col, None)
        elif not isinstance(col, numbers.Integral):
            col = int(col)
        if not 0 <= col < 8:
            col = None
            print("\x1b[31mColor has to be between 0 and 7. Value will be ignored")

        if isinstance(back, str):
            back = self.color_dict.get(back, None)
        elif not isinstance(back, numbers.Integral):
            back = int(back)
        if not 0 <= back < 8:
            back = None
            print("\x1b[31mBackground has to be between 0 and 7. Value will be ignored")

        if style is not None and int(style) in range(8):
            formats[0] = str(style)
        if col is not None:
            formats[1] = f"3{col}"
        if back is not None:
            formats[2] = f"4{back}"

        self._color_string = f"\x1b[{';'.join([f for f in formats if f is not None])}m"

    def start(self):
        return self._color_string

    def stop(self):
        return self._end_string

    def __enter__(self):
        print(self._color_string, end='')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self._end_string, end='')


with Color(1, 7, 7):
    print("Testing")
