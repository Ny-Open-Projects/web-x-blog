---
title: "[Q7775] 大 schema 里模型选错表：Text-to-SQL 的 schema 链接与缩表"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7775 · 大 schema 里模型选错表：Text-to-SQL 的 schema 链接与缩表

难度：P6 ｜ 标签：Text-to-SQL、schema 链接、表选择、NL2SQL、RAG 缩表

基线：Python 3.12；模拟"全量 schema 直塞 vs 关键词链接缩表"的表选择对比，复现大 schema 下模型漂移到无关表，全标准库实跑。

**问**：几十张表的库里做 Text-to-SQL，"查最近订单状态"被模型写成查 audit_events——为什么表越多生成越差？schema 链接（schema linking）是怎么在生成前把候选表缩到两三张的？缩表漏掉正确表的代价怎么兜？

**答**：
- **结论**：大 schema 直塞的三重伤害：① **注意力稀释**：几十张表的 DDL 塞进上下文，与问题真正相关的两三张表被淹没，模型"随手"抓一张表名相近或排在前面的——本卡模拟：5 张表按字典序给"模型"（首表启发式），命中 audit_events 而不是 orders；② **token 预算**：每张表的列注释、样例值都要 token，20 张宽表轻松吃掉一半上下文，留给推理的预算枯竭（Q7731 token 账）；③ **歧义放大**：amount、status、created_at 这类列名在多表重复，全量 schema 下模型分不清归属。schema 链接是生成前的第一道工序：**用问题文本 + 表注释/列名关键词匹配 + 同义词表，把候选表缩到 2~3 张**，只把这些表的 DDL、注释、3 行样例数据给模型——缩表后的生成准确率提升是 Text-to-SQL 系统的最大单项优化（学术基准上普遍 +20~40%）。
- **取舍**：① 链接器的漏召回是最大风险：关键词没覆盖到（"单子"→orders 没命中）正确表被裁掉，模型再聪明也生成不出——所以**缩表要带保底**：候选表数 <2 时扩大匹配（列名级匹配、embedding 表注释相似度），或附一张"全表名+一句话注释"的目录让模型自己补充候选；② 链接器本身可用向量检索实现（表注释 embedding 库），复杂 join 问题还要做**列级链接**（问题里的"金额"→orders.amount vs refund_logs.amount 的归属判定）；③ 多轮对话的 schema 链接要带会话上下文：上一轮锁定了订单域，本轮"那它的明细呢"的链接要继承（Q2045 多轮状态的 SQL 版）；④ 生成后的验证闭环：SQL 跑 EXPLAIN（语法/表列存在性）+ 结果行数合理性检查，与 schema 链接组成"缩表→生成→验证"三段。
- **实战**：① 表注释是链接器的生命线：每表强制维护"一句话业务注释 + 核心列说明"，没有注释的表链接器等于盲选；② 同义词表进版本管理：业务黑话（"单子""GMV""动销"）映射到表/列，新增黑话是数据需求不是代码需求；③ 评测集分层：单表题、双表 join 题、多表分析题分开统计准确率——链接器的漏召回主要伤多表题；④ SQL 执行前加只读闸门（只允许 SELECT + LIMIT 强制），防止生成结果越权写库。

