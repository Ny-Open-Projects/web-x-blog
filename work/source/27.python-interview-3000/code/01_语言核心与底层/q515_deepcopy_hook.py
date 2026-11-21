import copy

class Node:
    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def __deepcopy__(self, memo):
        cls = type(self)
        new = cls.__new__(cls)
        memo[id(self)] = new                    # 先登记,防循环与共享分裂
        new.name = copy.deepcopy(self.name, memo)
        new.children = copy.deepcopy(self.children, memo)
        return new

    def __repr__(self):
        return f"Node({self.name!r}, n_children={len(self.children)})"

if __name__ == "__main__":
    tree = Node("root", [Node("a"), Node("b")])
    clone = copy.deepcopy(tree)
    print(clone, "| independent:", clone.children is not tree.children)

    shared = Node("leaf")
    holder = Node("h", [shared, shared])        # 两处引用同一对象
    clone2 = copy.deepcopy(holder)
    print("memo preserves sharing:", clone2.children[0] is clone2.children[1])
