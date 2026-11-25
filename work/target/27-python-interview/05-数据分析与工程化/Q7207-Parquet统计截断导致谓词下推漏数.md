---
title: "[Q7207] Parquet 统计信息截断导致谓词下推漏数"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7207 · Parquet 统计信息截断导致谓词下推漏数

难度：P7 ｜ 标签：Parquet、统计信息、谓词下推、数据正确性

基线：Python 3.12；Parquet 列统计（min/max）与 row group 裁剪；纯 Python 模拟统计截断。

**问**：一张按 `url` 排序写入的 Parquet 表，查询 `WHERE url >= 'https://example.com/very/long/path...'` 时结果少了几千行；把同一个查询改成 `LIKE 'https://example.com/very/long/%'` 反而正常。文件没坏、数据也在，为什么范围查询会漏？

**答**：
- **结论**：Parquet 的 row group 裁剪依赖列统计的 `min`/`max`。对**字符串**，写入端通常只保留前 N 个字节（常见 64 字节，`statistics.truncate_length`）来避免统计膨胀；**max 被截断后会比真实最大值小**。如果查询下界刚好落在"截断后的 max"和"真实 max"之间，引擎会判定该 row group 不可能命中而直接跳过，产生**假阴性**——结果少了，但不报错。
- **取舍**：开启统计截断能显著减小 footer 体积、加快元数据读取；关闭或调大截断长度会让统计更准，但 footer 变大、解析变慢。`LIKE` 前缀查询能正常，是因为它可能被改写成范围或由其他过滤路径处理，恰好绕开了被截断的 max。正确性敏感的场景应关闭截断或接受"统计只用于加速、不用于排除"的保守策略。
- **实战**：① 对字符串列的范围查询做**对拍**：关掉 row group 裁剪前后结果必须一致；② 长 URL/哈希这类列，查询尽量用完整值等值匹配或前缀，不要依赖范围裁剪；③ 写入端显式设置统计截断长度并写进数据契约；④ 升级 Parquet 库时回归"裁剪正确性"，不同实现的截断策略可能不同。

```python
def row_group_skipped(
    actual_max: str, predicate_lower: str, stat_truncate: int | None
) -> bool:
    """返回该 row group 是否会被统计裁剪跳过。"""
    stat_max = actual_max if stat_truncate is None else actual_max[:stat_truncate]
    # 统计 max 小于谓词下界 -> 引擎认为不可能命中，跳过
    return stat_max < predicate_lower


if __name__ == "__main__":
    actual = "https://example.com/very/long/path/" + "z" * 80
    predicate = "https://example.com/very/long/path/" + "z" * 70
    print("实际 max >= 下界:", actual >= predicate)
    print("截断 64 字节后跳过:", row_group_skipped(actual, predicate, 64))
    print("关闭截断后跳过  :", row_group_skipped(actual, predicate, None))
    print("结论：截断让 max 偏小，范围查询可能被错误裁剪")
```

**追问一**：为什么截断 max 是"向下截断"，而不是保留一个安全的上界？
→ 解析：字符串截断后按字典序比较，前缀相同的短串一定小于长串（`"abc" < "abcd"`），所以截断后的 max 是真实 max 的**下界**，不是上界。引擎若把它当精确 max 用，就会过度裁剪。安全做法是对 max 做"向上取整"（末位加一）或干脆不裁剪 max。

**追问二**：数值列的统计会有类似问题吗？
→ 解析：数值定长、无截断，min/max 是精确的，不会因截断出错；但会有精度/类型问题（float 的 NaN、-0.0、decimal 缩放）以及统计缺失（老文件、复杂类型）。字符串和二进制列才是截断假阴性的重灾区。