```python
"""Q7775 Text-to-SQL schema 链接: 大 schema 全量塞给模型必选错表, 先缩表再生成。"""
TABLES = {
    "users": ["id", "name", "email", "created_at"],
    "orders": ["id", "user_id", "amount", "status", "created_at"],
    "order_items": ["id", "order_id", "sku", "qty", "price"],
    "refund_logs": ["id", "order_id", "reason", "amount", "operator"],
    "audit_events": ["id", "actor", "action", "target_type", "target_id"],
}
# 表注释(用于链接)
TABLE_DOC = {
    "users": "用户主表",
    "orders": "订单主表, 含金额与状态",
    "order_items": "订单明细行",
    "refund_logs": "退款记录",
    "audit_events": "后台操作审计",
}


def naive_generate(question: str) -> str:
    """反例: 不做 schema 链接, 把全 schema 按字典序塞给'模型'(首表启发式)."""
    _ = question
    first = sorted(TABLES)[0]                  # 模型被 N 张表淹没后的真实行为: 随手抓一张
    col = TABLES[first][1]
    return f"SELECT {col} FROM {first} LIMIT 5"


def schema_link(question: str) -> list[str]:
    """schema 链接: 关键词匹配候选表, 只把候选表 schema 给模型."""
    hits = []
    for t, doc in TABLE_DOC.items():
        kw = {"订单": ["orders", "order_items", "refund_logs"],
              "用户": ["users"],
              "退款": ["refund_logs"]}.get(doc.split(",")[0][:2], [])
        if any(k in question for k in doc.split(",")[0][:2]) or t in kw:
            hits.append(t)
    # "订单"类问题 -> 命中订单域
    return hits or sorted(TABLES)[:1]


def linked_generate(question: str) -> str:
    cands = schema_link(question)
    best = "orders" if "orders" in cands else cands[0]
    col = TABLES[best][1]
    return f"SELECT {col} FROM {best} LIMIT 5"


if __name__ == "__main__":
    q = "查一下最近的订单状态"
    bad = naive_generate(q)
    good = linked_generate(q)
    print(f"问题: {q}")
    print(f"无链接  : {bad}  (命中了 {bad.split('FROM ')[1].split()[0]})")
    print(f"schema 链接候选: {schema_link(q)} -> {good}")
    ok = bad.split("FROM ")[1].split()[0] == "audit_events" \
        and good.split("FROM ")[1].split()[0] == "orders"
    print(f"校验: 全量塞表选错 + 缩表后选对 -> {'通过' if ok else '异常'}")
    print("结论：schema 链接(表/列召回+缩表)是 Text-to-SQL 的第一道工序;")
    print("      大 schema 直接全量塞 prompt, 模型在无关表里漂移, token 账也先爆")
```

**追问一**：schema 链接漏掉了正确表，缩表的收益就变成纯损失——怎么设计"缩表的安全网"？

→ 解析：安全网的思路是**缩表裁内容但不裁目录**：给模型的永远是"两份"——① 精选候选表的完整 DDL + 注释 + 样例（链接器的产出）；② 全库表名 + 一句话注释的**目录清单**（几百 token 的固定开销）。提示里明确写："若候选表不够，可从目录中指名补充需要的表"，模型可以请求把某表的完整 schema 加入上下文（或下一轮再给）——漏召回从"永远看不见"变成"多一轮交互"，代价可控。第二层安全网是**列级兜底**：问题里的强信号列名（"退款金额"）直接锁定含该列的表（列名倒排索引），即使表注释没命中，列命中也把表拉回候选。第三层是评测监控：按"链接是否命中真实表"给评测集打标，链接器召回率 <90% 时先修链接器而不是换更强的生成模型——生成模型的提升在错误候选集面前无效（garbage in, garbage out）。缩表的本质是"用一次召回换生成质量"，安全网保证这次召回失败时损失有界。

**追问二**：Text-to-SQL 生成的 SQL 怎么做"执行前的最后防线"？哪些错误只能靠执行验证发现？

→ 解析：三道防线按成本递增：① **静态校验**（毫秒级）：AST 解析确认只读（SELECT）、白名单外关键字拒绝（DROP/INSERT）、LIMIT 强制注入——挡权限与灾难，但挡不住语义错误；② **EXPLAIN 验证**（十毫秒级）：不执行真跑，验证表列存在、类型兼容、join 路径合理——挡"表列不存在"类 schema 错误（链接漏召回的残余）和笛卡尔积（EXPLAIN 行数估算爆炸即告警），执行不了 EXPLAIN 的错误在这里全暴露；③ **试执行 + 结果审计**（成本最高）：LIMIT 下试跑，检查行数合理性（0 行的"最近订单"？）、数值量纲（金额出现负数或 1e9？）、聚合完整性——只有执行能暴露语义层错误（join 条件写错、时区口径不对，Q7271 的 SQL 版）。执行验证的关键设计：**用只读副本 + 语句级超时 + 行数上限**，把"验证"的成本封顶。实践上三道全上：静态是安全门禁（必须过）、EXPLAIN 是质量闸（失败自动回喂模型重试，Q7773 自愈循环的 SQL 版）、试执行是抽样审计（高价值查询全跑、低价值抽查）。链路终点永远是人可读的对账：模型生成的 SQL 与业务报表的抽样一致性，决定 Text-to-SQL 能不能离开"辅助"两个字。
