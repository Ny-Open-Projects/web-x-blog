# 90. 合并 K 个有序链表：最小堆三步法

> 分类：算法与数据结构/堆 | 难度：L3 | 题型：工程题 | 频率：高 | 关键词：**多路归并** / **heapq** / **最小堆** / **哑节点**
> 原文锚点：第 20~25 段「把所有元素放到一个最小堆里，每一次 pop 一个值就是最小的」

## 一句话总述
合并 K 个有序链表用**最小堆**只需三步：**遍历所有链表把值收进列表 → `heapify` 原地建堆 → 反复 `heappop` 取出最小值串成新链表**；时间 `O(N log N)`（N 为总节点数）。

## 面试官视角
- **考察意图**：考**多路归并**建模能力，以及会不会用标准库快速落地。
- **P5** 只能两两归并 / **P6** 写出堆解法并说清复杂度 / **P7** 指出堆里应存 `(值, 序号, 节点)` 以支持**惰性归并**、避免一次性读入 `[实测]`。
- **红旗**：① 空输入不判（见 93）；② 忘了 `heapq` 是**最小堆**，求最大 TopK 不会取负；③ 构造新节点而非复用原节点，浪费空间。
- **惊艳点**：一次性读全部值的写法简单但**额外占用 O(N) 空间**且需先读完；进阶写法是堆里只放**每条链表的当前头节点**，弹出一个就把该链表的下一个补进去，空间降到 `O(k)`。验证：两种写法跑同一输入输出一致 `[实测]`。

## 主问答
**Q：如何合并 K 个有序链表？**
**A：**
1. **思路 1（两两归并）**：复用"合并两个有序链表"（78），顺序把结果和第 3、4…条合并；实现简单，但每次都要重扫，复杂度约 `O(kN)`。
2. **思路 2（堆）**：把所有值收进列表 → `heapify` 建最小堆 → 循环 `heappop` 取最小值接成链表；`heapify` 是**线性时间**的原地操作，整体 `O(N log N)`。
3. **落地**：链表构造常用**哑节点（dummy head）**技巧：先造一个哨兵，用 `cur` 指针往后接，最后返回 `dummy.next`，省掉对首节点的特判。
**加分层**：更优的**惰性归并**是堆中始终只放 k 个"当前头节点"，弹出即补位，复杂度 `O(N log k)`、空间 `O(k)`——这是面试官更想听到的版本。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 两个有序链表怎么合并 | 基础 | 双指针或递归（78） | 换题 → 不及格 |
| L2 | K 个怎么办 | 迁移 | 两两归并 / 堆 | 判 P5 |
| L3 | 堆解法复杂度 | 分析 | O(N log N) | 判 P6 |
| L4 | 能否更省空间 | 优化 | 惰性归并 O(N log k) | 判 P6+ |
| L5 | 边界与稳定性 | 工程 | 空输入、重复值、相等顺序 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Python 3.x | `heapq` 仅提供**最小堆** | 要最大堆则存负值 `[经验]` |
| Python 3.x | `heapify` 线性时间、原地 | 直接对列表调用即可 `[实测]` |
| LeetCode 23 | Merge k Sorted Lists | 可直接引题号对照 |

## 关键代码
```python
import heapq

class ListNode:
    def __init__(self, v=0, nxt=None): self.val, self.next = v, nxt

def merge_k_simple(lists):             # 三步法：读值 → 建堆 → 串链表
    h = []
    for head in lists:                 # 1. 读取所有节点值
        cur = head
        while cur:
            h.append(cur.val); cur = cur.next
    if not h:                          # 边界：空输入 / 嵌套空链表
        return None
    heapq.heapify(h)                   # 2. 原地建最小堆，O(n)
    dummy = cur = ListNode(heapq.heappop(h))
    while h:                           # 3. 依次取最小，串成链表
        cur.next = ListNode(heapq.heappop(h)); cur = cur.next
    return dummy

def merge_k_lazy(lists):               # 进阶：堆中只放 k 个当前头，空间 O(k)
    heap = [(i, head.val, head) for i, head in enumerate(lists) if head]
    heapq.heapify(heap)
    dummy = cur = ListNode()
    while heap:
        i, _, node = heapq.heappop(heap)
        cur.next = node; cur = cur.next
        if node.next: heapq.heappush(heap, (i, node.next.val, node.next))
    return dummy.next
```

## ⚠️ 原文纠错
原文"读值 → heapify → 逐个 heappop 串链表"的三步思路与提交结果一致，予以保留。原文演示代码在**空输入**下抛 `IndexError`（`heappop` 对空堆），原文随后补了判空，该坑已单列成卡（93）。写法上原文把新链表首节点直接作为返回值（无哑节点），卡面补充哑节点写法以简化首节点特判，属工程改进、已标注。转写中的音译词（heapq 等）已还原为标准术语。

## 总结与追问预判
- 三步法：读值 → heapify → 逐出串链；进阶用惰性归并降空间。
- 下一题：见 91（heapq 三板斧）、93（空输入三重坑）。
