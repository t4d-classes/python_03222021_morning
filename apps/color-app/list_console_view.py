

class ListConsoleView:

    def __init__(self, item_list):
        self.item_list = item_list

    def display_count(self):

        print("Number of items: " + str(len(self.item_list)))

    def display_table(self):
        print(" ".join(self.item_list.headers()))
        print("---------------------------")
        for item in self.item_list:
            print(item.row())
