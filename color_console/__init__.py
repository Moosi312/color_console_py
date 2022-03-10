import sys
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
        "black": black,
        "red": red,
        "green": green,
        "yellow": yellow,
        "blue": blue,
        "pink": pink,
        "brown": brown,
        "white": white
    }

    named_colors = {
        "error": [1, red, black],
        "success": [1, green, None],
        "warning": [1, yellow, None],
        "info": [1, blue, None],
        "default": [None, None, None]
    }

    _end_string = "\x1b[0m"

    def __init__(self, style=None, col=None, back=None, name=None, out=sys.stdout, error=True):
        self.out = out
        formats = self.named_colors.get(name, [None, None, None])

        if not isinstance(style, numbers.Integral):
            try:
                style = int(style)
            except TypeError:
                if error:
                    print("\x1b[31mStyle has to be integer\x1b[0m")
            else:
                if not 0 <= style < 8:
                    style = None
                    if error:
                        print("\x1b[31mStyle has to be between 0 and 7. Value will be ignored\x1b[0m")

        if isinstance(col, str):
            col = self.color_dict.get(col, None)
        if not isinstance(col, numbers.Integral):
            try:
                col = int(col)
            except TypeError:
                if error:
                    print("\x1b[31mColor has to be integer or named color\x1b[0m")
            else:
                if not 0 <= col < 8:
                    col = None
                    if error:
                        print("\x1b[31mColor has to be between 0 and 7. Value will be ignored\x1b[0m")

        if isinstance(back, str):
            back = self.color_dict.get(back, None)
        if not isinstance(back, numbers.Integral):
            try:
                back = int(back)
            except TypeError:
                if error:
                    print("\x1b[31mBackground has to be integer or named color\x1b[0m")
            else:
                if not 0 <= back < 8:
                    back = None
                    if error:
                        print("\x1b[31mBackground has to be between 0 and 7. Value will be ignored\x1b[0m")

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
        self.out.write(self._color_string)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.out.write(self._end_string)

    def __getattr__(self, item):
        return Color(name=item)
