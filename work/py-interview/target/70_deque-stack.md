# 70. 用 deque 实现栈，和队列只差一个方法

> 分类：算法与数据结构/栈 | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**LIFO** / **append** / **pop**
> 原文锚点：第 98~101 段「在 stack 的时候，我们是 append 一个值，然后直接调用 pop 方法，实际上它就默认是从右边去取」

## 一句话总述
栈是 **LIFO（后进先出）**：用 deque 时**入栈和出栈都在右端**——`append()` + `pop()`；与队列（右进左出）**只差出队用的是 `pop` 还是 `popleft`**。

## 面试官视角
- **考察意图**：能否抓住"同一容器换一端方法就换了语义"这个本质。
- **P5** 知道 LIFO / **P6** 能写出类并说清与队列的差异 / **P7** 能展开单调栈、表达式求值、以及用栈做非递归遍历。
- **红旗**：① 把队列和栈的方法写反；② 不知道 `deque.pop()` 默认取右端；③ 空栈 pop 不处理。
- **惊艳点**：栈的核心价值是把**递归改成迭代**——二叉树遍历（见 74）、DFS、括号匹配都靠它消递归。验证：用栈重写中序遍历 `[实测]`。

## 主问答
**Q：怎么用 Python 实现栈？它和队列的实现差别在哪？**
**A：**
1. **先给结论**：内部 `deque`，入栈 `append()`，出栈 `pop()`（右端），两端操作均 O(1)。
2. **再给对比**：**栈 = 同端进出（LIFO）**；**队列 = 右进左出（FIFO）**。实现上唯一区别就是 `pop()` 与 `popleft()`。
3. **最后给边界**：空栈 `pop()` 抛 `IndexError`；`deque` 默认 `pop()` 取**右端**，`popleft()` 才取左端。
**加分层**：Python 里其实**直接用 list 当栈完全没问题**（`append`/`pop` 尾部均摊 O(1)）——这是 list 唯一适合当栈而不适合当队列的原因（见 69）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 栈的特点 | 术语 | 后进先出 | 换题 → 不及格 |
| L2 | 用哪些方法 | 机制 | append / pop | 判 P5 |
| L3 | 与队列差别 | 对比 | pop vs popleft | 判 P6 |
| L4 | 空栈怎么办 | 边界 | IndexError | 判 P6+ |
| L5 | 栈能用来干嘛 | 贯通 | 消递归 / 单调栈 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 全版本 | deque 与 list 均可用 | 需要两端操作时用 deque |
| Python 3.x | list 尾部均摊 O(1) | 纯栈场景 list 即可 |

## 关键代码
```python
from collections import deque

class Stack:
    def __init__(self): self.items = deque()
    def push(self, v): self.items.append(v)      # 右端入
    def pop(self):
        if not self.items: raise IndexError("pop from empty stack")
        return self.items.pop()                  # 右端出 -> LIFO
    def __len__(self): return len(self.items)

s = Stack()
for i in (1, 2, 3): s.push(i)
print(s.pop(), s.pop(), s.pop())   # 3 2 1
# 括号匹配：栈的典型应用
def valid(p):
    st, m = [], {")": "(", "]": "[", "}": "{"}
    for ch in p:
        if ch in m:
            if not st or st.pop() != m[ch]: return False
        else: st.append(ch)
    return not st
print(valid("([]){}"), valid("([)]"))
```

## ⚠️ 原文纠错
原文"append 后直接 pop，默认从右边取"的描述正确；补充一点：原文未提**空栈 pop 抛 IndexError**，卡面已加判空。转写中的音译词已还原为 stack / deque / pop。未发现原理性错误。

## 总结与追问预判
- 同端进出 = 栈；右进左出 = 队列；差别只在 `pop` 与 `popleft`。
- 下一题：见 71（两栈实现队列）、72（最小栈）。
