---
title: "[Q7242] 同一个字段先是 int 后是「15ms」：索引模板冲突，整批日志被拒"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7242 · 同一个字段先是 int 后是 "15ms"：索引模板冲突，整批日志被拒

难度：P7 ｜ 标签：结构化日志、动态映射、ES mapping、schema 漂移

基线：Python 3.12；用"字段首次出现定类型、后续不匹配即冲突"的模型模拟 Elasticsearch/ClickHouse 的动态 schema。

**问**：JSON 日志里的 `latency_ms` 大部分是 `12`，某次发版后有个服务改成 `"15ms"`（带单位）。上线当天日志平台报 `mapper_parsing_exception: failed to parse field [latency_ms] of type [long]`，这批日志整条被拒；运维把索引模板改成 `keyword` 后不报错了，但延迟看板的 P99 查询全是 0。字段只是换了个格式，为什么影响这么大？

**答**：
- **结论**：日志平台（ES 动态映射、ClickHouse 的列类型、BigQuery 的 schema）都是**写入时定类型、之后不可改**：第一个文档决定了 `latency_ms` 是 `long`，后续写入 `"15ms"` 无法解析 → 整条文档被拒（默认 `ignore_malformed=false`）。改成 `keyword` 能写进去了，但字符串的字典序比较不等于数值比较（`"9" > "12"`），范围查询/分位数聚合全错，看板自然归零。根因不在平台，在**生产端把"带单位的展示字符串"塞进了数值字段**。
- **取舍**：① 生产端强制类型：`latency_ms` 永远是整数毫秒，展示单位由前端加；原始值另存 `latency_raw: keyword`；② 索引模板显式声明字段类型（`long`/`double`/`keyword`），关掉动态映射（`dynamic: strict` 或 `false`），让"新字段/错类型"在写入时暴露而不是污染 mapping；③ 必须兼容脏数据时用 `ignore_malformed: true` + `_ignored` 字段，把坏文档捞出来而不是静默丢；④ 多版本并存期用"双写新字段 + 旧字段保留"过渡，别原地改语义。
- **实战**：① 日志字段要有 schema（名字、类型、单位、是否可空），和埋点一样版本化；② CI 里用样例日志跑一遍目标平台的 mapping 校验（或本地 `_simulate` API）；③ 监控"被拒文档数 / 总量"，超过阈值告警——这次事故的第一信号其实是拒写率，不是看板归零；④ 分位数、求和这类聚合字段一律数值型，单位写进字段名（`latency_ms`、`size_bytes`）。

```python
"""动态映射：首个文档定类型，后续类型漂移导致拒写或查询失真。"""
class MappingConflict(Exception):
    pass


TYPE_MAP = {int: "long", float: "double", str: "keyword", bool: "boolean"}


class Index:
    def __init__(self, strict: bool = True) -> None:
        self.mapping: dict[str, str] = {}
        self.docs: list[dict] = []
        self.rejected = 0
        self.coerced = 0
        self.strict = strict

    def index(self, doc: dict) -> None:
        doc = dict(doc)
        for key, value in doc.items():
            ftype = TYPE_MAP.get(type(value), "object")
            known = self.mapping.get(key)
            if known is None:
                self.mapping[key] = ftype
            elif known != ftype:
                if self.strict:
                    self.rejected += 1
                    raise MappingConflict(
                        f"failed to parse field [{key}] of type [{known}]: {value!r}"
                    )
                self.coerced += 1
                self.mapping[key] = "keyword"     # 降级成全字符串
                doc[key] = str(value)
        self.docs.append(doc)

    def range_query(self, field: str, gt: float) -> list[dict]:
        ftype = self.mapping[field]
        if ftype in ("long", "double"):
            return [d for d in self.docs if d[field] > gt]
        # keyword：统一转字符串比较，数值语义已丢失
        return [d for d in self.docs if str(d[field]) > str(gt)]


if __name__ == "__main__":
    base = {"ts": "2026-11-24T10:00:00Z", "trace_id": "t-1"}

    strict = Index(strict=True)
    strict.index({**base, "latency_ms": 12})
    strict.index({**base, "latency_ms": 30})
    print("strict 已写入:", len(strict.docs), "| mapping:", strict.mapping)
    try:
        strict.index({**base, "latency_ms": "15ms"})
    except MappingConflict as e:
        print("strict 拒写:", e, "| 被拒数:", strict.rejected)

    lenient = Index(strict=False)
    lenient.index({**base, "latency_ms": 12})
    lenient.index({**base, "latency_ms": 9})
    lenient.index({**base, "latency_ms": "15ms"})
    print("\nlenient mapping:", lenient.mapping, "| 降级次数:", lenient.coerced)
    print("文档:", [d["latency_ms"] for d in lenient.docs])
    print("latency_ms > 10 命中:", [d["latency_ms"] for d in lenient.range_query("latency_ms", 10)])
    print("  -> 字典序下 '9' > '10'，'15ms' 也混进了结果，数值语义已经丢了")

    # 正确姿势：数值字段 + 原始值分列，模板显式声明类型
    fixed = Index(strict=True)
    fixed.index({**base, "latency_ms": 12, "latency_raw": "12ms"})
    fixed.index({**base, "latency_ms": 9, "latency_raw": "9ms"})
    print("\n分列后 > 10 命中:", [d["latency_ms"] for d in fixed.range_query("latency_ms", 10)])
    print("结论：写入前定类型；展示字符串与数值分列；动态映射要显式关掉")
```

**追问一**：设了 `dynamic: strict` 为什么还是可能出问题？

→ 解析：`strict` 只保证"**不在模板里的字段**写入时报错"，它不保护"同一字段在不同索引/不同版本里类型不同"。日志平台通常按天建索引，`logs-2026.11.23` mapping 是 `long`、`logs-2026.11.24` 还是 `long`，但如果中间有人手动改过模板，或者写到了别名指向的旧索引，查询跨索引时就会 `field type mismatch`。真正要守的是**索引模板版本化 + 变更走审批 + 别名只指向已对齐的索引**，并把"跨索引字段类型一致性"做成巡检项。

**追问二**：已经写坏的字段怎么迁移？

→ 解析：不能原地改类型（ES 要 reindex，ClickHouse 要改表）。路径是"新字段 + 双写 + 回填 + 切看板 + 删旧字段"：① 生产端同时写 `latency_ms`（数值）与 `latency_ms_v2`（数值，语义不变但强制类型）；② reindex 历史数据，把 `"15ms"` 解析成 `15`（解析规则必须显式，不能 `int("15ms")`）；③ 看板切到新字段，观察一个发布周期；④ 最后删旧字段与旧代码。期间两套字段并存，schema 文档要标注 deprecate 时间点，否则半年后没人知道该用哪个。
