"""字典合并的版本兼容写法:管道运算符、解包与 update 的取舍。"""
import sys


def merge_pipe(base, extra):
    """3.9+ 可用:新增的 | 运算符,右优先,返回新字典。"""
    return base | extra


def merge_unpack(base, extra):
    """3.5+ 可用:解包重建新字典,跨老版本的首选写法。"""
    return {**base, **extra}


def merge_update(base, extra):
    """update 法:复制后原地改,语义与上面两种等价。"""
    out = dict(base)
    out.update(extra)
    return out


if __name__ == "__main__":
    base = {"a": 1, "b": 2}
    extra = {"b": 20, "c": 30}

    print("管道法:", merge_pipe(base, extra))
    print("解包法:", merge_unpack(base, extra))
    print("update 法:", merge_update(base, extra))

    print("base 未被修改:", base)
    print("右优先覆盖:", merge_unpack(base, extra)["b"])
    print("本机版本:", f"{sys.version_info.major}.{sys.version_info.minor}")

    # 常见坑:合并是浅的,嵌套结构被整体替换而不是递归合并
    nested_a = {"db": {"host": "a", "port": 1}}
    nested_b = {"db": {"port": 2}}
    print("浅合并覆盖整个子字典:", {**nested_a, **nested_b})
