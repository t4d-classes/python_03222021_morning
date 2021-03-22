
result = 0.0

command = input("Enter a command > ")

while command:

    if command == "add":
        num = float(input("Enter an operand > "))
        result = result + num
        print(f"Result: {result}")
    elif command == "subtract":
        num = float(input("Enter an operand > "))
        result = result - num
        print(f"Result: {result}")
    elif command == "multiply":
        num = float(input("Enter an operand > "))
        result = result * num
        print(f"Result: {result}")
    elif command == "divide":
        num = float(input("Enter an operand > "))
        result = result / num
        print(f"Result: {result}")
    elif command == "clear":
        result = 0.0
        print(f"Result: {result}")

    command = input("Enter a command > ")
