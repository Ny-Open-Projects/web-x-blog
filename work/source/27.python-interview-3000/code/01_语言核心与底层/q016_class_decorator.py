import functools

class CallCounter:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"call #{self.count}")
        return self.func(*args, **kwargs)

@CallCounter
def greet(name):
    return f"hello {name}"

if __name__ == "__main__":
    print(greet("alice"))
    print(greet("bob"))
    print(greet.count)      # 状态可直接读取
    print(greet.__name__)   # greet,元信息已拷贝
