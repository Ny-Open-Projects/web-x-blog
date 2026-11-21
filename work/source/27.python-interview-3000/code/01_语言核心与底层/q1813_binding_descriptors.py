"""classmethod/staticmethod 的描述符本质:绑定时机。"""
import types


class Meta:
    version = "1.0"

    def instance_method(self):
        return "bound to " + type(self).__name__

    @classmethod
    def klass(cls):
        return "bound to class " + cls.__name__

    @staticmethod
    def plain():
        return "no binding"


def descriptor_view():
    rows = []
    for name in ("instance_method", "klass", "plain"):
        attr = Meta.__dict__[name]
        rows.append((name, type(attr).__name__))
    return rows


if __name__ == "__main__":
    print("类体内是描述符对象:", descriptor_view())
    m = Meta()
    print("实例调用:", m.instance_method(), "|", m.klass(), "|", m.plain())
    print("__get__ 绑定结果:",
          type(Meta.__dict__["instance_method"].__get__(m, Meta)).__name__,
          type(Meta.__dict__["klass"].__get__(None, Meta)).__name__,
          type(Meta.__dict__["plain"].__get__(None, Meta)).__name__)
    print("普通函数也是描述符:",
          isinstance(Meta.__dict__["instance_method"], types.FunctionType))
