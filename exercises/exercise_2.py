def print_fruits():
    # Your task is to create a list of 5 fruits and use a for loop to iterate over the list and print each fruit.
    pass

def main():
    print_fruits()

# Unit tests
def test_print_fruits():
    fruits_list = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    
    import sys
    from io import StringIO

    out = StringIO()
    sys.stdout = out
    print_fruits()
    sys.stdout = sys.__stdout__
    assert out.getvalue().strip() == '\n'.join(fruits_list), 'Test Failed'

if __name__ == '__main__':
    main()
    test_print_fruits()
