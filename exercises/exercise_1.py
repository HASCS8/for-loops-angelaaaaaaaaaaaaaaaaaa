def print_numbers():
    # Your task is to use a for loop to print numbers from 1 to 10.
    pass

def main():
    print_numbers()

# Unit tests
def test_print_numbers():
    import sys
    from io import StringIO

    out = StringIO()
    sys.stdout = out
    print_numbers()
    sys.stdout = sys.__stdout__
    assert out.getvalue().strip() == '1\n2\n3\n4\n5\n6\n7\n8\n9\n10', 'Test Failed'

if __name__ == '__main__':
    main()
    test_print_numbers()
