"""常见面试陷阱总结(上):可变性、作用域与迭代的高频坑。"""


def trap_return_of_mutator():
    """陷阱一:list.sort 这类修改方法是原地操作,返回 None。"""
    lst = [3, 1, 2]
    result = lst.sort()
    return result, lst


def trap_late_binding():
    """陷阱二:闭包捕获变量本身,循环结束 i 停在 2。"""
    funcs = [lambda: i for i in range(3)]
    fixed = [lambda i=i: i for i in range(3)]
    return [f() for f in funcs], [f() for f in fixed]


def trap_mutate_while_iterate():
    """陷阱三:遍历字典时增删键,下一次 next 立刻炸。"""
    d = {"a": 1, "b": 2, "c": 3}
    try:
        for k in d:
            if k == "a":
                del d[k]
    except RuntimeError as e:
        return str(e)[:20] + "..."
    return "未触发,行为随版本有差异"


def trap_mutable_default(acc=[]):
    """陷阱四:默认值在 def 时求值一次,跨调用共享同一列表。"""
    acc.append(1)
    return acc


def trap_is_vs_eq():
    """陷阱五:常量折叠的对象可能相同,运行时构造绝不该赌 is。"""
    a = "hello world!"
    b = "hello" + " " + "world" + "!"            # 编译期折叠
    c = "".join(["hello", " ", "world", "!"])    # 运行时构造
    return a is b, a is c, a == c


if __name__ == "__main__":
    print("陷阱一 sort 返回值与原列表:", trap_return_of_mutator())
    print("陷阱二 late binding 与固化:", trap_late_binding())
    print("陷阱三 遍历时删键:", trap_mutate_while_iterate())
    print("陷阱四 默认参数跨调用共享:", trap_mutable_default(), trap_mutable_default())
    print("陷阱五 is 与 == 的三个结果:", trap_is_vs_eq())
