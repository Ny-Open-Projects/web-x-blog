---
title: [A276] 二叉树序列化与反序列化：前序/层序双口径、null 哨兵与迭代重建
date: 2026-11-24
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A276 · 二叉树序列化与反序列化的两种口径

> 难度:★★★★ | 标签:二叉树, 序列化, 反序列化, 前序遍历, 层序遍历, null 处理, 深度递归

**问**（笔试·编程题）：LeetCode 297 人人会写递归版，面试官要挖的是**口径与实现陷阱**：设计一个二叉树的序列化/反序列化，要求——① **两种口径都实现**：前序 + null 哨兵（`#`）与层序 + null 哨兵，各自精确往返（roundtrip 后结构相等），并断言两种口径产出的 **token 数相同**（都是 `2n+1`，n 为节点数）；② **null 处理**：左空右不空、左不空右空、叶子层的空孩子都要如实编码，缺一个哨兵反序列化就错位——用混合 null 的树断言；③ **递归爆栈陷阱**：2000 层的链状树，递归版序列化抛 `RecursionError`，显式栈的迭代版（序列化+反序列化都迭代）完整往返——说出 Python 默认递归上限与生产代码该选哪版；④ **随机树回归**：固定种子生成 30 棵随机树，两种口径全部往返相等，且前序/层序 token 数相等；⑤ 说清 LeetCode 口径（层序省略叶子层 null）与本口径的差异与代价。请说清与 A012（层序遍历本身，不涉及序列化）、Q369（json 的 default/序列化钩子，树这种非线性结构的 JSON 化是另一个问题域）的分工——本题只回答「**树结构往返的两种口径、null 哨兵的契约与递归深度陷阱**」。

**答**：① 分工：A012 只管遍历（把树读成序列），Q369 管 JSON 的类型钩子——都不管「**序列能不能无损还原结构**」这个核心契约。序列化树的难点恰恰在还原：遍历丢掉的信息是「哪里是空」，null 哨兵就是把「空」也编码进去——有了哨兵，**任何一种确定的遍历序都能唯一还原树**；没有哨兵（如只存中序），结构信息不足，必须再配一个前序/后序才能重建。这是「为什么 297 题必须带 null」的原理层答案。② 两种口径对账：前序口径 token 序是「根、左子树、右子树」递归展开，`#` 充当空子树终结符——反序列化是消费 token 流重建，递归版天然优雅但受深度约束；层序口径按 BFS 逐层展开，每个节点出队时消费两个孩子 token（是 `#` 就置 None，否则建节点入队）——反序列化天然迭代（队列驱动），**没有爆栈问题**，但 token 序对「深链树」冗余更大吗？实测答案是不：两种口径 token 数都是 `n + (n+1) = 2n+1`（n 个实节点 + n+1 个空指针全编码），冗余度完全相同——区别只在 token 的**排列**，不在数量。③ 深度陷阱：Python 默认递归上限 1000（`sys.getrecursionlimit()`），2000 层链状树的递归版直接 `RecursionError`——而且这是**运行时才爆**的定时炸弹：测试环境树浅、生产某条脏数据链深，一序列化就崩。生产铁律：**树深不可控时，序列化与反序列化都必须迭代化**——前序用显式栈（push right 再 push left），反序列化用「栈 + 状态位」（栈里存 `(parent, 待填字段)`，`#` 只推进状态、实节点建后入栈），两者都是 O(n) 时间 O(n) 空间且深度无上限。层序版天生满足这条，这是工程上常选层序的真正原因——不是「BFS 更好看」，是**它免费送了迭代实现**。④ 往返自证：结构相等用递归 `same(a,b)` 判（判例用小树，不受深度限制）；30 棵随机树（固定种子，插入序随机使树形覆盖平衡/退化两极）× 两种口径全部往返相等。⑤ LeetCode 口径的差异：297 的官方样例其实**省略了叶子层的 null**（`[1,2,3,null,null,4,5]` 只标非叶子节点的空孩子）——省 token（约一半）但实现显著更绕：序列化要判断「当前节点是叶子才不发哨兵」，反序列化要维护「哪些节点还在等孩子」的队列语义，边界错误率远高于全哨兵版。工程建议：内部传输/存储用全哨兵版（简单可证），只在对接 LeetCode 风格接口时做一次口径转换；体积敏感再上紧凑编码（值变长编码、哨兵合并成位图——那是 Q5123 的容量账问题）。

