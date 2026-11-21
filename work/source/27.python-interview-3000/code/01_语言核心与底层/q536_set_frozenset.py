a = {1, 2, 3}
b = {3, 4}

if __name__ == "__main__":
    print("union:", a | b, "intersection:", a & b)
    print("difference:", a - b, "symmetric:", a ^ b)
    print("subset:", {1, 2} <= a)

    fs = frozenset(b)
    d = {fs: "hashable set"}              # frozenset 可做 dict key
    print(d[fs])

    try:
        {a: "x"}                          # 可变 set 不可哈希
    except TypeError as e:
        print("unhashable:", e)

    empty = set()
    print("empty set is not dict:", type(empty).__name__)
