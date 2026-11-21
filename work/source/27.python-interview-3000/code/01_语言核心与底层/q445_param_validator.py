import functools
import inspect

def validate(**rules):
    """按参数名校验:type 表示类型约束,callable 表示谓词"""
    def deco(func):
        sig = inspect.signature(func)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            for name, checker in rules.items():
                value = bound.arguments[name]
                if isinstance(checker, type):
                    if not isinstance(value, checker):
                        raise TypeError(
                            f"{name} must be {checker.__name__}, got {type(value).__name__}"
                        )
                elif not checker(value):
                    raise ValueError(f"{name} failed predicate with {value!r}")
            return func(*args, **kwargs)
        return wrapper
    return deco

def positive(v):
    return v > 0

@validate(x=int, y=positive)
def scale(x, y):
    return x * y

if __name__ == "__main__":
    print(scale(3, 2.5))
    try:
        scale("3", 2)
    except TypeError as e:
        print("TypeError:", e)
    try:
        scale(3, -1)
    except ValueError as e:
        print("ValueError:", e)
