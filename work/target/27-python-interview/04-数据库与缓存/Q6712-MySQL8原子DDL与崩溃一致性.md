---
title: "[Q6712] MySQL 8.0 原子 DDL：DDL 崩在中间怎么办"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6712 · MySQL 8.0 原子 DDL：DDL 崩在中间怎么办

难度：P7 ｜ 标签：MySQL 8.0、原子 DDL、数据字典、崩溃恢复

基线：Python 3.12；MySQL 8.0 原子 DDL；纯 Python 模拟 DDL 日志的提交/回滚。

**问**：给一张 800 万行的表加索引，DDL 执行到 70% 时实例被 OOM kill。5.7 时代重启后遇到过"表结构变了但数据没重建完"、"临时表残留"、"数据字典和 InnoDB 不一致"的烂摊子；8.0 说支持原子 DDL，它到底保证了什么？是不是 DDL 就不会失败了？

**答**：
- **结论**：8.0 的原子 DDL 把**数据字典更新、存储引擎操作、binlog 写入**纳入一个原子单元，并通过 **DDL log** 记录进度。崩溃恢复时，未提交的 DDL 要么整体前滚、要么整体回滚，不会留下"字典已改、数据没改"的半成品。它保证的是**元数据与数据的一致性**，不是"DDL 一定成功"或"DDL 瞬间完成"。
- **取舍**：原子 DDL 不等于无锁、无阻塞：`ALTER TABLE` 仍要拿 MDL，长事务会阻塞 DDL，DDL 又会阻塞后续查询；大表 rebuild 仍要占磁盘（新旧表空间并存）和 IO；DDL 在从库是串行重放，主库 10 分钟的 DDL 可能让从库延迟更久。所以生产仍要用 gh-ost/pt-osc 做在线变更，或选低峰窗口。
- **实战**：① 变更前查 `information_schema.innodb_trx` 的长事务，避免 MDL 等待雪崩；② 大表 DDL 评估磁盘余量（重建期间双份空间）与从库延迟；③ 用 `ALGORITHM=INPLACE/INSTANT` 显式声明期望，不支持就失败而不是偷偷 copy；④ 原子 DDL 只保一致性，回滚仍要靠备份/反向 DDL。

```python
def run_ddl(atomic: bool, crash_at: str) -> dict[str, object]:
    """模拟数据字典(dict)与表数据(data)在 DDL 各阶段的可见状态。"""
    state = {"dict": "old", "data": "old", "temp": False}
    stages = ["begin", "dict_update", "rebuild", "commit"]
    for stage in stages:
        if stage == "dict_update":
            state["dict"] = "new"
            state["temp"] = True
        elif stage == "rebuild":
            state["data"] = "new"
        elif stage == "commit":
            state["temp"] = False
            return {"state": state, "result": "committed"}
        if stage == crash_at:
            if atomic:
                # DDL log 回滚：字典与数据一起回到旧状态
                return {"state": {"dict": "old", "data": "old", "temp": False},
                        "result": "rolled_back"}
            return {"state": state, "result": "partial"}
    return {"state": state, "result": "unknown"}


if __name__ == "__main__":
    for atomic in (False, True):
        print(f"atomic={atomic} crash@rebuild:", run_ddl(atomic, "rebuild"))
    print("结论：原子 DDL 消除半成品，但不消除 MDL 等待、磁盘与从库延迟")
```

**追问一**：原子 DDL 能保证 DDL 和 binlog 一致吗？
→ 解析：8.0 把 DDL 的 binlog 写入纳入原子提交，崩溃后不会出现"库上改了、binlog 没记"或反之；但**主从复制**仍是异步的，从库执行同一 DDL 时可能失败（版本差异、对象不存在），需要 `slave_skip_errors` 之外的修复流程。

**追问二**：为什么 `ALTER TABLE ... ADD INDEX` 在 8.0 仍可能锁表？
→ 解析：是否锁表取决于 `ALGORITHM` 与操作类型。加索引通常支持 INPLACE（不阻塞 DML，但开始/结束要短暂 MDL），加列在 8.0.12+ 支持 INSTANT；而改列类型、改字符集往往要 COPY，全程阻塞写。原子 DDL 解决的是崩溃一致性，不改变这些算法约束。