```python
# 全部标准库；二叉树序列化双口径：前序/层序 + null 哨兵 + 迭代重建 + 往返自证
import random
import sys
from collections import deque

NULL = "#"


class TreeNode:
    __slots__ = ("val", "left", "right")

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def same(a, b):
    """结构相等：val 与两棵子树逐位相等。"""
    if a is None or b is None:
        return a is b
    return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)


def pre_serialize(root):
    """前序 + 全 null 哨兵：递归版，深度受限。"""
    out = []

    def rec(node):
        if node is None:
            out.append(NULL)
            return
        out.append(str(node.val))
        rec(node.left)
        rec(node.right)

    rec(root)
    return out


def pre_serialize_iter(root):
    """前序迭代版：显式栈，深度无上限。"""
    out, stack = [], [root]
    while stack:
        node = stack.pop()
        if node is None:
            out.append(NULL)
            continue
        out.append(str(node.val))
        stack.append(node.right)                # 先右后左，出栈才是左先
        stack.append(node.left)
    return out


def pre_deserialize_iter(tokens):
    """前序迭代重建：栈中 (parent, 待填字段)，# 只推进状态。"""
    it = iter(tokens)
    first = next(it)
    if first == NULL:
        return None
    root = TreeNode(int(first))
    stack = [[root, "left"]]
    for tok in it:
        parent, field = stack[-1]
        child = None if tok == NULL else TreeNode(int(tok))
        if field == "left":
            parent.left = child
            stack[-1][1] = "right"              # 父帧留在栈顶，转入右孩子
        else:
            parent.right = child
            stack.pop()                         # 右孩子填完，父帧出栈
        if child is not None:
            stack.append([child, "left"])       # 新节点入栈等它的左孩子
    assert not stack
    return root


def level_serialize(root):
    """层序 + 全 null 哨兵：BFS，每个出队节点都发两个孩子 token。"""
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(NULL)
            continue
        out.append(str(node.val))
        q.append(node.left)
        q.append(node.right)
    return out


def level_deserialize(tokens):
    """层序重建：队列驱动，天然迭代、深度无上限。"""
    it = iter(tokens)
    tok = next(it)
    if tok == NULL:
        return None
    root = TreeNode(int(tok))
    q = deque([root])
    while q:
        node = q.popleft()
        tok = next(it)
        if tok != NULL:
            node.left = TreeNode(int(tok))
            q.append(node.left)
        tok = next(it)
        if tok != NULL:
            node.right = TreeNode(int(tok))
            q.append(node.right)
    return root


def build_mixed_null():
    """混合 null 树：1(左空,右=2(左=4,右空))——null 契约的最小考题。"""
    return TreeNode(1, None, TreeNode(2, TreeNode(4), None))


if __name__ == "__main__":
    # 1) 混合 null 树：两种口径往返相等，token 数均为 2n+1
    root = build_mixed_null()
    pre = pre_serialize_iter(root)
    lv = level_serialize(root)
    assert pre == ["1", NULL, "2", "4", NULL, NULL, NULL], pre
    assert lv == ["1", NULL, "2", "4", NULL, NULL, NULL], lv
    assert same(pre_deserialize_iter(pre), root)
    assert same(level_deserialize(lv), root)
    n = 3
    assert len(pre) == len(lv) == 2 * n + 1
    print("混合 null: 前序 %s / 层序 %s，token 数均为 2n+1，往返相等 ✅" % (pre, lv))

    # 2) 递归爆栈陷阱：2000 层链状树，递归版 RecursionError，迭代版往返成功
    chain = TreeNode(0)
    cur = chain
    for i in range(1, 2000):
        cur.right = TreeNode(i)
        cur = cur.right
    try:
        pre_serialize(chain)                    # 递归版
        assert False, "应当爆栈"
    except RecursionError:
        limit = sys.getrecursionlimit()
        assert limit == 1000
    deep_tokens = pre_serialize_iter(chain)     # 迭代版序列化
    rebuilt = pre_deserialize_iter(deep_tokens) # 迭代版重建
    cur, i = rebuilt, 0
    while cur is not None:
        assert cur.val == i
        cur = cur.right
        i += 1
    assert i == 2000
    print("深链 2000 层: 递归版 RecursionError（limit=%d），迭代版序列化+重建全对 ✅" % limit)

    # 3) 随机树回归：30 棵树 × 两种口径，往返相等且 token 数相等
    rng = random.Random(2026)
    for t in range(30):
        n = rng.randint(1, 120)
        rt = None
        for v in rng.sample(range(10000), n):   # 随机插入序：覆盖平衡与退化两极
            if rt is None:
                rt = TreeNode(v)
                continue
            cur = rt
            while True:
                if v < cur.val:
                    if cur.left is None:
                        cur.left = TreeNode(v)
                        break
                    cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = TreeNode(v)
                        break
                    cur = cur.right
        tp, tl = pre_serialize_iter(rt), level_serialize(rt)
        assert len(tp) == len(tl) == 2 * n + 1
        assert same(pre_deserialize_iter(tp), rt)
        assert same(level_deserialize(tl), rt)
    print("随机回归: 30 棵树（含退化链形）两种口径往返全对、token 数全等 ✅")

    # 4) 空树与单节点边界
    assert pre_serialize_iter(None) == [NULL]
    assert pre_deserialize_iter([NULL]) is None
    assert level_deserialize([NULL]) is None
    one = pre_serialize_iter(TreeNode(42))
    assert one == ["42", NULL, NULL] and same(pre_deserialize_iter(one), TreeNode(42))
    print("边界: 空树/单节点往返正确 ✅")
```

