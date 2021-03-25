from functools import reduce

from models.history_entry import HistoryEntry

class History:

    def __init__(self, calc_ops_list):
        self.__history = []
        self.__calc_ops = calc_ops_list

    @property
    def history(self):
        # computational logic
        return self.__history.copy()

    @history.setter
    def history(self, value):
        # validation logic
        self.__history = value

    def next_entry_id(self):
        return max([entry.id
                   for entry in self.__history] or [0]) + 1

    def create_history_entry(self, entry_id, op_name, op_value):
        return HistoryEntry(entry_id, op_name, op_value)

    def append_history_entry(self, op_name, op_value):

        new_history_entry = self.create_history_entry(
            self.next_entry_id(), op_name, op_value)
        self.__history.append(new_history_entry)

    def get_calc_op_by_command(self, command_name):

        for calc_op in self.__calc_ops:
            if calc_op.cmd == command_name:
                return calc_op

    def perform_calc_op(self, result, history_entry):
        calc_op = self.get_calc_op_by_command(history_entry.op_name)
        return calc_op.fn(result, history_entry.op_value)

    def calc_result(self):
        return reduce(self.perform_calc_op, self.__history, 0)

    @property
    def result(self):
        return reduce(self.perform_calc_op, self.__history, 0)

    def display_operation_counts(self):

        op_counts = []

        for calc_op in self.__calc_ops:
            op_counts.append(
                (calc_op.label,
                    len([entry for entry in self.__history
                        if entry.op_name == calc_op.cmd])))

        print("Op Counts")
        print("---------")
        for op_count in op_counts:
            print(f"{op_count[0]}: {op_count[1]}")

    def display_history(self):
        print(" Id | Op Name | Op Value ")
        print("-------------------------")
        for history_entry in self.__history:
            print(" | ".join([
                str(history_entry.id).rjust(3),
                history_entry.op_name.ljust(7),
                str(history_entry.op_value).rjust(8)]))

    def remove_history_entry(self, entry_id):
        for entry in self.__history:
            if entry.id == entry_id:
                self.__history.remove(entry)
                break

    def clear_history(self):
        self.__history.clear()