import functools

def make(name):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"enter {name}")
            result = func(*args, **kwargs)
            print(f"exit  {name}")
            return result
        return wrapper
    return deco

@make("A")
@make("B")
@make("C")
def core():
    print("  core running")

if __name__ == "__main__":
    core()
    # enter A -> enter B -> enter C -> core -> exit C -> exit B -> exit A
    print(core.__name__)
