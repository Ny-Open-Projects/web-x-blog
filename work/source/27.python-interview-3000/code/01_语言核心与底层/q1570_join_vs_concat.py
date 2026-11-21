import io
import timeit

PIECES = ["line-%04d\n" % i for i in range(4000)]


def by_join(parts):
    return "".join(parts)


def by_plus(parts):
    out = ""
    for p in parts:
        out += p                # CPython 特化路径:左值无别名
    return out


def by_stringio(parts):
    buf = io.StringIO()
    write = buf.write
    for p in parts:
        write(p)
    return buf.getvalue()


def by_plus_aliased(parts):
    out = ""
    alias = out                 # 多余引用让 refcount 恒大于 1
    for p in parts:
        out += p                # 特化失效:每轮新建字符串
    return alias, out


if __name__ == "__main__":
    assert by_join(PIECES) == by_plus(PIECES) == by_stringio(PIECES)
    n = 20
    t_join = timeit.timeit(lambda: by_join(PIECES), number=n) / n
    t_plus = timeit.timeit(lambda: by_plus(PIECES), number=n) / n
    t_io = timeit.timeit(lambda: by_stringio(PIECES), number=n) / n
    print("join     : %6.3f ms" % (t_join * 1000))
    print("+=       : %6.3f ms   # 唯一引用时享受原地扩容" % (t_plus * 1000))
    print("StringIO : %6.3f ms" % (t_io * 1000))

    # 别名破坏 += 特化:多一个引用就退化为反复重建
    t_alias = timeit.timeit(lambda: by_plus_aliased(PIECES), number=5) / 5
    print("+= 别名版: %6.3f ms   # 特化失效, 显著变慢" % (t_alias * 1000))

    alias, result = by_plus_aliased(PIECES)
    print("alias stays old:", alias == "",
          "| result correct:", result == by_join(PIECES))
