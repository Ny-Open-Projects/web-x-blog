# 68. 用 deque 封装一个队列类

> 分类：算法与数据结构/队列 | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**FIFO** / **append** / **popleft**
> 原文锚点：第 75~88 段「我们使用 deque 去实现队列…append 往右边追加，pop 从左边取」

## 一句话总述
队列是 **FIFO（先进先出）**：用 `deque` 时 **入队 = `append`（右端）**、**出队 = `popleft`（左端）**，再补一个 `empty()` 委托 `len(items) == 0` 即可。

## 面试官视角
- **考察意图**：考察"用内置结构组合出高级结构"的能力，以及**委托/组合**而非继承的写法。
- **P5** 能说清 FIFO / **P6** 能写出类并选对两端方法 / **P7** 能指出改用 list 的性能代价与 `maxlen`、并发安全。
- **红旗**：① 入队出队用了同一端（那是栈）；② 用 `list.pop(0)`；③ `empty()` 写成 `items is None`。
- **惊艳点**：这里用**组合（持有 deque 实例）而不是继承 deque**——继承会把不需要的 `appendleft` 等接口一并暴露，破坏 FIFO 约束。验证：对比两种写法的公开方法集 `[实测]`。

## 主问答
**Q：用 Python 实现一个队列，并说明为什么用 deque。**
**A：**
1. **先给结论**：内部持有一个 `collections.deque`，`push`/`enqueue` 委托 `items.append()`，`pop` 委托 `items.popleft()`，天然 FIFO。
2. **再给机制**：deque 两端增删都是 **O(1)**；若用 list，`append` 虽是 O(1)，但头部 `pop(0)` 需要搬移所有元素，是 **O(n)**（见 69）。
3. **最后给边界**：`popleft()` 对**空队列**会抛 `IndexError`，需要在 `pop` 里先判空或明确约定抛异常；`empty()` 用 `len(items) == 0` 判断。
**加分层**：真实生产里如果需要**有界队列 / 阻塞队列**，用 `queue.Queue(maxsize=...)`，它自带锁与阻塞语义，`deque` 只在单线程或已加锁场景下用作容器。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 队列特点 | 术语 | 先进先出 | 换题 → 不及格 |
| L2 | 两端方法名 | 机制 | append / popleft | 判 P5 |
| L3 | 空队列出队 | 边界 | IndexError | 判 P6 |
| L4 | 用 list 行不行 | 权衡 | 行但头删 O(n) | 判 P6+ |
| L5 | 多线程用什么 | 工程 | queue.Queue | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 全版本 | deque 语义稳定 | append + popleft |
| Python 3.x | `queue.Queue` 提供阻塞与超时 | 线程间传递用 Queue，而非裸 deque |

## 关键代码
```python
from collections import deque

class Queue:
    def __init__(self): self.items = deque()
    def push(self, v): self.items.append(v)      # 右端入队
    def pop(self):
        if self.empty(): raise IndexError("pop from empty queue")
        return self.items.popleft()              # 左端出队
    def empty(self): return len(self.items) == 0
    def __len__(self): return len(self.items)

q = Queue()
for i in (0, 1, 2): q.push(i)
print(q.pop(), q.pop(), q.pop())   # 0 1 2 —— FIFO
print(q.empty())                   # True
```

## ⚠️ 原文纠错
原文实现与测试（入 0/1/2，出 0/1/2）均正确；需补正两点：① 原文未处理**空队列出队**会抛 `IndexError` 的边界，卡面已加判空；② 原文留的思考题"用 list 实现的优缺点"，答案在 369 单独展开。转写中的音译词已还原为 deque / queue。

## 总结与追问预判
- 右进左出即 FIFO；空队要判；线程场景换 `queue.Queue`。
- 下一题：见 69（list 队列代价）、70（栈）。
