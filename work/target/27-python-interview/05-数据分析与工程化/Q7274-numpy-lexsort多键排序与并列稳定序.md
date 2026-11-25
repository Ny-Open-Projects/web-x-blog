---
title: "[Q7274] 排行榜并列名次全乱了：numpy lexsort 的多键排序与稳定序"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7274 · 排行榜并列名次全乱了：numpy lexsort 的多键排序与稳定序

难度：P6 ｜ 标签：numpy、lexsort、多键排序、稳定排序、并列名次

基线：Python 3.12（numpy 知识卡，代码用纯标准库模拟 lexsort 键序语义保证可运行）；复现"只按分数排序时并列名次不稳定"的事故，实现主键-次键的正确多键排序与 tie-breaker 设计，全标准库实跑。

**问**：榜单需求"分数相同按报名时间先后排"，上线后每周重跑名次会变——`np.argsort(score)` 对并列分数的顺序不保证。numpy 的 argsort 稳定吗？lexsort 的键序为什么"从最后一个键排起"？多键排序里 tie-breaker 怎么设计才算闭环？

**答**：
- **结论**：`np.argsort` 默认 quicksort（introsort），**不稳定**——并列元素的相对顺序在数据排列变化后可能改变，这正是"每周重跑名次会变"的根因；stable 排序（`kind='stable'` 归并）保证并列元素保持原数组顺序，但"原数组顺序"本身也是数据读入顺序，不算业务语义。正确解法是**显式多键**：`np.lexsort((次键, 主键))` ——主键放**最后一个**（lexsort 从最后键排起，最后键是最高优先级），本卡是 `np.lexsort((报名序, -分数))`：分数降序为主、报名序升序为次。tie-breaker 设计闭环的三条铁律：① 次键必须**业务上不可并列**（唯一 id、全序时间戳），否则排序仍未定义；② 次键方向显式化（lexsort 全部升序，降序主键用取负或 `argsort()[::-1]` 配合稳定次键的技巧，别隐式依赖）；③ 排序结果快照化：同输入必同输出（确定性），跨日重跑用 golden 对账（Q7277）。与 SQL `ORDER BY score DESC, sign_up ASC` 语义完全对应——排序需求先写成 SQL 语义再翻译成 numpy，别凭感觉调参数。
- **取舍**：① `kind='stable'` vs lexsort：只有"并列保持输入序"够用时用 stable（少一次排序成本）；业务名次必须 lexsort + 唯一次键——"保持输入序"依赖读入顺序，读入顺序被分片并行读取改变（Q7003 xdist 分片同族）时又是不确定；② lexsort 的成本：k 个键 k 次间接排序（O(N log N) × k），大数组上先用桶/整数编码合并键（如把 `(分数, 报名序)` 打包成一个 64 位整数）单次排序更快——空间换时间的经典取舍；③ 降序的坑：取负对浮点 NaN 会翻成 -NaN 仍排在意外位置，含 NaN 先做 NaN 策略（置底/剔除，Q7226 NaN 传染的同族纪律）；④ 与 pandas `sort_values(['score','sign_up'], ascending=[False,True])` 对齐——pandas 默认快速排序也不稳定（Q7224 同族教训），多键是比 stable 更本质的解。
- **实战**：① 榜单重算的可复现性验收：同一天跑两次结果全等，换机器跑结果全等——做不到就是排序键不完备；② 名次并列的展示语义单独定（同分同名次 1-1-3 还是连续 1-2-3），排序与展示两件事别混；③ 大榜单的增量维护：新数据只 append，全量重排改用"归并插入"（新行二分插入有序数组），但快照对账逻辑不变。

