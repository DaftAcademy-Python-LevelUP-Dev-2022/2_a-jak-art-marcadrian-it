import re
def greeter(func):

    def wrapper_func(*args):
        # Do something before the function.

        result="Aloha "+func(*args)

        return result.title()
        # Do something after the function.
    return wrapper_func

def sums_of_str_elements_are_equal(func):
    def getSum(n):
        negative = False
        if n<0:
            n=abs(n)
            negative=True
        sum = 0
        while (n != 0):

            sum = sum + int(n % 10)
            n = int(n/10)
        if negative==True:
            return -abs(sum)
        else:
            negative=False
            return sum
    negative = False
    def wrapper_func(*args):
        # Do something before the function.
        nonlocal negative
        entry = [int(d) for d in re.findall(r'-?\d+', func(*args))]
        if getSum(entry[0]) == getSum(entry[1]):
            result=f'{getSum(entry[0])} == {getSum(entry[1])}'
        else:
            result=f'{getSum(entry[0])} != {getSum(entry[1])}'


        return result
        # Do something after the function.
    return wrapper_func






def format_output(*required_keys):
    def decorator(func):
        def wrapper_func(*args):
            entry = func(*args)
            result = {}
            for key in required_keys:
                if '__' in key:
                    split_keys = key.split('__')
                    for single_key in split_keys:
                        if single_key not in entry:
                            raise ValueError

                    result[key] = ""
                    for i in range(len(split_keys)):
                        result[key] = result[key] + entry[split_keys[i]] + " "
                    result[key] = result[key][:-1]

                else:
                    if key in entry:
                        if entry[key] != "":
                            result[key] = entry[key]
                        else:
                            result[key] = "Empty value"
                    else:
                        raise ValueError

            return result
        return wrapper_func
    return decorator

def add_method_to_instance(klass):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            return func()
        setattr(klass, func.__name__, inner_wrapper)
        return inner_wrapper
    return outer_wrapper
