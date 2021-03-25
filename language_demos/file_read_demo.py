
try:

    with open("colors.txt", "r") as colors_file:

        for color in colors_file:
            print(color.rstrip())

except IOError as exc:
    print(exc)
except:
    print("something went wrong")
finally:
    print("runs no matter what...")