

def summarize(values):
    items = list(values)                # 注意:这一步就把迭代器吃光了
    if not items:
        return 0, None
    return sum(items), max(items)


def process(stream, tag):
    print("%-16s ->" % tag, summarize(stream))


if __name__ == "__main__":
    process(iter([3, 1, 4, 1, 5]), "iterator 1st")
    process(iter([]), "iterator empty")  # 耗尽后:静默的 0 与 None

    def gen():
        yield from [3, 1, 4, 1, 5]

    g = gen()
    process(g, "generator 1st")
    process(g, "generator 2nd")          # 静默空结果:最危险的事故形态
    print("iter(x) is x 判别:", iter([1]) is iter([1]) is False,
          "| 生成器是真迭代器:", iter(gen()) is not None)
