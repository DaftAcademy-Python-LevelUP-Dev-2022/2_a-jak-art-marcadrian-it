import re
def greeter(func):

    def wrapper_func(*args, **kwargs):
        # Do something before the function.

        result="Aloha "+func(*args, **kwargs)

        return result.title()
        # Do something after the function.
    return wrapper_func


def sums_of_str_elements_are_equal(func):
    def getSum(n):
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

        def wrapper_func(*args, **kwargs):
            # Do something before the function.
            nonlocal negative
            entry = [int(d) for d in re.findall(r'-?\d+', func(*args, **kwargs))]
            if getSum(entry[0]) == getSum(entry[1]):
                result=f'{getSum(entry[0])} == {getSum(entry[1])}'
            else:
                result=f'{getSum(entry[0])} != {getSum(entry[1])}'


            return result
            # Do something after the function.
        return wrapper_func


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
