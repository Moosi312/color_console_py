from color_console import Color
import unittest


class TestColors(unittest.TestCase):
    def test_numbers(self):
        for style in range(8):
            for color in range(8):
                for back in range(8):
                    self.assertEqual(Color(style, color, back)._color_string, f"\x1b[{style};3{color};4{back}m",
                                     "Color does not produce correct string")

    def test_names(self):
        names = {
            "error": "\x1b[1;31;40m",
            "success": "\x1b[1;32m",
            "warning": "\x1b[1;33m",
            "info": "\x1b[1;34;m",
            "default": "\x1b[m"
        }
        for name, col_string in names.items():
            self.assertEqual(Color(name=name), col_string, "Name does not match correct string")

    def test_dicts(self):
        colors = [("black", 0), ("red", 1), ("green", 2), ("yellow", 3),
                  ("blue", 4), ("pink", 5), ("brown", 6), ("white", 7)]
        for style in range(8):
            for color in colors:
                for back in colors:
                    self.assertEqual(Color(style, color[0], back[0])._color_string,
                                     f"\x1b[{style};3{color[1]};4{back[1]}m",
                                     "Names colors do not produce correct string")

    def test_oor(self):
        self.assertEqual(Color(8, 8, 8)._color_string, "\x1b[m", "Out of range produces wrong string")
        self.assertEqual(Color(col="Banana", back="Oachkatzl"), "\x1b[m", "Unknown color produces wrong string")
