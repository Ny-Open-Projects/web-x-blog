---
title: [Q6632] Redis 小对象编码（intset/ziplist/listpack）与内存容量账
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6632 · Redis 小对象编码优化与内存容量账

难度：P6 ｜ 标签：容量规划 / Redis / 内存

**问**：同一份"1 万个用户 ID 列表"，用 List 存 hash node 与用 Set 存 int 有数倍内存差。Redis 的小对象编码（intset / listpack / ziplist / embstr）在容量账里能省多少？什么条件下会"悄悄"退回重型编码，导致容量估算失准？

**答**：
- **结论**：Redis 每个 value 按"小而专用"优先选编码：小整数集合用 intset（每元素 4-8 字节 + 无指针），小 hash/zset/list 用 listpack（7.0 取代 ziplist，连续内存无指针），短字符串用 embstr。容量账意义：同为 1 万元素，intset 约 40KB 级，而 hashtable 编码的 set 每元素要走 dict entry（约 3 倍以上）。但编码有**隐式退化条件**：元素数超 `*-max-*` 配置（如 128/512）、单元素超 64 字节、有元素被改为非整数、`HSET` 大字段——任一触发就整表转 hashtable/listpack，且**多数不会转回来**（`OBJECT ENCODING` 可查）。所以容量估算必须按"最坏编码"算，不能按配置文件里的理想值算。7.x 的 listpack 将转换阈值集中到 `list-max-listpack-*`/`hash-max-listpack-*`，8.x 延续。
- **取舍**：为了吃编码红利把大值拆小（字段分桶、ID 保持整数）会牺牲读模式的简洁（一次 HGETALL 变多次）；反向操作是把 listpack 阈值调大（如 512→1024），CPU 查找 O(n) 换内存——小对象才划算，单表上千字段是负优化。诊断顺序：先 `OBJECT ENCODING key` 看实际编码，再谈优化，别对着配置猜。
- **实战**：① 容量账用"退化后编码 × 1.5 安全系数"，监控里对 TOP 内存 key 抽样记录 encoding；② 批量写入的 key 最易踩退化：先写小后补大字段会固化 hashtable；③ `MEMORY USAGE key`（含 `SAMPLES` 参数）是账面工具；④ Python 侧 redis-py 用 `memory_usage()` / `object('encoding', key)` 做巡检脚本。

```python
# Redis 小对象编码 vs 重型编码的内存账模型 (数值为演示量级)
# 基线: Python 3.9+ 标准库; 线上用 redis-py 的 object('encoding', key) 核实
from dataclasses import dataclass


@dataclass
class EncodingModel:
    n: int
    elem_bytes: int          # 编码后每元素字节
    overhead_per_elem: int   # 重型编码的 dict/指针开销
    is_compact: bool

    def bytes_(self) -> int:
        per = self.elem_bytes if self.is_compact \
            else self.elem_bytes + self.overhead_per_elem
        return per * self.n


def encoding_for(n: int, max_entries: int, max_elem_bytes: int,
                 elem_bytes: int, all_ints: bool) -> str:
    """编码判定: 任一阈值突破即退化 (多数不可逆)。"""
    if all_ints and n <= max_entries:
        return "intset"
    if n <= max_entries and elem_bytes <= max_elem_bytes:
        return "listpack"
    return "hashtable"


def main() -> None:
    # 1 万元素 ID 列表: 紧凑 vs 退化后的账
    compact = EncodingModel(10_000, 8, 0, True)
    heavy = EncodingModel(10_000, 8, 24, False)
    ratio = heavy.bytes_() / compact.bytes_()
    assert ratio >= 3, ratio                      # 退化后 3 倍以上
    assert encoding_for(100, 128, 64, 8, True) == "intset"
    # 混入一个非整数元素 -> 整表转 hashtable, 不可逆
    assert encoding_for(100, 128, 64, 8, False) == "listpack"
    assert encoding_for(200, 128, 64, 8, True) == "hashtable"
    print(f"1万元素: 紧凑 {compact.bytes_() // 1024}KB vs "
          f"退化 {heavy.bytes_() // 1024}KB (x{ratio:.1f})")
    print("OK: 容量按最坏编码 x1.5 计; 用 OBJECT ENCODING 抽样核实退化")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么 listpack 在 7.0 取代 ziplist？
→ 一句话提示：ziplist 的连锁更新（prevlen 字段级联改写）在中间插入时是 O(n²) 隐患，listpack 每个节点只记自身长度，去掉 prevlen 彻底消除级联。

**追问 2**：intset 什么时候会退化，退化后还能回去吗？
→ 一句话提示：混入非整数或元素数超 set-max-intset-entries 即转 hashtable；编码升级单向，删除超限元素也不会自动降回，只能重建 key。

## 背诵要点
- 编码红利量级：intset/listpack vs hashtable 相差 3 倍以上；阈值 = 元素数（128/512 量级）+ 单元素 64 字节 + 全整数。
- 退化单向不可逆（多数情况），容量账必须按最坏编码 × 1.5 安全系数。
- 巡检三板斧：`OBJECT ENCODING`、`MEMORY USAGE`、redis-py `object('encoding', key)`。

## 复盘追问
- 一条 key 内存从 40KB 涨到 5MB，排查路径？提示：先看 encoding 是否退化，再看是元素数突破还是混入非整数/大字段，最后决定拆桶还是重建。
- 把 list-max-listpack-* 调到 1024 会付出什么？提示：listpack 查找 O(n)，读多的大列表 CPU 上升；小 key 省内存、大 key 是负优化。
