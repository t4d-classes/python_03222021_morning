

colors = [
    (1, "red", "ff0000"),
    (2, "green", "00ff00"),
    (3, "blue", "00ff00"),
]

color_id = 2

for color in colors:
    if (color[0] == color_id):
        colors.remove(color)
        break

print(colors)
