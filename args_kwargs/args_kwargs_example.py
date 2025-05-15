def greet(greeting, *names, uppercase=False, punctuation="!"):
    for name in names:
        message = f"{greeting}, {name}{punctuation}"
        if uppercase:
            message = message.upper()
        print(message)


# This function just wraps `greet` and forwards all arguments
def greet_wrapper(*args, **kwargs):
    print("Calling greet with:")
    print("  args:", args)
    print("  kwargs:", kwargs)
    greet(*args, **kwargs)


# Call the wrapper with positional and keyword arguments
greet_wrapper("Hello", "Alice", "Bob", uppercase=True, punctuation=".")
