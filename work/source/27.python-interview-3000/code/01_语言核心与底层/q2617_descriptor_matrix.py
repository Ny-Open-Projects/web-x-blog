"""描述符查找矩阵:数据描述符压制实例字典,非数据描述符被压制。"""


class DataDesc:
    """数据描述符:定义了 __set__,永远优先于实例字典。"""

    def __get__(self, obj, owner=None):
        return "来自数据描述符"

    def __set__(self, obj, value):
        raise AttributeError("数据描述符拒绝写入")


class NonDataDesc:
    """非数据描述符:只有 __get__,会被实例字典同名属性覆盖。"""

    def __get__(self, obj, owner=None):
        return "来自非数据描述符"


class Host:
    dd = DataDesc()
    nd = NonDataDesc()


if __name__ == "__main__":
    h = Host()
    print("dd 实例访问:", h.dd)                  # 数据描述符
    print("nd 实例访问:", h.nd)                  # 非数据描述符

    h.__dict__["nd"] = "实例字典的值"
    print("nd 写入实例字典后:", h.nd)            # 被实例字典覆盖
    print("nd 类访问:", Host.nd)                 # 类访问仍走描述符

    try:
        h.dd = "试试写"
    except AttributeError as exc:
        print("dd 赋值被拦:", exc)

    print("dd 在实例 __dict__ 里塞值也无效:")
    h.__dict__["dd"] = "塞不进去的值"
    print("dd 仍是:", h.dd)
