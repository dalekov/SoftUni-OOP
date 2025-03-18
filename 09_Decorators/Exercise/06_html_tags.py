def tags(html_tag):
    def decorator(func):
        def wrapper(*args):
            res = func(*args)
            return f"<{html_tag}>{res}</{html_tag}>"
        return wrapper
    return decorator
