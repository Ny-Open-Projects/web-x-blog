# 88. peek 与 empty：实现队列时最容易漏的两个接口

> 分类：算法与数据结构/栈与队列 | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**peek** / **empty** / **抽取公共逻辑** / **两栈判空**
> 原文锚点：第 55~65 段「我们还需要实现 push、pop、peek 还有 empty 这四个操作」

## 一句话总述
实现"用栈模拟队列"时，除 `push`/`pop` 外常被要求补 `peek`（**只返回队头不弹出**）与 `empty`（**两个栈同时为空才为空**）；两者都应**复用同一段"倒栈"逻辑**，避免复制粘贴。

## 面试官视角
- **考察意图**：考**接口完备性**与**消除重复**的意识，顺带看边界处理。
- **P5** 只实现 push/pop / **P6** 补齐四个接口且判空正确 / **P7** 抽出 `_pour()` 私有方法，让 pop 与 peek 共用 `[实测]`。
- **红旗**：① `peek` 写成"pop 出来再压回去"（多两次操作且顺序易错）；② `empty` 只看一个栈；③ peek/pop 各抄一遍倒栈代码。
- **惊艳点**：指出题目通常保证**操作合法**（不会对空队列 pop/peek），但**生产代码仍要防御**——接口契约来自调用方，边界要自己兜住 `[经验]`。验证：对空队列调 pop 看是否有明确异常。

## 主问答
**Q：用两个栈实现队列时，peek 和 empty 怎么写？**
**A：**
1. **peek**：逻辑与 pop **前半段完全相同**——输出栈非空就直接看它的栈顶，否则先把输入栈整体倒入，再返回栈顶；区别在于**不弹出**。
2. **消除重复**：把"倒栈"抽成 `_pour()`，`pop` 与 `peek` 都先调它，再各自 `pop()` 或返回 `[-1]`。
3. **empty**：必须 `not in_stack and not out_stack`；只判断输入栈会误判——元素已倒进输出栈时输入栈是空的，但队列并不空。
**加分层**：题目若约定"所有操作合法"，可不处理空队列；但**工程实现建议显式抛 `IndexError`**，把假设变成可观测的失败。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 队列有哪些操作 | 接口 | push/pop/peek/empty | 换题 → 不及格 |
| L2 | peek 与 pop 区别 | 语义 | 查看 vs 弹出 | 判 P5 |
| L3 | 倒栈逻辑放哪 | 设计 | 抽成公共方法 | 判 P6 |
| L4 | 判空看几个栈 | 边界 | 两栈同时空 | 判 P6+ |
| L5 | 题目保证合法还要防御吗 | 工程 | 要，显式抛错 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 语言无关 | 四接口是题目要求 | 按 peek/empty 补齐作答 |
| LeetCode 232 | 约定操作均合法 | 可不判空，但建议保留 |
| Python 3.x | 空 list 取 [-1] 抛 IndexError | 与显式抛错行为一致 `[实测]` |

## 关键代码
```python
class MyQueue:
    def __init__(self): self.in_s, self.out_s = [], []
    def push(self, x): self.in_s.append(x)
    def _pour(self):                       # 公共逻辑：只在输出栈空时倒
        if not self.out_s:
            while self.in_s:
                self.out_s.append(self.in_s.pop())
    def _check(self):
        if not self.in_s and not self.out_s:
            raise IndexError("queue is empty")
    def pop(self):
        self._check(); self._pour(); return self.out_s.pop()
    def peek(self):
        self._check(); self._pour(); return self.out_s[-1]   # 只返回不弹
    def empty(self):
        return not self.in_s and not self.out_s               # 两栈同时空

q = MyQueue()
q.push(1); q.push(2)
print(q.peek(), len(q.in_s) + len(q.out_s))   # 1 2 —— peek 不减少元素
print(q.pop(), q.empty())                     # 1 False
print(q.pop(), q.empty())                     # 2 True
```

## ⚠️ 原文纠错
原文四接口（push/pop/peek/empty）的拆分正确，予以保留；原文实现中 peek 与 pop 各自重复了一遍倒栈代码，卡面改为**抽取公共方法**更可维护（该改进属工程建议，已标注）。原文"两个栈都为空才算 empty"的判断正确。转写中的音译词已还原为标准术语。

## 总结与追问预判
- peek 不弹出、empty 看两栈；倒栈逻辑抽成公共方法。
- 下一题：见 71（两栈队列）、87（单栈为何无解）。
