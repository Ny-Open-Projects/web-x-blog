"""reprlib:大容器表示的截断与定制。"""
import reprlib


def default_truncate():
    big = list(range(100)) + [{"k": i} for i in range(3)]
    r = reprlib.Repr()
    r.maxlist = 6                    # 列表最多显示 6 项
    r.maxdict = 2
    r.maxstring = 12
    return r.repr(big)


class QuietRepr(reprlib.Repr):
    def __init__(self):
        super().__init__()
        self.maxlevel = 2            # 嵌套深度上限
        self.maxother = 24

    def repr_str(self, s, level):
        return "str<" + str(len(s)) + "字节>"    # 长字符串只报尺寸


def log_friendly(obj):
    return QuietRepr().repr(obj)


if __name__ == "__main__":
    print("原生 repr 会全量展开:", repr(list(range(40)))[:44], "……")
    print("reprlib 截断:", default_truncate())
    payload = {"users": ["u" * 500], "meta": {"deep": {"deeper": [1, 2, 3]}}}
    print("日志友好表示:", log_friendly(payload))
