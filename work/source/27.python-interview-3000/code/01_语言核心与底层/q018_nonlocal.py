counter_value = 0

def bad_counter():
    counter_value += 1   # UnboundLocalError,赋值使它成为局部

def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

if __name__ == "__main__":
    c = make_counter()
    print(c(), c(), c())   # 1 2 3,各闭包独立

    d = make_counter()
    print(d())             # 1,与 c 互不影响
