# 81. 反转二叉树（镜像）：递归三行是怎么来的

> 分类：算法与数据结构/二叉树 | 难度：L2 | 题型：工程题 | 频率：高 | 关键词：**镜像** / **递归** / **先序** / **swap**
> 原文锚点：第 15~34 段「如果这个根不为空的话，我们就把这个左孩子跟这个右孩子来进行一个交换」

## 一句话总述
反转二叉树就是求**镜像**：对每个节点**交换左右孩子**，再**递归处理左右子树**；本质是**先序遍历**（先处理根、再递归左右），代码只有几行。

## 面试官视角
- **考察意图**：看你是真懂递归，还是背了一段代码；关键在二叉树是**递归定义**的。
- **P5** 写不出 / **P6** 写出递归并说清"先序" / **P7** 补出迭代栈写法与 O(n)/O(h) 复杂度并点出深树爆栈 `[实测]`。
- **红旗**：① 只交换不递归（只翻了根一层）；② 忘记 `return root`；③ 把"遍历"和"原地修改"混为一谈。
- **惊艳点**：递归栈深 = 树高 h，**退化成链时会 RecursionError**（CPython 默认上限 1000）`[实测]`。验证：构造 2000 节点链状树跑递归版即可复现。

## 主问答
**Q：手写反转二叉树，并说明你的思路。**
**A：**
1. **定义**：二叉树是**递归定义**的——任意子树依然是二叉树，所以每个节点可以用同一套动作处理。
2. **动作**：对每个节点 **swap(left, right)** → 递归左子树 → 递归右子树 → **return root**；顺序与**先序遍历**完全一致。
3. **复杂度**：每节点访问一次，时间 `O(n)`；递归栈 `O(h)`，h 为树高（平衡树 `O(log n)`，退化成链 `O(n)`）。
**加分层**：Python 里 `root.left, root.right = root.right, root.left` 是元组解包，无需临时变量；要求非递归时用**显式栈做先序**、出栈即交换。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 什么叫镜像 | 概念 | 左右孩子互换 | 换题 → 不及格 |
| L2 | 写递归版 | 编码 | 先交换再递归左右 | 判 P5 |
| L3 | 和先序遍历的关系 | 迁移 | 顺序一致：先根后左右 | 判 P6 |
| L4 | 时间空间复杂度 | 分析 | O(n) / O(h) | 判 P6 |
| L5 | 树退化成链怎么办 | 边界 | 递归爆栈，改显式栈 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 语言无关 | 与 Python 版本无关 | 按递归 + 先序作答 |
| CPython 3.x | 递归上限默认 1000 | 深树改显式栈 `[实测]` |
| LeetCode 226 | Invert Binary Tree | 可直接引题号对照 |

## 关键代码
```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

def invert(root):                      # 递归：先序（处理根 → 左右）
    if root is None:
        return None
    root.left, root.right = root.right, root.left   # 元组解包交换
    invert(root.left)
    invert(root.right)
    return root

def invert_iter(root):                 # 迭代：显式栈，避免深树 RecursionError
    stack = [root] if root else []
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        stack.extend(n for n in (node.left, node.right) if n)
    return root
```

## ⚠️ 原文纠错
原文"交换左右孩子 → 递归左右子树 → 返回根"的思路正确，予以保留。原文口述的「先跟遍历」标准术语应为**先序遍历（pre-order）**，卡面已还原。原文关于 Homebrew 作者面试轶事的段落属背景故事、与解法无关，未进卡面。

## 总结与追问预判
- 交换 → 递归左右 → `return root`；O(n) 时间、O(h) 栈。
- 下一题：见 82（层序遍历）、83（空树边界）。