**追问**：1) 为什么两种口径 token 数都是 2n+1？—— 全哨兵口径编码的是「**每个节点的全部孩子指针**」：n 个节点共 n+1 个空指针（二叉树指针守恒：`2n = n-1 条边 + n+1 空指针`），实节点 token n 个，合计 2n+1——排列随口径不同、总数是结构常数。这个账反过来给了反序列化的**终止校验**：token 流消费完且栈/队列恰好清空，任何一处哨兵缺失都会表现为「消费到一半 StopIteration 或结构残留」——本题 `assert not stack` 就是这个契约的落点。2) 不用哨兵能不能序列化？—— 能，两条路：a) 存中序+前序两个序列重建（`2n` token，但反序列化要 O(n²) 递归定位或哈希表 O(n)——且只适用**无重复值**的树，重复值下口径崩坏）；b) 对 BST 只存前序、按值域边界重建（LeetCode 105/106 家族）——省空间但把「通用二叉树」限定成了 BST。全哨兵版的价值是**对任意二叉树成立且单序列可还原**，工程上「简单可证」优先于「省 token」。3) 树序列化的生产场景里，递归版真的一无是处吗？—— 不是，分界线在**深度可控性**：表达式树、组织架构树、JSON AST 这类「人写出来的结构」深度通常 <100，递归版最可读；而「数据长出来的结构」（链状退化 BST、动态规划的决策树展开）深度不可控，必须迭代。折中方案是 `sys.setrecursionlimit` 上调——但这只是把炸弹的引线加长，且深递归还吃 C 栈（setlimit 过高会段错误而非 RecursionError），所以铁律仍是：**边界不可控 → 迭代**，和 Q1299（deepcopy 爆栈）是同一条工程判断。
