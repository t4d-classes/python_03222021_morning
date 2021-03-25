
colors = ["red","green","blue","yellow"]


new_colors_file = open("new_colors.txt", "w")

for color in colors:
    new_colors_file.write(color + "\n")

new_colors_file.close()