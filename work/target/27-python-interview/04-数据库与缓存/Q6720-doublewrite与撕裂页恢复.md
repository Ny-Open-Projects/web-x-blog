---
title: "[Q6720] doublewrite：16KB 页只写了一半怎么恢复"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6720 · doublewrite：16KB 页只写了一半怎么恢复

难度：P7 ｜ 标签：InnoDB、doublewrite、torn page、崩溃恢复

基线：Python 3.12；MySQL 8.0 InnoDB doublewrite；纯 Python 模拟撕裂页与恢复。

**问**：数据库跑在普通云盘上，一次断电后 InnoDB 启动报 `Database page corruption`，几个 16KB 的数据页校验失败。redo log 不是能恢复吗？为什么 redo 救不了这几个页？doublewrite 在其中做了什么？

**答**：
- **结论**：磁盘的原子写单位通常小于 InnoDB 页（16KB），断电可能只写入页的前半部分，形成 **torn page（撕裂页）**。redo 是**物理逻辑日志**，重放前提是页本身结构完整、LSN 对得上；半新半旧的页连校验都过不了，redo 无法在其上重放。**doublewrite** 的做法是：刷页前先把整页顺序写到 doublewrite 区域并 fsync，再写到真实数据文件；崩溃恢复时先用 doublewrite 里的完整副本还原撕裂页，再重放 redo。
- **取舍**：doublewrite 带来**双倍写放大**（每页写两次）和额外 fsync，但它是崩溃安全的底线。8.0.20+ 支持独立的 doublewrite 文件、批量刷写，降低对 buffer pool 的阻塞；某些支持原子写的存储/文件系统理论上可关，但云盘大多不承诺 16KB 原子写，生产不建议关。SSD 上 doublewrite 的成本主要是带宽与延迟，不是磁盘寻道。
- **实战**：① 不要为了写性能关闭 `innodb_doublewrite`，除非存储明确保证原子写并做过断电演练；② 监控 `Innodb_dblwr_pages_written` 与 `Innodb_dblwr_writes`，比例异常说明刷页模式变化；③ 定期做 `innodb_force_recovery` 演练与备份恢复演练；④ 云盘关注 IOPS/带宽是否被 doublewrite 放大打满。

```python
PAGE_SIZE = 16 * 1024


def write_page(offset: int, data: bytes, torn_at: int | None = None) -> bytes:
    """模拟落盘：torn_at 表示只写入了前 N 字节就断电。"""
    page = bytearray(PAGE_SIZE)
    n = PAGE_SIZE if torn_at is None else torn_at
    page[:n] = data[:n]
    return bytes(page)


def recover(page: bytes, expected: bytes, copy: bytes | None) -> str:
    if page == expected:
        return "page_ok"
    if copy == expected:
        return "restored_from_doublewrite"   # 先用副本还原，再重放 redo
    return "corrupt"                          # 没有完整基线页，redo 无法重放


if __name__ == "__main__":
    data = bytes([7]) * PAGE_SIZE
    torn = write_page(0, data, torn_at=PAGE_SIZE // 2)
    print("无 doublewrite:", recover(torn, data, None))
    print("有 doublewrite:", recover(torn, data, data))
    print("结论：redo 依赖完整页，doublewrite 先把撕裂页还原成可重放的页")
```

**追问一**：为什么 redo log 不能直接把半页覆盖成完整页？
→ 解析：redo 记录的是"对某个页做了什么修改"（物理位置 + 逻辑操作），重放需要页的基线版本与 LSN 正确。半页既不是旧版本也不是新版本，页头/校验/索引结构都可能损坏，重放会写坏更多数据。doublewrite 提供的是"完整基线页"，redo 才能接上。

**追问二**：doublewrite 和 binlog 都叫"写两份"，它们解决的是同一个问题吗？
→ 解析：不是。doublewrite 解决**单机页级崩溃一致性**（防止 torn page），是 InnoDB 内部的物理副本；binlog 解决**复制与时间点恢复**（逻辑变更流），用于从库同步和 PITR。两者层次、格式、用途都不同，不能互相替代。
