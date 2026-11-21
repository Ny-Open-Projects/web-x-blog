

def connect(host="localhost", port=5432, *, timeout=3.0, retries=2):
    return (host, port, timeout, retries)


def temp_converter(c, offset=273.15):
    return c + offset


if __name__ == "__main__":
    print("connect defaults :", connect.__defaults__, connect.__kwdefaults__)
    print("call             :", connect())

    # 运行时改默认:影响之后所有调用
    connect.__defaults__ = ("db.internal", 6432)
    connect.__kwdefaults__["timeout"] = 0.5
    print("after mutate     :", connect())

    # 形状错误:defaults 长度与带默认值的参数数不符,下次调用才炸
    connect.__defaults__ = ("only-host",)
    try:
        connect()
    except TypeError as err:
        print("bad shape        :", err)

    # 测试钩子:快照 - 改 - 还原
    saved = temp_converter.__defaults__
    temp_converter.__defaults__ = (0.0,)
    print("shifted          :", temp_converter(25.0))
    temp_converter.__defaults__ = saved
    print("restored         :", temp_converter(25.0))

    # 同一默认可变对象被别名共享(Q004 的运行时视角)
    def append_log(msg, bucket=[]):
        bucket.append(msg)
        return bucket

    alias = append_log
    alias("first")
    print("shared bucket    :", append_log("second"),
          "| same object:",
          append_log.__defaults__[0] is alias.__defaults__[0])
