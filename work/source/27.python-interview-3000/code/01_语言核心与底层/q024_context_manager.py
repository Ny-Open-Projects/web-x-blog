class Tagged:
    def __init__(self, name, swallow=False):
        self.name = name
        self.swallow = swallow

    def __enter__(self):
        print(f"enter {self.name}")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"exit {self.name}, exc={exc_type.__name__ if exc_type else None}")
        return self.swallow   # True 吞掉异常

if __name__ == "__main__":
    with Tagged("normal"):
        print("  body")

    try:
        with Tagged("swallow", swallow=True):
            raise ValueError("handled inside")
    except ValueError:
        print("  never reaches here")

    try:
        with Tagged("propagate"):
            raise ValueError("goes out")
    except ValueError as e:
        print("  caught outside:", e)
