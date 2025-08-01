import logger

@logger.logger
def sample_function(a, b, c=1):
    print("Inside sample_function")
    print(f"a: {a}, b: {b}, c: {c}")
    return a * b + c