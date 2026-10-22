# 93. 空输入三重坑：[]、[[]] 与空堆 heappop

> 分类：算法与数据结构/边界与测试 | 难度：L2 | 题型：事故题 | 频率：中 | 关键词：**嵌套空** / **真值判断** / **IndexError** / **判空时机**
> 原文锚点：第 59~79 段「输入是一个空列表套了一个空列表，这也是一个坑」

## 一句话总述
合并 K 个有序链表时连续踩了三个坑：`heappop` 对**空堆**抛 `IndexError`；输入 `[]` 要判空；而 `[[]]`（**嵌套空列表**）在 Python 里是**真值**，`if not lists` 判不出来——最稳的做法是**判真正要用的堆/列表是否为空**。

## 面试官视角
- **考察意图**：考**边界枚举能力**与对 Python 真值规则的准确理解。
- **P5** 只判最外层 / **P6** 能说出 `[[]]` 是 truthy / **P7** 会把判空放在**真正消费数据的对象**上，并当场列出用例矩阵 `[实测]`。
- **红旗**：① 用 `if not lists:` 试图覆盖 `[[]]`；② 判空后又对空堆 `heappop`；③ 只改一个用例就提交，被下一个用例打回。
- **惊艳点**：通用原则——**边界判空要落在"实际被消费的容器"上**，而不是入参的外壳；本例中就是判 `if not heap: return None`。验证：`bool([])` 为 False、`bool([[]])` 为 True `[实测]`。

## 主问答
**Q：合并 K 有序链表时，空输入有哪几种情况？怎么一次判干净？**
**A：**
1. **坑一**：`heappop([])` 对空堆抛 `IndexError: index out of range`；所以**取最小值前必须先确认堆非空**。
2. **坑二**：入参 `[]`（一条链表都没有）时，收集值的循环不执行，堆为空，直接返回 `None`。
3. **坑三**：入参 `[[]]`（有一条链表，但这条是空的）在 Python 里是**真值**（非空列表，里面装了一个空列表），`if not lists` **判不出来**；归根到底堆还是空的。
**加分层**：所以**统一判 `if not heap: return None`** 即可一次覆盖三种情况——无论外层空还是内层空，值列表都不会被填充。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 空堆 pop 会怎样 | 排错 | 抛 IndexError | 换题 → 不及格 |
| L2 | 怎么修 | 编码 | 取前判空 | 判 P5 |
| L3 | [[]] 是真值吗 | 语言 | 是，非空列表 | 判 P6 |
| L4 | 判空放哪一层 | 设计 | 放在被消费的容器 | 判 P6+ |
| L5 | 如何枚举边界 | 方法 | 空/单/嵌套/极端 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Python 3.x | `bool([[]])` 为 True | 不能用 `not lists` 覆盖 `[实测]` |
| Python 3.x | `heapq.heappop([])` 抛 IndexError | 取前必须判空 |
| 判题平台 | 必测空输入与嵌套空输入 | 提交前本地跑用例矩阵 |

## 关键代码
```python
import heapq
print(bool([]), bool([[]]))            # False True ← 嵌套空列表是真值

try:
    heapq.heappop([])                  # 空堆直接抛错
except IndexError as e:
    print("IndexError:", e)            # index out of range

class ListNode:
    def __init__(self, v=0, nxt=None): self.val, self.next = v, nxt

def merge_k(lists):
    h = []
    for head in lists:                 # 外层空 / 内层空，循环都不执行
        cur = head
        while cur:
            h.append(cur.val); cur = cur.next
    if not h:                          # ★ 一次覆盖 []、[[]]、[[], []]
        return None
    heapq.heapify(h)
    dummy = cur = ListNode(heapq.heappop(h))
    while h:
        cur.next = ListNode(heapq.heappop(h)); cur = cur.next
    return dummy

print(merge_k([]), merge_k([[]]), merge_k([[], []]))   # None None None
```

## ⚠️ 原文纠错
原文最终采用的判空方式（判收集值的列表 `h` 是否为空，从而一次覆盖 `[]` 与 `[[]]`）正确且优于逐层判空，予以保留；原文第一次只判外层 `lists` 导致 `[[]]` 用例仍失败，这个踩坑过程与本卡结论一致。转写中的音译词已还原为标准术语。

## 总结与追问预判
- 空堆 heappop 报错；`[[]]` 是真值；判空落在被消费的容器上。
- 下一题：见 90（堆三步法）、83（空树边界）。
