# 54. 为什么用 deque 而不是 list 实现栈和队列

> 分类：算法与数据结构/链式结构 | 难度：L2 | 题型：工程题 | 频率：高 | 关键词：**deque** / **双端队列** / **O(1)**
> 原文锚点：第 16、45~50 段「通过 collections 模块里面有个双端队列…可以非常容易去实现这个栈或者实现一个队列」

## 一句话总述
Python 没有内置链表结构，但 `collections.deque` 作为**双端队列**在**两端增删都是 O(1)**，用它实现栈和队列既简单又不会退化。

## 面试官视角
- **考察意图**：是否知道 `list.pop(0)` 是 O(n) 这个经典性能坑。
- **P5** 知道 deque 两端快 / **P6** 说清与 list 头插的复杂度差 / **P7** 能补 maxlen、线程安全、底层分块数组。
- **红旗**：① 用 `list.pop(0)` 做队列；② 以为 deque 是链表所以中间插入也快（其实是 O(n)）；③ 不知道 `maxlen` 的自动丢弃语义。
- **惊艳点**：deque 的 `append`/`popleft` 是**线程安全**的原子操作，单生产者单消费者场景可直接用，无需加锁 `[源码]`。

## 主问答
**Q：怎么用 Python 实现栈和队列？**
**A：**
1. **先给结论**：两者都用 `collections.deque`：**栈** = `append()` + `pop()`（同一端）；**队列** = `append()` + `popleft()`（两端）。
2. **再给机制**：deque 底层是**分块（block）的双端数组**，两端增删均摊 O(1)；而 list 头部 `insert(0, x)` / `pop(0)` 需要整体搬移元素，是 **O(n)**。
3. **最后给边界**：deque **中间**插入删除仍是 O(n)，要按索引随机访问请用 list；`maxlen` 满了会**自动从另一端丢弃**；`rotate(n)` 可做环形位移。
**加分层**：`deque` 还可当**滑动窗口**容器——配合 `maxlen` 维护最近 N 条记录，是监控与限流里的常用写法。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 栈和队列怎么实现 | 术语 | deque 两端操作 | 换题 → 不及格 |
| L2 | 为啥不用 list | 复杂度 | 头删 O(n) | 判 P5 |
| L3 | deque 中间插入快吗 | 边界 | 不快，仍 O(n) | 判 P6 |
| L4 | maxlen 满了会怎样 | 参数 | 自动丢另一端 | 判 P6+ |
| L5 | 有啥实战用法 | 经验 | 滑动窗口/BFS | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 全版本 | 语义稳定 | 队列一律用 `popleft()` |
| Python 3.x | `deque` 支持 `index`/`rotate`/`maxlen` | 需要索引访问时明确它会退化成 O(n) |

## 关键代码
```python
from collections import deque
stack = deque(); stack.append(1); stack.append(2)
print(stack.pop())                  # 2 —— 栈顶（右端）出
q = deque(); q.append("a"); q.append("b")
print(q.popleft())                  # a —— 队首（左端）出
win = deque(maxlen=3)
for i in range(5): win.append(i)
print(list(win))                    # [2, 3, 4] —— 自动丢弃旧元素
dq = deque([1, 2, 3]); dq.appendleft(0); dq.rotate(1)
print(list(dq))                     # [3, 0, 1, 2]
```

## ⚠️ 原文纠错
原文称 deque 是"内置的 collections 模块里的双端队列"，表述正确；但把它描述为"列表这种结构"的替代易引起误解——deque 底层是**分块数组**而非链表，卡面已补正。转写中的音译词已统一还原为 deque / stack / queue。未发现其他技术错误。

## 总结与追问预判
- 栈 = 右端进出，队列 = 右进左出；头操作别用 list。
- 下一题：见 50（结构全景）、63（heapq 与 bisect）。
