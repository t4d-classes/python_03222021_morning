
result = 0.0

history = []


def get_next_entry_id(history_list):
    return max([entry[0] for entry in history_list] or [0]) + 1


command = input("Enter a command > ")

while command:

    if command == "add":
        num = float(input("Enter an operand > "))
        result = result + num
        # more declarative
        next_history_entry_id = get_next_entry_id(history)
        history.append((next_history_entry_id, command, num))
        print(f"Result: {result}")
    elif command == "subtract":
        num = float(input("Enter an operand > "))
        result = result - num
        next_history_entry_id = get_next_entry_id(history)
        history.append((next_history_entry_id, command, num))
        print(f"Result: {result}")
    elif command == "multiply":
        num = float(input("Enter an operand > "))
        result = result * num
        next_history_entry_id = get_next_entry_id(history)
        history.append((next_history_entry_id, command, num))
        print(f"Result: {result}")
    elif command == "divide":
        num = float(input("Enter an operand > "))
        result = result / num
        next_history_entry_id = get_next_entry_id(history)
        history.append((next_history_entry_id, command, num))
        print(f"Result: {result}")
    elif command == "remove":
        history_entry_id = int(input("Enter a history entry id > "))
        for history_entry in history:
            if (history_entry[0] == history_entry_id):
                history.remove(history_entry)
                break
    elif command == "history":
        print(" Id | Command  | Value ")
        print("-----------------------")
        for history_entry in history:
            print(" | ".join([
                str(history_entry[0]).rjust(3),
                history_entry[1].ljust(9),
                str(history_entry[2]).ljust(6)
            ]))
    elif command == "clear":
        result = 0.0
        print(f"Result: {result}")

    command = input("Enter a command > ")
