from functools import reduce


def add_op(x, y):
    return x + y


calc_ops = [
    {"id": 1, "label": "Add", "cmd": "add", "fn": add_op},
    {"id": 2, "label": "Subtract", "cmd": "subtract", "fn": lambda x, y: x - y},
    {"id": 3, "label": "Multiply", "cmd": "multiply", "fn": lambda x, y: x * y},
    {"id": 4, "label": "Divide", "cmd": "divide", "fn": lambda x, y: x / y},
    {"id": 5, "label": "Exponent", "cmd": "exponent", "fn": lambda x, y: x ** y},
]

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
    return max([entry["entry_id"] for entry in history_list] or [0]) + 1


def create_history_entry(entry_id, op_name, op_value):
    return {"entry_id": entry_id, "op_name": op_name, "op_value": op_value}


def append_history_entry(history_list, op_name, op_value):

    new_history_entry = create_history_entry(
        next_entry_id(history_list), op_name, op_value)
    history_list.append(new_history_entry)


def get_calc_op_by_command(calc_ops_list, command_name):

    for calc_op in calc_ops_list:
        if calc_op["cmd"] == command_name:
            return calc_op

# def perform_calc_op(accumulator, current):


def perform_calc_op(result, history_entry):
    calc_op = get_calc_op_by_command(calc_ops, history_entry["op_name"])
    calc_op_fn = calc_op["fn"]

    # return value is the new accumulator/result
    return calc_op_fn(result, history_entry["op_value"])


def calc_result(history_list, calc_ops_list):

    # more declarative
    return reduce(perform_calc_op, history_list, 0)

    # more imperative
    # result = 0
    # for entry in history_list:
    #     calc_op = get_calc_op_by_command(calc_ops_list, entry[1])
    #     calc_op_fn = calc_op[3]
    #     result = calc_op_fn(result, entry[2])
    # return result


def display_operation_counts(history_list):

    op_counts = []

    for calc_op in calc_ops:
        op_counts.append(
            (calc_op["label"],
                len([entry for entry in history_list
                    if entry["op_name"] == calc_op["cmd"]])))

    print("Op Counts")
    print("---------")
    for op_count in op_counts:
        print(f"{op_count[0]}: {op_count[1]}")


def display_history(history_list):
    print(" Id | Op Name | Op Value ")
    print("-------------------------")
    for history_entry in history_list:
        print(" | ".join([
            str(history_entry["entry_id"]).rjust(3),
            history_entry["op_name"].ljust(7),
            str(history_entry["op_value"]).rjust(8)]))


def remove_history_entry(history_list, entry_id):
    for entry in history_list:
        if entry["entry_id"] == entry_id:
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
        print("Result: " + str(calc_result(history, calc_ops)))
    else:
        num = get_operand()
        append_history_entry(history, command, num)
        print("Result: " + str(calc_result(history, calc_ops)))

    command = get_command()
