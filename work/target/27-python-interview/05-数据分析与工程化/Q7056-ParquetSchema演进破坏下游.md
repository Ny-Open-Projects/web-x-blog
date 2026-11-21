---
title: [Q7056] Parquet schema 演进破坏下游的事故复盘
date: 2026-11-20
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7056 · Parquet schema 演进破坏下游的事故复盘

难度：P6 | 标签：schema 演进、数据格式、兼容性、事故复盘

**问**：上游把 `amount_cents int` 改名成 `amount_yuan float64`，任务"成功"，下游报表金额全部变成 0 或量级错乱。文件格式不是支持 schema evolution 吗，为什么还是炸了？哪些演进安全、哪些是破坏性的？

**答**：
- **结论**：Parquet 支持的是"物理层演进"（加列、某些类型加宽），不等于"语义层兼容"——下游按旧列名读，改名后的列读不到，pandas 静默补 NaN、SQL 补 NULL 或直接 KeyError，任务照常"成功"，坏数据流到报表才被人发现。安全的演进只有两类：加可选列（带默认值）、整数类型向宽加宽（int32→int64）；破坏性的四类：改名（=删列+加列）、类型收窄或语义变更（int 分→float 元）、删列、分区列变更。规则必须进 schema 注册表：写侧每次变更先过兼容检查，读侧对缺失列显式声明默认值，禁止静默 NaN。
- **取舍**：改名确有必要时走"双写期"：新旧两列并存 N 天，下游全部迁完再删旧列——这和 API 的 deprecation 窗口同构。有人主张"读侧写兼容 shim 自动映射旧列名"——短期止血可以，长期会积累一张"别名映射表"没人敢删，正确归宿还是注册表里的显式版本。
- **实战**：落地清单：① 写侧 CI 校验：数据集 schema diff 报告（新增/删除/类型变更），破坏性变更需下游 owner 会签；② 读侧防御：读时断言列集合符合期望版本，不符合即失败（fail fast 优于静默错数）；③ 单位进列名（amount_cents/amount_yuan），让"语义变更"在 diff 里显形。

```python
"""Parquet schema 演进事故：类型升级与改名如何把下游读崩，兼容规则清单。"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Schema:
    version: int
    fields: dict[str, type]

V1 = Schema(1, {"order_id": int, "amount_cents": int})
V2 = Schema(2, {"order_id": int, "amount_cents": int, "channel": str})   # 安全演进
V3 = Schema(3, {"order_id": int, "amount_yuan": float})                  # 改名+换类型

def check_compatible(old: Schema, new: Schema) -> list[str]:
    """下游按 old 读、文件按 new 写时的破坏面检查。"""
    breaks = []
    for f, t in old.fields.items():
        if f not in new.fields:
            breaks.append(f"列消失(或被改名): {f} —— 下游 KeyError/静默补空")
        elif new.fields[f] is not t:
            breaks.append(f"类型变更: {f} {t.__name__}->{new.fields[f].__name__} —— 语义/精度可能漂移")
    for f in new.fields:
        if f not in old.fields and f != "channel":
            breaks.append(f"新增列未声明默认值: {f}")
    return breaks

print("V1 -> V2（加列，向后兼容）：", check_compatible(V1, V2) or "无破坏")
print("V1 -> V3（改名+类型升级）：")
for b in check_compatible(V1, V3):
    print("   ", b)

def read_column(rows: list[dict], col: str, default: int | None = None):
    """下游读取：显式默认值优于静默 None。"""
    return [r.get(col, default) for r in rows]

rows_v3 = [{"order_id": 1, "amount_yuan": 12.5}]
print("下游读 amount_cents:", read_column(rows_v3, "amount_cents", default=0),
      "—— 静默补 0，金额报表就此失真")
print("治理：schema 变更走注册表审批（只允许加列/带默认值），"
      "读侧用显式默认值并断言版本，改名视为破坏性变更走双写期")
```

**追问链**：
1. 追问一层：为什么"任务成功"但数据是错的这类事故最难发现？——schema 不兼容在读取层表现为默认值/None 而非异常，管道的监控盯的是任务退出码与行数，行数没变、退出码 0，一切绿灯；错数据在下游报表被人肉发现时已经污染了 N 天。防线是把"列集合与类型断言"做成读取层的硬失败。
2. 追问二层：int32→int64 为什么安全、int 分→float 元为什么不安全？——前者是纯加宽：所有旧值在新类型下表示不变；后者同时改了类型与语义（单位），旧值按新语义解读全部错 100 倍，且 float 的二进制表示让"看起来还像金额"——这类"能跑但错"的演进比直接报错更危险。

**背诵要点**：
1. Parquet 的 schema evolution 是物理层能力，语义兼容要自己管：加列安全，改名/删列/类型语义变更是破坏性的。
2. 读侧 fail fast：断言列集合与版本，显式默认值，禁止静默 NaN。
3. 改名走双写期；单位写进列名让语义变更在 diff 里显形。

**复盘追问**：
1. 为什么这事故在下游报表才发现而不是 ETL 层？（ETL 的校验只有行数与退出码，没有 schema 断言；把 schema 校验做成读取层硬失败，事故在第一跳就被拦住）
2. "双写期"的退出条件怎么定才不会拖成永久双写？（下游 owner 会签迁移清单 + 读旧列流量归零监控，两个条件同时满足才删列；拖成永久双写的根因是没有"旧列读流量"指标）
