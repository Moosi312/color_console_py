from color_console import Color

for style in range(8):
    print()
    with Color(style):
        print(f"Style {style}")
    for color in range(8):
        for back in range(8):
            with Color(style, color, back):
                print(f"{style};3{color};4{back}", end="")
        print()

print("\nOnly Color")
for color in range(8):
    with Color(color=color):
        print(f"3{color}", end=" ")
print()

print("\nOnly Background")
for color in range(8):
    with Color(background=color):
        print(f"4{color}", end="")
    print(end=" ")
print()

print("\nOnly Style")
for style in range(8):
    with Color(style=style):
        print(f"{style}", end=" ")
print("\n")

with Color.error:
    print("Print error message with Color.error or Color.err")
with Color.warning:
    print("Print warning message with Color.warning or Color.warn")
with Color.success:
    print("Print success message with Color.success or Color.succ")
with Color.info:
    print("Print info message with Color.info")
