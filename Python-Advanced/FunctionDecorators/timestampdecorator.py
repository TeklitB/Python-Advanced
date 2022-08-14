from datetime import datetime

def timestamp_decorator(tmstamp):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print('{} from {}'.format(tmstamp, our_function.__name__))
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper


@timestamp_decorator('String Timestamp')
def print_timestamp(*args):
    print(f"TimeStamp: {args}") 

@timestamp_decorator('Adding two numbers')
def add_two_numbers(num1, num2):
    print(f"{num1} + {num2} = ", num1 + num2)


@timestamp_decorator('Multiplying two numbers')
def multiply_two_numbers(num1, num2):
    print(f"{num1} * {num2} = ", num1 * num2)


# get current time using now() method
timestamp = datetime.now()

# convert timestamp to human-readable string, following passed pattern:
string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

print_timestamp(string_timestamp)
add_two_numbers(4, 6)
multiply_two_numbers(4, 5)


