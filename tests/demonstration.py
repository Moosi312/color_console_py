from color_console import Color

for style in range(8):
    print(f"\nStyle {style}")
    for color in range(8):
        for back in range(8):
            with Color(style, color, back, error=False):
                print(f"{style};3{color};4{back}", end="")
        print()

print("\nOnly Color")
for color in range(8):
    with Color(col=color, error=False):
        print(f"3{color}", end=" ")
print()

print("\nOnly Background")
for color in range(8):
    with Color(back=color, error=False):
        print(f"4{color}", end="")
    print(end=" ")
print()

print("\nOnly Style")
for style in range(8):
    with Color(style=style, error=False):
        print(f"{style}", end=" ")
print()
