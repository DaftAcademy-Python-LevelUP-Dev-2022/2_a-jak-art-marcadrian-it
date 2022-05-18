def greeter(func):

    def wrapper_func(*args):
        # Do something before the function.
        
        result="Aloha "+func()
        
        return result.title()
        # Do something after the function.
    return wrapper_func


def sums_of_str_elements_are_equal(func):
    pass


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
