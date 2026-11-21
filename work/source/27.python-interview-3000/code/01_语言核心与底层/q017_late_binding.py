import functools

funcs_bad = [lambda: i for i in range(3)]
funcs_ok  = [lambda i=i: i for i in range(3)]
funcs_par = [functools.partial(lambda k: k, i) for i in range(3)]

if __name__ == "__main__":
    print([f() for f in funcs_bad])  # [2, 2, 2]  late binding
    print([f() for f in funcs_ok])   # [0, 1, 2]  默认参数固化
    print([f() for f in funcs_par])  # [0, 1, 2]

    def outer():
        x = 1
        def inner():
            return x
        x = 2           # inner 读到的是最终值
        return inner()
    print(outer())      # 2
