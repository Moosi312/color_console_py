class Color:
    black = 0
    red = 1
    green = 2
    yellow = 3
    blue = 4
    pink = 5
    brown = 6
    white = 7

    def __init__(self, name=None, style=None, col=None, back=None):
        formats = [None, None, None]
        if name is not None:
            if name == "error":
                style, col, back = [1, Color.red, Color.black]
            elif name == "success":
                style, col, back = [1, Color.green, None]
        if style is not None and int(style) in range(8):
            formats[0] = str(style)
        if col is not None:
            formats[1] = f"3{col}"
        if back is not None:
            formats[2] = f"4{back}"

        self.color_string = f"\x1b[{';'.join([f for f in formats if f is not None])}m"

    def __enter__(self):
        print(self.color_string, end='')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("\x1b[0m", end='')
