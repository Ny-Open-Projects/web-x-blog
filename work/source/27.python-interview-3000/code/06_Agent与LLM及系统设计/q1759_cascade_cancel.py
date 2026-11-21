"""父任务取消级联传播:子任务树先于父级回收,取消原因沿树传递,取消幂等。"""


class TaskNode:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.cancelled = False
        self.reason = None
        self.cleanups = []                       # 该节点持有的资源清理动作
        if parent is not None:
            parent.children.append(self)

    def cancel(self, reason="parent cancelled"):
        if self.cancelled:
            return False                         # 幂等:重复取消跳过
        self.cancelled = True
        self.reason = reason
        for child in self.children:              # 先孩子后自己
            child.cancel(reason)
        for fn in self.cleanups:
            fn(self.name)
        return True


if __name__ == "__main__":
    events = []
    root = TaskNode("root")
    sub_a = TaskNode("sub-a", parent=root)
    leaf1 = TaskNode("leaf-1", parent=sub_a)
    leaf2 = TaskNode("leaf-2", parent=sub_a)
    sub_b = TaskNode("sub-b", parent=root)
    for node in (root, sub_a, leaf1, leaf2, sub_b):
        node.cleanups.append(lambda name: events.append("cleanup:" + name))

    assert root.cancel("超时终止") is True
    assert root.cancel("重复取消") is False, "取消必须幂等"
    assert all(n.cancelled and n.reason == "超时终止"
               for n in (root, sub_a, sub_b)), "原因沿树传递到每个节点"
    assert events[0].startswith("cleanup:leaf"), "叶子资源最先回收"
    assert events[-1] == "cleanup:root", "根节点最后收尾"
    assert events.index("cleanup:leaf-1") < events.index("cleanup:sub-a") < events.index("cleanup:root")

    late = TaskNode("late-child", parent=root)   # 已取消父节点下新挂子任务
    assert late.cancelled is False, "级联只在取消时刻传播一次"
    late.cancel()
    assert late.cancelled
    print("级联取消通过:子树先回收 根最后 幂等重复取消被跳过")
