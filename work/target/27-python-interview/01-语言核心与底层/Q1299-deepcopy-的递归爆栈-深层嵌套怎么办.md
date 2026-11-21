---
title: [Q1299] deepcopy 的递归爆栈:深层嵌套怎么办
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1299 · deepcopy 的递归爆栈:深层嵌套怎么办

> 难度:★★★☆☆ | 标签:deepcopy, 递归, 疑难杂症

**问**:deepcopy 一个 5000 层嵌套的列表会怎样?为什么会爆栈?怎么修?

**答**:copy.deepcopy 是递归实现,每层嵌套消耗一段 Python 栈,深度超过 sys.getrecursionlimit(默认 1000,Q409)就抛 RecursionError——注意 Q005/Q515 讲的是浅深拷贝语义与 __deepcopy__ 定制,本题是容量问题。修复按序:能用浅拷贝就不用深(先确认真的有可变共享);必须深拷贝时改成迭代——显式栈遍历或按层重建,把「解释器递归」换成「数据结构递归」;或调大 recursionlimit(Q409 已警告 C 栈风险,治标)。设计层的正解:让数据结构别长这么深——链表式嵌套改显式树/图 + 节点表,序列化(JSON)天然扁平化。另一个坑:memo 参数(处理共享与循环引用)在自写迭代拷贝时必须等价复刻,否则共享子结构会被复制成多份,既是内存错误也是语义错误。

```python
# file: code/01_语言核心与底层/q1299_deepcopy_recursion.py
import copy
import sys


def build_nested(depth):
    node = []
    for _ in range(depth):
        node = [node]
    return node


def depth_of(node):
    d = 0
    while isinstance(node, list) and node:
        node = node[0]
        d += 1
    return d


def iterative_copy(root):
    # 针对本结构(每层恰一个孩子, 最内层为空)的迭代重建:从叶子逐层向外
    depth = depth_of(root)
    cur = []
    for _ in range(depth):
        cur = [cur]
    return cur


if __name__ == "__main__":
    print("recursionlimit:", sys.getrecursionlimit())
    shallow = build_nested(300)
    copied = copy.deepcopy(shallow)
    print("deepcopy depth 300 ok:", depth_of(copied) == 300,
          "<- 每层约耗 2 个栈帧, 500 层已贴着默认限制")
    deep = build_nested(5000)
    try:
        copy.deepcopy(deep)
    except RecursionError as e:
        print("depth 5000 ->", type(e).__name__)
    fixed = iterative_copy(deep)
    print("iterative copy depth:", depth_of(fixed))
```

**追问**:1) json.dumps 同样深度会炸吗?——会,标准 json 编码器也是递归的;要么换迭代序列化器,要么先把结构扁平化,原理与本题一致。2) 为什么递归会爆栈?——deepcopy 每层同时消耗 Python 帧(可被 recursionlimit 控制)与 C 栈(eval 嵌套,3.11+ 有保护但仍有硬限);几千层嵌套的 RecursionError 不是 bug 是设计。3) 缓解手段?——迭代式自写复制(显式栈 + visited)、限制输入深度(校验层拒绝深嵌套)、结构扁平化;调高 setrecursionlimit 是把崩溃推迟成段错误。4) 生产陷阱?——用户可控的深嵌套 JSON 打到序列化/反序列化路径(DoS 面),入口必须限深;CPython 本地能过、其他实现崩;递归 copy 与递归 repr 同源爆栈。
