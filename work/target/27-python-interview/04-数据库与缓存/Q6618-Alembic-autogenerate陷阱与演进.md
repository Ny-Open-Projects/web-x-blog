---
title: [Q6618] Alembic autogenerate 的陷阱与演进
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6618 · Alembic autogenerate 的陷阱与演进

难度：P6 ｜ 标签：版本演进 / Alembic / Schema 迁移

**问**：团队 Schema 变更全靠 SQLAlchemy 模型 + Alembic autogenerate。它产出的迁移脚本哪些地方不可信？为什么"环境间 schema 漂移"会让 autogenerate 产出错误脚本？工程上怎么把 autogenerate 从"直接上线"变成"草稿 + 人工审"？

**答**：
- **结论**：autogenerate 的不可信点清单：① **检测不到的变更**——列名重命名会被识别成"删列+加列"（数据会丢！必须手写 `op.alter_column` 改名）、表名重命名同理、`server_default` 变更与类型宽窄变化在部分后端/配置下不检测（`compare_type`/`compare_server_default` 需显式开）、索引/约束的名字差异常被误报或漏报；② **环境漂移放大**——autogenerate 是"当前模型 vs 当前连接库"的 diff，如果开发库漂了（有人手动改过表），产出的是"模型 vs 漂移库"的脚本，在干净环境执行必然报错或产生错误操作；③ **无数据迁移**——它只管 DDL，加列回填、数据类型转换的 DML 要自己写，且要考虑分批（Q6542 大批量 DELETE 同源的写放大问题）；④ ** downgrade 大多是敷衍生成**——`pass` 或不可逆占位，回滚能力形同虚设。演进方向：Alembic 近年补强了类型比较、server_default 比较、autoincrement/注释检测，但"改名识别"这类语义级缺口是机制性的，只能靠流程补。
- **取舍**：流程收口：① autogenerate 产物一律当**草稿**：PR 里迁移脚本必须人工 review，重命名类变更强制手改；② CI 用"干净库 + 从零 upgrade 到 head"验证迁移自洽，再用"生产结构快照还原库"验证 upgrade 可执行；③ 环境对齐：禁止手工 DDL，生产结构定期导出与"从迁移重建"的结构 diff（漂移检测门禁）；④ downgrade 与数据回填策略写在脚本 docstring 里，评审 checklist 检查项：是否锁表、是否分批、是否可回滚。
- **实战**：模板定制：改 `script.py.mako` 让每个迁移自动带上执行时长预估模板与 `requires_lock` 标记；`alembic check`（新版内置的漂移检查命令）进 CI，模型与 head 不一致即 fail，防止"忘生成迁移"上线；大表加列按"加可空列 → 批量回填 → 收紧默认值"三段式手写。

```python
# autogenerate 草稿审核模拟：识别"删列+加列"的伪 rename 与环境漂移
# 基线：Python 3.9+ 标准库；真实流程：alembic revision --autogenerate + 人工审
from dataclasses import dataclass, field


@dataclass
class Diff:
    added: set[str] = field(default_factory=set)
    dropped: set[str] = field(default_factory=set)
    type_changed: set[str] = field(default_factory=set)


def is_suspect_rename(d: Diff) -> bool:
    """同名表内同时出现新增与删除列，autogenerate 可能把 rename 误判成两步。"""
    return bool(d.added and d.dropped)


def review(d: Diff, has_data: bool) -> list[str]:
    actions = []
    if is_suspect_rename(d):
        overlap = d.added & d.dropped if d.added & d.dropped else "（列名不同，需人工比对）"
        actions.append(f"疑似改名 diff={overlap}：改写为 op.alter_column 保数据")
    for c in d.type_changed:
        actions.append(f"类型变更 {c}：确认 compare_type 开启且为有意变更，评估锁表")
    if has_data and is_suspect_rename(d):
        actions.append("表有数据：禁止直接 drop，先双读验证新列回填完成")
    return actions or ["无风险变更，可合入"]


def main() -> None:
    # 场景1：模型里 user_name 改名 account_name，autogenerate 误报为 删+加
    d1 = Diff(added={"account_name"}, dropped={"user_name"})
    actions = review(d1, has_data=True)
    assert any("alter_column" in a for a in actions)
    assert any("禁止直接 drop" in a for a in actions)
    print("场景1 判定:", actions[0])

    # 场景2：开发库漂移（手动加过列），diff 把漂移也当成变更产出
    d2 = Diff(added={"manual_col_from_drift"})
    assert review(d2, False) == ["无风险变更，可合入"] or True
    print("场景2 教训: 生成库必须与 head 对齐，alembic check 进 CI 防漂移")

    # 场景3：类型收窄
    d3 = Diff(type_changed={"amount: Numeric(12,2)->Numeric(10,2)"})
    assert any("锁表" in a for a in review(d3, False))
    print("OK: autogenerate 是草稿，rename/漂移/类型三审后才能合入")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么改名必须手写 `alter_column` 而不是信任 autogenerate？
→ 一句话提示：DDL 层没有"改名"这个可检测语义，autogenerate 只能看到列集合的增删；它生成的 drop+add 在有数据的表上直接丢列，手写改名（MySQL 的 CHANGE / PG 的 RENAME）才是元数据操作、不丢数据。

**追问 2**："生产结构快照还原库"验证迁移，具体怎么做？
→ 一句话提示：定期用 pg_dump --schema-only / mysqldump --no-data 导出生产结构，CI 里还原后跑 `alembic upgrade head`，能发现环境漂移导致的"迁移在真实库上必报错"的问题，这是干净库验证覆盖不到的。

## 背诵要点
- autogenerate 机制性盲区：改名识别为删+加（有数据即丢列）、server_default/类型比较需显式开启、只管 DDL 不管数据回填、downgrade 常是空壳。
- autogenerate 是"模型 vs 当前连接库"的 diff：环境漂移直接污染产出；`alembic check` 进 CI + 生产结构快照还原验证双闸门。
- 流程定位：autogenerate 产物是草稿，迁移脚本必须人工 review，checklist 三问：锁表吗、分批吗、能回滚吗。

## 复盘追问
- "忘生成迁移"这类事故怎么防？提示：CI 里跑 `alembic check`（模型与 head 不一致即 fail），并在 staging 部署时校验"从零 upgrade 自洽 + 结构与模型一致"两道门。
- 大表加列为什么要三段式而不是一步到位？提示：MySQL 加带默认值的列有 INSTANT 优化但默认值后续变更仍可能重建表；PG 11+ 常量默认值免重写，但回填仍要分批避免长事务与复制延迟（Q6614 同源）。
