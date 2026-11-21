"""del 的容器形态:删切片、删键、删属性,都只是断开引用。"""


class Config:
    def __init__(self):
        self.debug = True
        self.level = 3


if __name__ == "__main__":
    lst = [0, 1, 2, 3, 4, 5]
    del lst[1]
    print("del lst[1]:", lst)
    del lst[1:3]
    print("del lst[1:3]:", lst)
    try:
        del lst[10]
    except IndexError as exc:
        print("del 越界:", exc)

    d = {"a": 1, "b": 2, "c": 3}
    del d["b"]
    print("del d['b']:", d)
    try:
        del d["z"]
    except KeyError as exc:
        print("del 缺键:", exc)

    cfg = Config()
    del cfg.debug
    print("属性删掉了:", not hasattr(cfg, "debug"))

    lst2 = [7, 8, 9]
    lst2.remove(8)            # 按值删
    popped = lst2.pop(0)      # 按位删并返回
    print("remove+pop 之后:", lst2, "| pop 弹出:", popped)
