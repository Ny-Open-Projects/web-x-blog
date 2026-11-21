---
title: [Q7023] pandas dtype 瘦身与内存画像
date: 2026-11-20
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7023 · pandas dtype 瘦身：同一份数据如何省 70% 内存？

> 难度:★★★ | 标签:pandas, 内存优化, dtype

**问**：一个 2000 万行的 pandas 清洗任务被 OOM 杀掉。除了升级机器，dtype 层面有哪些系统性的降内存手段？收益与风险怎么评估？

**答**：结论：pandas 默认 dtype 极其"奢侈"——字符串是 object（每格一个 Python str 对象）、数值默认 int64/float64、低基数分类字段是重复字符串。系统性瘦身三板斧：**数值降宽**（int64→int32/int16，float64→float32，按值域）、**object→category**（低基数字段，如省份/状态，收益最大）、**日期用 datetime64 而非字符串**。通常可省 50-80% 内存，且 `astype` 降宽会带来溢出与精度风险，必须以值域扫描为前提，不是无脑转型。

机理与实战：
- 内存画像先行：`df.memory_usage(deep=True)` 逐列看账，object 列的 deep 值才是真实占用（浅层只算指针 8 字节）。降宽决策必须基于画像，不是猜。
- category 的边界：`unique/nunique/分组/内存` 全赢；但 `values` 每次访问要走 categories 映射，merge/category 对齐可能隐式转回 object；**category 只给低基数列**，唯一值占比 >50% 时反而变慢。
- downcast 安全线：`pd.to_numeric(col, downcast=...)` 基于实际值域选型，比裸 astype 安全；但写入下游（Parquet/回 DB）要确认 schema，int16 写回 int64 列会有精度/兼容问题——瘦身在"计算态"做，落盘态与表 schema 对齐。

```python
# 基线:Python 3.9+ / pandas 2.x ;缺库降级:纯标准库演示值域判定逻辑
try:
    import pandas as pd
    HAS_PD = True
except ImportError:
    HAS_PD = False


def shrink_memory(df):
    """画像驱动的瘦身:数值降宽+低基数转 category。"""
    start = df.memory_usage(deep=True).sum()
    for col in df.columns:
        s = df[col]
        if pd.api.types.is_integer_dtype(s):
            df[col] = pd.to_numeric(s, downcast="integer")   # 按值域选最小宽度
        elif pd.api.types.is_float_dtype(s):
            df[col] = pd.to_numeric(s, downcast="float")
        elif s.dtype == object:
            ratio = s.nunique(dropna=False) / max(len(s), 1)
            if ratio < 0.05:                                  # 低基数才转
                df[col] = s.astype("category")
    end = df.memory_usage(deep=True).sum()
    return df, start, end


def demo_pd() -> None:
    n = 500_000
    df = pd.DataFrame({
        "user_id": range(n),                        # int64,可降 int32
        "province": [["BJ", "SH", "GZ"][i % 3] for i in range(n)],  # 低基数 object
        "score": [i % 100 for i in range(n)],       # int 语义在 float64?是 int64
    })
    df, a, b = shrink_memory(df)
    print(f"瘦身 {a/1e6:.1f}MB -> {b/1e6:.1f}MB, 节省 {100*(1-b/a):.0f}%")
    print(df.dtypes.to_dict())


def demo_stdlib() -> None:
    """缺库降级:纯标准库演示 int 值域->最小宽度 与 低基数判定。"""
    vals = [100, 32767, -128]
    fits = {"int8": all(-128 <= v <= 127 for v in vals),
            "int16": all(-32768 <= v <= 32767 for v in vals),
            "int32": all(-2**31 <= v <= 2**31 - 1 for v in vals)}
    chosen = next(k for k in ("int8", "int16", "int32") if fits[k])
    print("值域扫描选定宽度:", chosen)
    cards, n = set(["BJ"] * 1000 + ["SH"] * 500), 1500
    print("低基数比例:", len(cards) / n < 0.05)


if __name__ == "__main__":
    demo_pd() if HAS_PD else demo_stdlib()
```

**追问一**：降宽后数值溢出的事故怎么防？
答：downcast 本身基于当前值域不会溢出，风险在**后续写入新数据**——int8 列来了一个 300 就回绕成负数。防线：写入路径做断言或用约束校验（pandera/Pydantic），以及"瘦身只作用于一次性计算任务，长期驻留的表链路保持原宽"。

**追问二**：category 列做 merge 时为什么内存暴涨？
答：两侧 categories 集合不同时 merge 会物化为 object 再对齐，瞬间放大内存。工程惯例：merge 前把 category 显式 astype(object) 或统一 categories，merge 完再转回。

**背诵要点**：
- 画像先行：memory_usage(deep=True) 逐列看账，object 列 deep 值才是真实占用。
- 三板斧：数值 downcast、低基数(<5% 唯一值占比)转 category、日期转 datetime64。
- category 陷阱：merge 对齐物化、高基数反向劣化、访问走映射。

**复盘追问**：
- 如何自动化"值域扫描→dtype 建议"并纳入管道的 lint 步骤？
- Arrow 后端（dtype_backend="pyarrow"）与手动降宽的收益/取舍差异？

## 背诵要点
- int64→最小宽度按值域扫描选择，溢出风险靠写入断言兜底。
- category 收益与基数成反比，<5% 唯一值占比是经验线。
- 瘦身作用于计算态，落盘 schema 与 DB/Parquet 对齐。

## 复盘追问
- 一次 ETL 任务里"读入瘦身→计算→写出原宽"的 dtype 管线怎么组织？
- float64→float32 的精度损失在哪些聚合场景会显性暴露？
