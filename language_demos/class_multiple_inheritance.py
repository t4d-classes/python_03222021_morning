
class Grandparent:

    def __init__(self):
        print("grandparent")
        super().__init__()

class ParentA(Grandparent):

    def __init__(self):
        print("parenta")
        super().__init__()


class ParentB(Grandparent):

    def __init__(self):
        print("parentb")
        super().__init__()

class Child(ParentA, ParentB):
    
    def __init__(self):
        print("child")
        super().__init__()

class Child2(ParentB, ParentA):
    
    def __init__(self):
        print("child 2")
        super().__init__()        


print(Child.__mro__)

Child()

Child2()