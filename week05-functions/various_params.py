
def my_function(a, *args, **kwargs):
    print(f"a: {a}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")



my_function(6, 7, 8, 9, 10, 11, name="John", age=34, gpa=3.7)