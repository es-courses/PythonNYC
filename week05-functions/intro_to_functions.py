
def add_two_numbers(a: int, b: int) -> int:
    result = a + b 
    return result 


def print_message(name: str) -> None:
    print(f"Welcome {name}!")

if __name__ == '__main__':
    total = add_two_numbers(5, 8)
    print(total)
    total = add_two_numbers(1, 6)
    print(total)

    result = print_message("Michael")
    print(result)

    add_two_numbers()