```python
"""Q7274 lexsort 多键排序: 并列名次的稳定 tie-breaker(主键放最后)."""


def unstable_rank(rows: list[dict]) -> list[int]:
    """模拟快排 argsort(score): 并列分数顺序不确定(演示: 按分数, 再按哈希).
    真实 numpy quicksort 的并列序依赖实现, 等价于'不可依赖'."""
    return [r["uid"] for r in sorted(rows, key=lambda r: (r["score"], hash(r["uid"]))) ]


def lexsort_rank(rows: list[dict]) -> list[int]:
    """模拟 np.lexsort((次键, 主键)): 最后键优先 = 分数降序, 次键 = 报名序升序."""
    return [r["uid"] for r in
            sorted(rows, key=lambda r: (-r["score"], r["signup"]))]
    # numpy 对应: np.lexsort((signup, -score))


def assert_total_order(rows: list[dict], ranked: list[int]) -> bool:
    """tie-breaker 闭环检查: 次键必须全序唯一."""
    s = {r["signup"] for r in rows}
    ranked_keys = [(-r["score"], r["signup"]) for r in
                   sorted(rows, key=lambda r: (-r["score"], r["signup"]))]
    return len(s) == len(rows) and ranked_keys == sorted(ranked_keys)


if __name__ == "__main__":
    rows = [{"uid": 10, "score": 90, "signup": 5},
            {"uid": 11, "score": 95, "signup": 2},
            {"uid": 12, "score": 90, "signup": 1},
            {"uid": 13, "score": 95, "signup": 4},
            {"uid": 14, "score": 90, "signup": 3}]
    u1 = unstable_rank(rows)
    u2 = unstable_rank([{**r, "uid": r["uid"] + 100} for r in rows])  # uid 变化
    l1 = lexsort_rank(rows)
    print(f"快排形态(并列序不稳定): {u1} -> 换数据后 {u2}")
    print(f"lexsort(分数降序, 报名序升序): {l1}")
    print("语义校验: 并列 95 分按报名序 2,4 -> 11,13; 并列 90 分按 1,3,5 -> 12,14,10")
    closed = assert_total_order(rows, l1)
    tie_ok = l1.index(11) < l1.index(13) and l1.index(12) < l1.index(14)
    ok = tie_ok and closed and u1 != l1
    print(f"校验: tie-breaker 闭环(次键唯一全序) + 并列顺序正确 -> {'通过' if ok else '异常'}")
    print("结论：argsort 默认不稳定, 并列名次必须显式多键; lexsort 最后键最优先;")
    print("      次键必须业务全序唯一, 排序结果同输入必同输出")
```

**追问一**：为什么"用 stable 排序解决并列"通常还是不够？它与显式多键的本质差别在哪？

→ 解析：stable 只承诺**输入序保持**，而输入序不是业务语义：① 分片/并行读取让输入序不可控（读 8 个分片合并的顺序取决于哪个分片先返回，Q7003/Q7219 的并行秩序同族）；② 数据管道上游的任何重排都会传染下来；③ 输入序承载的可能是"上一次排序的残留"——上周的旧名次顺序污染本周结果，形成看不见的历史耦合。显式多键的本质差别是**把全序关系写进业务定义**：`score DESC, signup ASC` 是业务规则的编码，与物理输入序完全解耦，换数据源、换并行度、换机器结果都一致。stable 排序的正确定位是**工具**而非**契约**：在多键排序内部，第二次排序需要 stable 来保持第一次排序的成果（lexsort 内部正是逐键 stable 排序）——它保证"两步之间不被破坏"，但不定义"第一步从哪来"。面试官想听的一句话总结：**并列顺序是一个业务决策，决策不显式存在，就会由物理世界的偶然性替你做。**

**追问二**：数组很大时多键排序的性能账怎么算？"打包合并键"的编码技巧边界在哪？

→ 解析：lexsort 的成本 = k 次间接排序（每次 O(N log N)，且通过索引间接寻址，缓存不友好）——k=3、N=5000 万时，内存带宽成为瓶颈。打包合并键的思路：把多个键编码进一个 64 位整数后**单次**排序——例如 `key = (score << 24) | signup`（score 占高位 40 位、signup 占低 24 位），一次 argsort 等价于双键 lexsort，速度提升约 k 倍且是单数组直接寻址。编码边界三条：① **位宽预算**：每键分配的位数必须覆盖其值域（signup 超 2^24 就溢出串键），高位的分数范围与低位 id 数相加不能超过 64 位；② **有符号与负数**：整数补码让负数在高位编码后乱序，需要先做偏移（score+常数）或全用无符号域；③ **浮点主键不能直接位移**：浮点数的位模式与数值序不同（符号位、指数），要么转定点数（分数×100 转整型，注意四舍五入口径 Q1433），要么放弃打包退回 lexsort。通用判据：**打包编码是"值域可枚举、键全为整数"时的专属优化；键里一旦有浮点/字符串/超位域，回到多键 lexsort 或 pandas sort_values，正确性优先。**
