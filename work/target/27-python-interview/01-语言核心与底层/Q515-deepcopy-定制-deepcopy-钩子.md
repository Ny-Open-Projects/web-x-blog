---
title: [Q515] deepcopy 定制:__deepcopy__ 钩子
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q515 · deepcopy 定制:__deepcopy__ 钩子

> 难度:★★★★ | 标签:copy, 深拷贝

**问**:deepcopy 慢或行为不对时,如何定制?memo 参数为什么必须传下去?

**答**:copy.deepcopy 优先调用对象的 __deepcopy__(self, memo) 钩子,不走通用的递归反射。定制动机:跳过不可拷贝资源(连接、锁)、按业务语义决定深浅边界、加速大对象。memo 是「id → 已拷贝对象」的登记表,职责有二:防循环引用(self 引用自己时先登记再拷贝)、保持共享——两处引用同一对象时拷贝后仍是同一个;自己的实现必须用 copy.deepcopy(x, memo) 传递并先 `memo[id(self)] = new`,否则环形结构栈溢出、共享对象被分裂成多份。

```python
# file: code/01_语言核心与底层/q515_deepcopy_hook.py
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
```

**追问**:1) 只想要「浅一点」的定制用什么钩子?——__copy__ 控制浅拷贝行为;还可实现 __reduce__ 参与序列化式拷贝,三者的优先级是 __deepcopy__ > __reduce_ex__ > 通用反射。2) 为什么 deepcopy 慢又容易踩坑?——全图递归复制 + memo 字典防环防共享;含锁/socket/连接等不可复制资源的对象要么抛错要么产出死副本——都需要 __deepcopy__ 定制。3) 底层调度顺序?——copy.deepcopy 先问 __deepcopy__(memo),否则走 __reduce_ex__ 重建;memo 按 id 记录「已复制」保证共享对象只复制一次(DAG 语义)。4) 生产陷阱?——复制含 threading.Lock 的配置直接崩或得到死锁副本;性能黑洞,批量场景应显式工厂函数;浅拷贝 copy() 保护不了嵌套结构——分不清浅/深是真实事故源。
