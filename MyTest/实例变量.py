# Example of an instance variable
class ClassA():
    def __init__(self):
        self.y = 3

# Example of a static variable
class ClassB():
    x = 7

def main():
    # Create class instances
    a = ClassA()
    b = ClassB()

    # Two ways to print the static variable.
    # The second way is the proper way to do it.
    print(b.x)
    print(ClassB.x)

    # One way to print an instance variable.
    # The second generates an error, because we don't know what instance
    # to reference.
    print(a.y)
    # print(ClassA.y)

main()