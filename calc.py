history = []


def input_int(prompt):
    return int(input(prompt))


def input_float(prompt):
    return float(input(prompt))


def get_operand():
    return input_float("Please enter an operand: ")


def get_command():
    return input("Enter a command: ")


def get_history_entry_id():
    return input_int("Please enter a history entry id: ")


def next_entry_id(history_list):
    return max([entry[0] for entry in history_list] or [0]) + 1


def create_history_entry(entry_id, op_name, op_value):
    return (entry_id, op_name, op_value)


def append_history_entry(history_list, op_name, op_value):

    new_history_entry = create_history_entry(
        next_entry_id(history_list), op_name, op_value)
    history_list.append(new_history_entry)


def calc_result(history_list):
    result = 0
    for entry in history_list:
        if entry[1] == "add":
            result = result + entry[2]
        elif entry[1] == "subtract":
            result = result - entry[2]
        elif entry[1] == "multiply":
            result = result * entry[2]
        elif entry[1] == "divide":
            result = result / entry[2]
    return result


def display_operation_counts(history_list):

    add_op_counts = 0
    subtract_op_counts = 0
    multiply_op_counts = 0
    divide_op_counts = 0

    for entry in history_list:
        if entry[1] == "add":
            add_op_counts += 1
        elif entry[1] == "subtract":
            subtract_op_counts += 1
        elif entry[1] == "multiply":
            multiply_op_counts += 1
        elif entry[1] == "divide":
            divide_op_counts += 1

    print("Op Counts")
    print("---------")
    print(f"Add: {add_op_counts}")
    print(f"Subtract: {subtract_op_counts}")
    print(f"Multiply: {multiply_op_counts}")
    print(f"Divide: {divide_op_counts}")


def display_history(history_list):
    print(" Id | Op Name | Op Value ")
    print("-------------------------")
    for history_entry in history_list:
        print(" | ".join([
            str(history_entry[0]).rjust(3),
            history_entry[1].ljust(7),
            str(history_entry[2]).rjust(8)]))


def remove_history_entry(history_list, entry_id):
    for entry in history_list:
        if entry[0] == entry_id:
            history_list.remove(entry)
            break


command = "clear"

while command:

    if command == "history":
        display_history(history)
        display_operation_counts(history)
    elif command == "remove":
        history_entry_id = get_history_entry_id()
        remove_history_entry(history, history_entry_id)
    elif command == "clear":
        history = []
    else:
        num = get_operand()
        append_history_entry(history, command, num)
        print("Result: " + str(calc_result(history)))

    command = get_command()
