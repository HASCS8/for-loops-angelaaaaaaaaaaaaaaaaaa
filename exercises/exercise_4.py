def print_rectangle():
    # Your task is to create a nested loop to print a rectangle pattern.
    # For instance, a 3x3 rectangle would look like:
    # ***
    # ***
    # ***
    rows = int(input("Please Enter the Total Number of Rows: "))
    col = int(input("Please Enter the Total Number of columns: "))

    print("Rectangle Star Pattern")
    for i in range(rows):
        for j in range(col):
            print('*', end=' ')
        print()

def main():
    print_rectangle()

# Unit tests
def test_print_rectangle():
    import sys
    from io import StringIO

    out = StringIO()
    sys.stdout = out
    print_rectangle()
    sys.stdout = sys.__stdout__
    assert out.getvalue().strip() == '***\n***\n***', 'Test Failed'

if __name__ == '__main__':
    main()
    test_print_rectangle()
