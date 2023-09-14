def print_pyramid():
    # Your task is to create a nested loop to print a pyramid pattern.
    # For instance, a pyramid with a base of 5 would look like:
    #   *
    #  ***
    # *****
    pass

def main():
    print_pyramid()

# Unit tests
def test_print_pyramid():
    import sys
    from io import StringIO

    out = StringIO()
    sys.stdout = out
    print_pyramid()
    sys.stdout = sys.__stdout__
    assert out.getvalue().strip() == '  *\n ***\n*****', 'Test Failed'

if __name__ == '__main__':
    main()
    test_print_pyramid()
