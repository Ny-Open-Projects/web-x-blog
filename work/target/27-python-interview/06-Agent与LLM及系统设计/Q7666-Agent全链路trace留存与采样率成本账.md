---
title: [Q7666] Agent 全链路 trace 留存与采样率成本账
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7666 · Agent 全链路 trace 留存与采样率成本账：观测数据比业务还贵

难度：P6-P7 | 标签：成本工程、可观测性、Agent

**问**：Agent 服务的 OpenTelemetry trace（每轮对话含全部 prompt/工具输出）三个月把观测平台的存储费推到月万元级，超过了 LLM API 费。观测成本账怎么算？采样率、留存周期、字段裁剪三者的账怎么平衡？事故排查时又不能没有 trace，怎么两全？

**答**：结论：Agent trace 的成本贵在**体积结构**：一次会话 = 1 个根 trace + N 轮 span，每轮含完整 prompt/补全文本（几 KB 到几百 KB），是普通 Web 请求 trace 的 100 倍量级。账的公式：月成本 = 请求数 × 每请求 span 数 × 平均 span 体积 × 采样率 × 留存单价。三个旋钮的杠杆排序：**字段裁剪（省 90%+）> 留存周期（线性）> 采样率**——先砍全量 prompt 落库，再分层留存，最后才是采样。

取舍与实战：
1. 分级留存（最重要）：全量文本（prompt/补全/工具输出）→ 热存 7 天（调试期）→ 归档冷存 30 天（S3 每月每 GB 不到 1 分钱）；结构化骨架（span 树、耗时、token 数、状态码）→ 留 90 天走指标/ cheapest 存储。事故排查 90% 只用骨架 + 7 天热文本，成本降一个数量级。
2. 采样策略按价值分层：错误/超时/慢会话 100% 采集（tail-based sampling），正常会话采 5-10%；Agent 会话价值不均——含工具失败的会话是排查金矿，优先保。
3. 字段裁剪红线：prompt 不全量存，存"长度 + 哈希 + 前 200 字符"；敏感字段脱敏（Q7510 出站审计）在采集层做，别让脱敏成本后移到存储。
4. 采样率不是万能旋钮：tail-based sampling 要缓冲完整会话再决策，缓冲内存本身是容量账（Q7627 SSE 句柄同类）；head sampling 省钱但丢错误会话，与 tail 组合用。

```python
"""观测成本账：span 体积 × 采样 × 留存分层（标准库，可运行）"""

def trace_cost_per_month(
    requests_per_day: int, spans_per_req: float,
    kb_per_span: float, sample_rate: float,
    hot_days: int, archive_days: int,
    hot_price_per_gb_month: float = 30.0,
    archive_price_per_gb_month: float = 0.02,
) -> dict:
    daily_gb = requests_per_day * spans_per_req * kb_per_span / 1024**2 * sample_rate
    hot_gb = daily_gb * hot_days
    archive_gb = daily_gb * archive_days
    cost = hot_gb * hot_price_per_gb_month + archive_gb * archive_price_per_gb_month
    return {"日增GB": round(daily_gb, 2), "月成本(元)": round(cost),
            "热存GB": round(hot_gb, 1), "归档GB": round(archive_gb, 1)}

full = trace_cost_per_month(50_000, 8, 40, 1.0, 30, 0)          # 全量文本全留存
tiered = trace_cost_per_month(50_000, 8, 0.5, 0.15, 7, 30)      # 裁剪+采样+分层
print("全量:", full)
print("分层:", tiered, "省:", f"{1 - tiered['月成本(元)'] / full['月成本(元)']:.1%}")
assert tiered["月成本(元)"] < full["月成本(元)"] / 10
```

**追问 1**：为什么"存哈希+前 200 字符"仍能支撑大多数排查？
**提示**：排查常问"这轮是否与上轮同 prompt"（哈希等值判断）、"prompt 是否异常膨胀"（长度）、"开头是否注入了什么"（前缀）——全文只在复现语义问题时才需要，而那时可用会话回放重新调模型生成（成本后移但按需）。

**追问 2**：tail-based sampling 的缓冲成本怎么算，什么规模下不再划算？
**提示**：要缓存完整会话（多分钟/多轮）才能决策，内存 = 并发会话数 × 会话 span 体积；会话超长或并发极高时缓冲成本反超收益，退化为 head sampling + 错误强制保真。

## 背诵要点
- Agent trace 是普通请求的 100 倍体积（全量 prompt/工具输出）；成本账 = 请求 × span × 体积 × 采样 × 留存单价。
- 杠杆排序：字段裁剪（prompt 存哈希+长度+前 200 字符，省 90%+）> 分层留存（文本 7 天热 + 30 天归档，骨架 90 天）> 采样率。
- 采样分层：错误/慢会话 100%（tail-based），正常 5-10%；head+tail 组合，缓冲内存进容量账。

## 复盘追问
- 如何用"排查事件回溯统计"验证 7 天热存是否足够（多少事故在第 8 天后才需要全文）？
- 脱敏在采集层做掉了，若后期新合规要求更强脱敏，已归档数据怎么办？
