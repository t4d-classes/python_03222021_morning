from functools import reduce


class CalcOp:

    def __init__(self, calc_op_id, label, cmd, fn):
        self.id = calc_op_id
        self.label = label
        self.cmd = cmd
        self.fn = fn


class HistoryEntry:

    def __init__(self, entry_id, op_name, op_value):
        self.id = entry_id
        self.op_name = op_name
        self.op_value = op_value


class History:

    def __init__(self, calc_ops_list):
        self.history = []
        self.calc_ops = calc_ops_list

    def next_entry_id(self):
        return max([entry.id
                   for entry in self.history] or [0]) + 1

    def create_history_entry(self, entry_id, op_name, op_value):
        return HistoryEntry(entry_id, op_name, op_value)

    def append_history_entry(self, op_name, op_value):

        new_history_entry = self.create_history_entry(
            self.next_entry_id(), op_name, op_value)
        self.history.append(new_history_entry)

    def get_calc_op_by_command(self, command_name):

        for calc_op in self.calc_ops:
            if calc_op.cmd == command_name:
                return calc_op

    def perform_calc_op(self, result, history_entry):
        calc_op = self.get_calc_op_by_command(history_entry.op_name)
        return calc_op.fn(result, history_entry.op_value)

    def calc_result(self):
        return reduce(self.perform_calc_op, self.history, 0)

    def display_operation_counts(self):

        op_counts = []

        for calc_op in calc_ops:
            op_counts.append(
                (calc_op.label,
                    len([entry for entry in self.history
                        if entry.op_name == calc_op.cmd])))

        print("Op Counts")
        print("---------")
        for op_count in op_counts:
            print(f"{op_count[0]}: {op_count[1]}")

    def display_history(self):
        print(" Id | Op Name | Op Value ")
        print("-------------------------")
        for history_entry in self.history:
            print(" | ".join([
                str(history_entry.id).rjust(3),
                history_entry.op_name.ljust(7),
                str(history_entry.op_value).rjust(8)]))

    def remove_history_entry(self, entry_id):
        for entry in self.history:
            if entry.id == entry_id:
                self.history.remove(entry)
                break

    def clear_history(self):
        self.history.clear()


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


calc_ops = [
    CalcOp(1, "Add", "add", lambda x, y: x + y),
    CalcOp(2, "Subtract", "subtract", lambda x, y: x - y),
    CalcOp(3, "Multiply", "multiply", lambda x, y: x * y),
    CalcOp(4, "Divide", "divide", lambda x, y: x / y),
    CalcOp(5, "Exponent", "exponent", lambda x, y: x ** y),
]

history = History(calc_ops)

command = "clear"

while command:

    if command == "history":
        history.display_history()
        history.display_operation_counts()
    elif command == "remove":
        history_entry_id = get_history_entry_id()
        history.remove_history_entry(history_entry_id)
    elif command == "clear":
        history.clear_history()
        print("Result: " + str(history.calc_result()))
    else:
        num = get_operand()
        history.append_history_entry(command, num)
        print("Result: " + str(history.calc_result()))

    command = get_command()
