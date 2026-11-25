---
title: "[Q6760] 物理备份恢复的原理账：拷页 + redo 前滚到备份时点"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6760 · 物理备份恢复的原理账：拷页 + redo 前滚到备份时点

难度：P7 ｜ 标签：MySQL、物理备份、redo 前滚、恢复原理、崩溃恢复

基线：Python 3.12；用页字典 + redo 日志模拟"拷贝时刻不一致的页 + 前滚修复"的全过程。

**问**：逻辑备份（mysqldump）跑 4 小时太慢，改用物理备份（XtraBackup 类）几十分钟拷完。物理备份是"把数据目录整个拷走"，可备份持续几十分钟，拷到的数据页必然是不一致的——有人提交了一半、有的页拷到一半，为什么恢复出来是完整的？恢复时那一步"apply log"到底在做什么？

**答**：
- **结论**：物理备份每个数据页都带 **LSN（日志序号）**，redo 日志按序记录每次修改。恢复分两步：① 把备份时刻拷来的**混乱但页内自检的页**当作"某个过去的混乱现场"；② 从备份记录的起始 LSN 起**重放 redo 到备份结束时刻**——新于备份页的修改被补上、页内可能损坏的半成品被 redo 前滚重写。这和崩溃恢复（实例断电后重启）是同一套机制：**redo 保证已提交事务不丢（前滚），undo 回滚未提交事务**。物理备份快是因为只做"顺序拷贝文件 + 记录日志位点"，不解析 SQL、不构建行。
- **取舍**：① 物理备份必须含**备份期间的 redo 日志**，redo 生成快的实例要给 xtrabackup 流程留足磁盘（Q6580 的 pg_wal/redo 容量账同理）；② 恢复耗时 = 拷回文件 + redo 前滚，redo 积压越大恢复越慢，RTO 要把这段算进去（Q6563）；③ 逻辑备份可跨版本/跨实例选择性恢复单表，物理备份基本要求同版本同配置整库恢复——灵活性换速度；④ 物理备份文件含全部数据，存储加密与访问控制要按生产数据级别管理。
- **实战**：① 备份完成后必须做"恢复演练级"验证（Q2018 的备份可用性验证），至少启动临时实例并校验行数/校验和；② 生产库与备份机版本、参数（页大小、字符集）必须一致，恢复前先 `--prepare` 把 redo 前滚到一致点；③ 演练记录真实 RTO 并与预案对齐；④ 恢复出的实例自增/序列状态随物理页而来，通常比逻辑备份更接近主库——但仍要核对（Q6622）。

```python
"""物理备份恢复模拟：拷页(带LSN) + redo 前滚到备份结束点 + undo 回滚未提交。"""
import copy

LSN_END = 0            # 备份结束时的 redo 位置，由备份工具记录


def build_state() -> tuple[dict, list, list]:
    """返回 (页字典: page->(data,lsn), redo日志: [(lsn,page,op,val)],
    未提交事务的行)。"""
    pages = {"p1": ("balance=100", 10), "p2": ("count=5", 20)}
    redo = [(30, "p1", "balance", 150),        # T1 提交：拷页后发生的修改
            (40, "p2", "count", 6)]            # T2 未提交，undo 阶段回滚
    return pages, redo, [("T2", "p2")]


def restore(pages: dict, redo: list, uncommitted: list) -> dict:
    pages = copy.deepcopy(pages)
    applied = 0
    for lsn, page, key, val in redo:           # redo 前滚到备份结束点
        old, _ = pages[page]
        new_data = old.replace(key.split("=")[0] + "=", f"{key.split('=')[0]}={val}") \
            if key.split("=")[0] in old else old
        pages[page] = (new_data, lsn)
        applied += 1
    # undo：未提交事务的修改从页里抹掉（这里以 T2 为例回滚）
    rolled = {p for _, p in uncommitted}
    for p in rolled:
        data, lsn = pages[p]
        pages[p] = (data.replace("count=6", "count=5"), lsn)
    print(f"  redo 前滚: {applied} 条已提交日志补写 -> 页与备份结束点一致")
    print(f"  undo 回滚: {len(rolled)} 个未提交事务的修改被抹掉")
    return pages


if __name__ == "__main__":
    pages, redo, uncommitted = build_state()
    LSN_END = max(l for l, *_ in redo)
    print("备份拷到的混乱现场（页内 LSN 落后于 redo）:")
    for p, (data, lsn) in pages.items():
        print(f"  {p}: {data}  @LSN {lsn}")
    print("\n恢复过程:")
    final = restore(pages, redo, uncommitted)
    print("\n恢复结果:")
    for p, (data, lsn) in sorted(final.items()):
        print(f"  {p}: {data}  @LSN {lsn}")
    ok = final["p1"][0] == "balance=150" and final["p2"][0] == "count=5"
    print(f"\n一致性校验: T1 已提交修改保留={'balance=150' in final['p1'][0]}"
          f" | T2 未提交修改清除={final['p2'][0] == 'count=5'} -> {'一致' if ok else '异常'}")
    print("结论：拷页不一致没关系，redo 前滚+undo 回滚把现场收敛到备份结束时刻")
    print("      RTO = 拷回文件 + redo 前滚，备份期间的 redo 量直接决定恢复时长")
```

**追问一**：为什么"页拷到一半"不会把恢复搞坏？

→ 解析：拷贝工具按页为单位读取并校验页校验和（checksum），拷到半途的页要么校验失败被重拷、要么被 redo 前滚重写覆盖——InnoDB 的双写机制（Q6720）保证磁盘上的页要么旧值要么新值、不会撕裂，备份工具读到的页同样满足"旧值完整或新值完整"。真正危险的不是页撕裂，而是**备份中途 DDL**：表结构在备份窗口变化会让某些页与新结构对不上，所以物理备份窗口内要冻结 DDL（变更冻结期，Q1474 的思路）。

**追问二**：恢复后的实例为什么还需要再做一次"崩溃恢复"？

→ 解析：备份结束点之后到"启动恢复实例"之间，如果直接把备份拷到生产环境并带着主库最后一段 binlog/redo 补齐（PITR，Q880），才会追到误操作前一刻；若只用备份本身，数据停在备份结束时刻。此外恢复实例首次启动时仍会执行一遍自己的崩溃恢复流程（对 --prepare 后仍残留的 undo 做清理）。所以完整的恢复链是：物理备份 → redo 前滚到备份点 →（可选）binlog 重放到目标时刻 → 启动自检 → 校验行数/校验和 → 切流量，每一步的耗时都要计入 RTO 的账。
