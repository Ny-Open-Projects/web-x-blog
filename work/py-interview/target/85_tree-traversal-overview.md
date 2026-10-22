# 85. 二叉树遍历全景：DFS 四种与 BFS 怎么选

> 分类：算法与数据结构/二叉树 | 难度：L2 | 题型：八股题 | 频率：高 | 关键词：**DFS** / **BFS** / **先中后序** / **递归与栈**
> 原文锚点：第 46~48 段「先序遍历，它是深度优先。而这个我们所说的是什么？是广度优先」

## 一句话总述
二叉树遍历分两大族：**DFS**（先序/中序/后序，递归或显式栈，一路走到底）与 **BFS**（层序，队列，一层一层）；**递归写法本质是栈**，选型取决于你要的是"路径信息"还是"层信息"。

## 面试官视角
- **考察意图**：考**体系感**——能不能一张表说清四五种遍历的顺序、实现与适用场景。
- **P5** 只会先序 / **P6** 说出三种 DFS 顺序差异并写递归 / **P7** 给出非递归写法与"二叉搜索树中序有序"这类应用 `[实测]`。
- **红旗**：① 说"递归不是栈"；② 认为层序只能用递归；③ 背顺序但说不出"根在什么时候被访问"。
- **惊艳点**：一句话区分——**先序看根在首位、中序看根在中间、后序看根在末尾**，区别只在根的访问时机，左右的相对顺序始终是"先左后右"。验证：同一棵树跑三种遍历对照 `[实测]`。

## 主问答
**Q：二叉树的遍历方式有哪些？分别用在什么场景？**
**A：**
1. **分类**：**DFS** 含先序（根-左-右）、中序（左-根-右）、后序（左-右-根）；**BFS** 即层序。递归实现 DFS 的调用栈就是栈结构。
2. **应用**：先序适合**自顶向下传递信息**（如 381 反转二叉树）；中序对**二叉搜索树**得到**有序序列**；后序适合**自底向上**（先算子树再算根，如求树高）；层序用于**按层/最短路径**类问题（如 384 左右视图）。
3. **实现**：递归最简；非递归 DFS 用**显式栈**，BFS 用**队列 `deque`**；递归过深时改显式结构避免 `RecursionError`。
**加分层**：复杂度都是 `O(n)` 时间；空间 `O(h)`（DFS）或 `O(w)`（BFS），w 是最大层宽。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 有几种遍历 | 概念 | DFS 三种 + 层序 | 换题 → 不及格 |
| L2 | 三种 DFS 顺序 | 记忆 | 根在前/中/后 | 判 P5 |
| L3 | 各自适用场景 | 迁移 | 中序有序、后序自底向上 | 判 P6 |
| L4 | 非递归怎么写 | 编码 | 栈 / deque | 判 P6+ |
| L5 | 复杂度与爆栈 | 分析 | O(n)、O(h)/O(w)、改显式栈 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 语言无关 | 与 Python 版本无关 | 按 DFS/BFS 分类作答 |
| CPython 3.x | 递归上限 1000 | 深树改显式栈/队列 `[实测]` |
| Python 3.x | 队列用 `collections.deque` | 不用 `list.pop(0)` |

## 关键代码
```python
from collections import deque

def preorder(root):                    # 根-左-右（381 反转树即此顺序）
    return [] if not root else [root.value] + preorder(root.left) + preorder(root.right)

def inorder(root):                     # 左-根-右：对 BST 得到有序序列
    return [] if not root else inorder(root.left) + [root.value] + inorder(root.right)

def postorder(root):                   # 左-右-根：自底向上，适合算树高
    return [] if not root else postorder(root.left) + postorder(root.right) + [root.value]

def preorder_iter(root):               # 非递归 DFS：显式栈，先压右再压左
    out, stack = [], [root] if root else []
    while stack:
        n = stack.pop()
        out.append(n.value)
        if n.right: stack.append(n.right)
        if n.left:  stack.append(n.left)
    return out

def level_order(root):                 # BFS：队列，按层
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        n = q.popleft(); out.append(n.value)
        if n.left:  q.append(n.left)
        if n.right: q.append(n.right)
    return out
```

## ⚠️ 原文纠错
原文"先序遍历是深度优先、层序遍历是广度优先"的判断正确，予以保留；原文口述的「先跟遍历」标准术语为**先序遍历（pre-order）**，卡面已还原。原文的遍历体系只讲了先序与层序，中序/后序为按标准知识体系补充，已在卡面列明适用场景而未冒称原文内容。

## 总结与追问预判
- 根的访问时机决定先/中/后序；层序用队列。
- 下一题：见 81（反转树=先序）、84（左右视图=层序变形）。
