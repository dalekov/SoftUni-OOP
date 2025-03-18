def type_check(type):
    def decorator(func):
        def wrapper(param):
            if not isinstance(param, type):
                return "Bad Type"
            return func(param)
        return wrapper
    return decorator