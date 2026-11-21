"""常见面试陷阱总结(下):拷贝、相等与异常的高频坑。"""
import copy


def trap_shallow_copy():
    """陷阱六:浅拷贝只复制外层,嵌套列表仍然共享。"""
    src = [[1, 2], [3, 4]]
    shallow = copy.copy(src)
    shallow[0].append(99)                 # 影响到 src
    deep = copy.deepcopy(src)
    deep[1].append(88)                    # 只影响 deep 自己
    return src, shallow, deep


def trap_except_name():
    """陷阱七:except as 的名字在块尾被隐式删除。"""
    try:
        raise ValueError("boom")
    except ValueError as e:
        message = str(e)                  # 想块外用,必须先留存
    try:
        print(e)
    except NameError:
        return "块外访问 e 抛 NameError,要用 message 留存", message


def trap_finally_return():
    """陷阱八:finally 里的 return 会覆盖 try 中在飞的异常。"""
    try:
        raise RuntimeError("被吞的异常")
    finally:
        return "finally 的 return 覆盖了一切"


def trap_bool_int():
    """陷阱九:bool 是 int 子类,True 与 1 相等且同哈希。"""
    d = {1: "int"}
    d[True] = "bool"
    return 1 == True, d, isinstance(True, int)


def trap_except_granularity():
    """陷阱十:except Exception 接不住 KeyboardInterrupt。"""
    results = []
    for exc in (ValueError("v"), KeyError("k"), KeyboardInterrupt()):
        try:
            raise exc
        except Exception as e:
            results.append(f"Exception 捕获 {type(e).__name__}")
        except KeyboardInterrupt:
            results.append("KeyboardInterrupt 要单独接")
    return results


if __name__ == "__main__":
    for row in trap_shallow_copy():
        print("陷阱六 浅拷贝联动:", row)
    print("陷阱七 except as 的隐式 del:", trap_except_name())
    print("陷阱八 finally return 吞异常:", trap_finally_return())
    print("陷阱九 bool 是 int 子类:", trap_bool_int())
    print("陷阱十 异常粒度:", *trap_except_granularity(), sep="\n  ")
