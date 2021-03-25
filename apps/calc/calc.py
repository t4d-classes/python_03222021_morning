from get_input import get_operand, get_command, get_history_entry_id
from models.calc_op import CalcOp
from models.history import History

def main():

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

if __name__ == '__main__':
    main()
