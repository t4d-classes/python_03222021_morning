
try:

    with open("colors2.txt", "r") as colors_file:

        for color in colors_file:
            print(color.rstrip())

except IOError as exc:
    print(exc)
except Exception as exc:
    print(exc)
finally:
    print("runs no matter what...")