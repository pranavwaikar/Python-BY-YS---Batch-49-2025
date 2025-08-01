import logger

# @logger.logger('my_log.txt')

@logger.logger('my_log.txt')
def sample_function(a, b, c=1):
    print("Inside sample_function")
    print(f"a: {a}, b: {b}, c: {c}")
    return a * b + c

@logger.logger('my_log2.txt')
def my_function(x, y):
    print("Inside my_function")
    print(f"x: {x}, y: {y}")
    return x + y

for i in range(2):
    result = sample_function(i, i + 1, c=i + 2)
    print(f"Result of sample_function: {result}")
    result2 = my_function(i, i + 1)
    print(f"Result of my_function: {result}")   