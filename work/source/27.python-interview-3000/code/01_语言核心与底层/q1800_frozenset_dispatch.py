"""frozenset 的运算分派:结果类型跟随左操作数。"""


def result_type_follows_left():
    s, f = {1, 2, 3}, frozenset({2, 3, 4})
    return type(s - f).__name__, type(f - s).__name__


def method_semantics():
    f, b = frozenset({2, 3, 4}), {3, 4, 5}
    joined = f.union(b)              # 参数任意可迭代,返回 frozenset
    return joined, type(joined).__name__


def unbound_strict():
    s, f = {1, 2}, frozenset({2, 3})
    try:
        frozenset.intersection(s, f)  # 未绑定调用:接收者必须是 frozenset
    except TypeError as e:
        return str(e)[:34]
    return sorted(frozenset.intersection(f, s))


def reflected_keeps_left():
    s, f = {1, 2}, frozenset({2, 3})
    return type(s ^ f).__name__, type(f ^ s).__name__


def hashable_key():
    groups = {
        frozenset({"read", "write"}): "admin",
        frozenset({"read"}): "viewer",
    }
    return groups[frozenset({"read"})]


if __name__ == "__main__":
    rt = result_type_follows_left()
    print("s - f 的类型:", rt[0], "| f - s 的类型:", rt[1])
    print("f.union(set) 语义:", method_semantics())
    print("未绑定调用对接收者的类型检查:", unbound_strict())
    print("对称差结果类型:", reflected_keeps_left())
    print("frozenset 作 dict 键:", hashable_key())
