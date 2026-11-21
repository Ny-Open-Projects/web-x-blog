"""描述符状态存放:存 self 上是全类共享,存实例字典才是每实例一份。"""
import weakref


class SharedStateDesc:
    """反例:计数器存在描述符 self 上,所有实例共用一个数。"""

    def __init__(self):
        self.reads = 0

    def __get__(self, obj, owner=None):
        self.reads += 1
        return self.reads


class PerInstanceStateDesc:
    """正例:状态按实例分存到宿主 __dict__,支持 __slots__ 用 weakref 兜底。"""

    def __init__(self):
        self._states = weakref.WeakKeyDictionary()

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, owner=None):
        if obj is None:
            return self
        state = self._states.get(obj)
        if state is None:
            state = {"reads": 0}
            self._states[obj] = state
        state["reads"] += 1
        return state["reads"]


class Page:
    shared = SharedStateDesc()
    per_instance = PerInstanceStateDesc()


if __name__ == "__main__":
    a, b = Page(), Page()
    a.shared; a.shared
    print("a 读两次后 b.shared =", b.shared, "(被 a 污染,共享 bug)")

    a.per_instance
    a.per_instance
    print("a 读两次后 b.per_instance =", b.per_instance, "(各自独立)")
    print("a.per_instance =", a.per_instance)
