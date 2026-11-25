---
title: "[Q7263] 形状一样的两张表相加全是 NaN：Series 算术的索引对齐陷阱"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7263 · 形状一样的两张表相加全是 NaN：Series 算术的索引对齐陷阱

难度：P5 ｜ 标签：pandas、索引对齐、NaN 传染、fill_value、对账

基线：Python 3.12；用标准库 dict 模拟 pandas 的索引对齐算术语义（含 add(fill_value)），复现对齐产 NaN 与补齐修复，全标准库实跑。

**问**：两张日销售表做 `df1 + df2` 求总销量，行数完全一样，结果却冒出一堆 NaN，而且 NaN 出现的位置跟业务直觉完全对不上。pandas 的算术运算为什么"按索引对齐"而不是"按位置"？这个语义在什么场景是 feature、什么场景是事故？修复的正确姿势是什么？

**答**：
- **结论**：pandas 算术（+、-、merge、concat 对齐类操作）的默认语义是**按标签（索引值）对齐**，不是按位置：两侧索引求并集，标签在任一侧缺失的位置结果就是 NaN。所以"行数一样"不保证"索引一样"——两天卖的商品不同、日期偏了一天、索引被 reset 过再 sort 过，都让对齐错位。这个语义在**时间序列重采样对齐**（两路不同频率数据合并）是 feature：自动找同一时刻；在**顺序数据求和**（明细按行累加）是事故：应该按位置加却按标签加。修复三选一：① 语义就要对齐：补齐索引（`reindex` + `fill_value`）或 `s1.add(s2, fill_value=0)`；② 语义是位置：先把两侧索引统一成 RangeIndex（`reset_index(drop=True)`），或者直接转 numpy 数组运算；③ 汇总类：确认索引语义后再决定，别让"+号能跑"代替"语义想清"。
- **取舍**：① `fill_value` 只补"缺失索引"，不补"本来就是 NaN 的值"——脏数据修补和对齐修补是两回事，别指望一个参数全解决；② MultiIndex / 重复索引的对齐行为更隐蔽（笛卡尔式展开），聚合去重（Q7217/Q7225）要先做；③ 性能账：对齐求并集有哈希成本，大数据量已知索引完全一致时，绕过对齐（values 数组直算）能省不少；④ dtype 参与对齐后的结果类型（int+缺失→float），下游 JSON 序列化要预防（Q7232 numpy 标量序列化）。
- **实战**：① 报表管线里所有跨表算术前先断言索引语义：`s1.index.equals(s2.index)` 不过就显式对齐；② 产出 NaN 后第一件事查索引是否错位，而不是 `fillna(0)` 糊弄过去——fillna 会把真缺失和错位缺失一起洗白；③ 单测覆盖"索引不一致"的用例，锁住对齐语义的预期。

```python
"""Q7263 Series 算术按索引对齐: 不对齐的键变 NaN, fill_value 才是补齐的正确姿势。

标准库模拟 pandas 的对齐语义: dict 键=索引, None 代表 NaN。
"""


class MiniSeries:
    def __init__(self, data: dict[str, float]):
        self.data = dict(data)

    def __add__(self, other: "MiniSeries") -> "MiniSeries":
        """pandas 语义: 按索引对齐求和, 任一方缺失 -> NaN(None)."""
        out = {}
        for k in self.data.keys() | other.data.keys():
            a, b = self.data.get(k), other.data.get(k)
            out[k] = None if (a is None or b is None) else a + b
        return MiniSeries(out)

    def add_fill(self, other: "MiniSeries", fill: float) -> "MiniSeries":
        """等价 s1.add(s2, fill_value=0): 缺失项补 fill 再算."""
        out = {}
        for k in self.data.keys() | other.data.keys():
            a = fill if k not in self.data else self.data[k]
            b = fill if k not in other.data else other.data[k]
            out[k] = a + b
        return MiniSeries(out)

    def nan_keys(self) -> set[str]:
        return {k for k, v in self.data.items() if v is None}


def fmt(s: MiniSeries) -> str:
    return "{" + ", ".join(f"{k}: {'NaN' if v is None else v}" for k, v in sorted(s.data.items())) + "}"


if __name__ == "__main__":
    # 订单表两天各有的商品不同: 直接相加会"造出"NaN
    day1 = MiniSeries({"A": 10, "B": 20, "C": 30})
    day2 = MiniSeries({"B": 5, "C": 6, "D": 7})

    naive = day1 + day2
    print(f"day1        : {fmt(day1)}")
    print(f"day2        : {fmt(day2)}")
    print(f"day1 + day2 : {fmt(naive)}")
    print(f"  -> NaN 键 {sorted(naive.nan_keys())}: 两天都有的 B/C 正常求和, 单日键 A/D 变 NaN")
    ok1 = naive.data["B"] == 25 and naive.data["C"] == 36
    print(f"  -> 对齐语义校验: B=20+5=25, C=30+6=36 -> {'通过' if ok1 else '异常'}")

    filled = day1.add_fill(day2, fill=0)
    print(f"add(fill=0) : {fmt(filled)}")
    ok2 = (filled.data["A"] == 10 and filled.data["D"] == 7
           and not filled.nan_keys())
    print(f"校验: fill_value 消灭 NaN, A=10, D=7 -> {'通过' if ok2 else '异常'}")
    print("结论：pandas 算术默认按索引对齐, 形状相同索引不同照样产 NaN;")
    print("      累计/汇总类先对齐索引或 add(fill_value=0), 报表里的 NaN 多半是对齐造的")
```

**追问一**：为什么"位置语义"和"标签语义"的选择不是小事？举一个选错就资损的例子。

→ 解析：典型的对账场景：订单明细表按行扣减库存表——两表行序一致但索引一个是订单号、一个是 RangeIndex，`stock_df - order_df` 按标签对齐直接全员 NaN，再 `fillna(0)` 就变成"库存一行没减"但报表照常产出——空转的数字比报错危险得多，因为它会一路流进财务口径。反过来，对账合并（按用户 ID 关联两天的余额）必须用标签语义，用位置加等于把甲的余额加到乙头上。所以判据不是"哪个方便"而是"行的身份是什么"：**行有业务身份（键）就标签语义，行是纯序列就位置语义**——这个决定要写进代码注释与单测，因为半年后没人记得当时的表长什么样。

**追问二**：add(fill_value=0) 和先 reindex 再相加，什么时候结果不一样？

→ 解析：当"缺失"有两种含义时不一样。`fill_value=0` 把"索引不存在的项"补成 0，但也**无法区分"该商品当天确实卖 0"和"该商品不在统计范围"**——若商品 D 已下架，统计上不应计入，fill=0 后它作为 0 混进总数，分母类指标（客单价、转化率）的口径被悄悄改变。reindex 方案更可控：显式传入目标索引（`s2.reindex(day1.index.union(day2.index), fill_value=0)`），而且能选择 fill 用 0、NaN 还是前值（ffill），甚至对不在白名单的索引直接丢弃。工程规则：**金额类求和 fill=0 通常无害；比率/均值类指标 fill 必须显式论证**，因为 fill 改变的不只是数值还有分母。这就是"NaN 是对齐造的还是数据本身的"必须先回答——前者补齐，后者要么修数据要么保持 NaN 让下游显式处理。
