---
title: [Q7685] Batch API 半价窗口与吞吐容量账
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7685 · Batch API 半价但等 24 小时：批处理窗口与吞吐的容量账

难度：P6 ｜ 标签：容量规划、Batch API、时效与吞吐
基线：OpenAI Batch API（50% 折扣，24h 窗口）；Anthropic Message Batches（类似模型）。

**问**：离线打标签任务每天 50 万条，实时 API 成本扛不住，同事说"换 Batch API 半价就完了"。切过去之后业务方投诉"标签晚一天出"。Batch API 的容量账怎么算？哪些负载适合、哪些不适合？

**答**：**结论**：Batch API 的账核心是**完成时效是概率而非 SLA**：官方承诺 24 小时窗口，实测常在 1-2 小时内完成，但高峰期可能拖满窗口——把它当"次日必达"用就是事故。容量账三个维度：① **价格维度**——50% 折扣 ×（输入+输出都打折），50 万条/日 → 月省 50% API 费；② **时效维度**——SLA 敏感（用户在等）的负载不能走 Batch，SLA 以天计的（离线画像、评测集、历史数据回填）全量收益；③ **吞吐维度**——Batch 的单文件 5 万条/批次上限与并发 batch 数，大批量要分片提交并管理 batch 状态机（submitted→in_progress→completed/failed）。混部策略：**分级时效路由**——实时走同步 API，日级走 Batch，小时级走"实时 API 限速池"，三档各配预算。

**取舍**：Batch 的隐性成本是**失败处理复杂度**：单条失败在结果文件里带 error 字段，要设计重试批（失败的 5% 重新组批再提交一轮），两轮后仍失败的走实时兜底或人工——这层状态机代码不写清楚，"省一半钱"会变成"漏 5% 数据的工单"。另一取舍是缓存收益：Batch 内重复 prompt 不吃实时服务的 prompt 缓存（各批独立计费），重复度高的负载要先去重。

**实战**：批处理分片与状态机管理账（标准库）：

```python
# Batch API 容量账：分片提交、状态机与时效路由
import time
from enum import Enum

MAX_PER_FILE = 50_000
TOTAL_DAILY = 500_000
RT_PRICE, BATCH_DISCOUNT = 1.0, 0.5

daily_cost_rt = TOTAL_DAILY * RT_PRICE
daily_cost_b = TOTAL_DAILY * RT_PRICE * BATCH_DISCOUNT
print(f"实时: {daily_cost_rt:,.0f} 元/日 vs Batch: {daily_cost_b:,.0f} 元/日 "
      f"（月省 {(daily_cost_rt-daily_cost_b)*30:,.0f} 元）")

class BatchState(str, Enum):
    SUBMITTED = "submitted"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

def submit_shards(items: list[str]) -> list[dict]:
    """按 5 万条/批分片提交，返回 batch 清单。"""
    batches = []
    for i in range(0, len(items), MAX_PER_FILE):
        batches.append({
            "id": f"b_{i // MAX_PER_FILE}",
            "state": BatchState.SUBMITTED,
            "size": min(MAX_PER_FILE, len(items) - i),
            "submitted_at": time.time(),
        })
    return batches

shards = submit_shards([f"doc{i}" for i in range(TOTAL_DAILY)])
print(f"每日 {TOTAL_DAILY:,} 条 -> {len(shards)} 个 batch 分片")

# 时效路由：按 SLA 分级
SLA_ROUTE = {
    "用户在等（秒级）": "同步 API（全价）",
    "小时级报表": "实时 API 限速池",
    "次日离线标签": "Batch API（半价）",
}
for k, v in SLA_ROUTE.items():
    print(f"  {k} -> {v}")

# 失败重试账：5% 失败的两轮策略
fail_rate = 0.05
retry1 = TOTAL_DAILY * fail_rate
retry2 = retry1 * 0.1                    # 二轮失败率大降
manual = retry2 * 0.2
print(f"\n失败链: 一轮重试 {retry1:,.0f} 条 -> 二轮 {retry2:,.0f} 条 "
      f"-> 人工兜底 {manual:,.0f} 条/日")
print(f"重试批的额外成本: {(retry1+retry2)*RT_PRICE*BATCH_DISCOUNT:,.0f} 元/日（已含折扣）")
```

**追问 1**：Batch 的 24h 窗口过了还没完成会怎样？设计上怎么兜底？
提示：超窗口 batch 被取消（部分结果保留）；兜底是"截止时间检查 + 未完成部分转实时 API 限速池补齐"，时效承诺按 24h+缓冲规划而非实测均值。

**追问 2**：为什么 Batch 里重复 prompt 吃不到实时服务的 prompt 缓存折扣？
提示：缓存按请求上下文在服务端预热复用，Batch 各请求独立计价且调度分散；重复度高的负载先在客户端去重（同 prompt 只提交一次、结果回填）。

**追问 3**：离线回填历史数据（百万级）走 Batch 的账与在线标签有什么不同？
提示：回填无时效压力可全量 Batch 且可打断重跑，重点是幂等键（文档 hash 作为请求 custom_id）防重复计费；在线标签的账重点在时效路由与失败重试链。

## 背诵要点
1. Batch API 半价但完成时效是概率（24h 窗口非 SLA）：用户在等的负载禁用；账 = 半价收益 ×（时效可容忍度）。
2. 单文件 5 万条上限，大批量分片提交 + 状态机管理；失败要设计两轮重试批 + 人工兜底链，否则省一半钱换漏 5% 数据。
3. 时效三级路由：同步 API（秒级）/ 实时限速池（小时级）/ Batch（日级）；Batch 内重复 prompt 不吃实时缓存，先去重。

## 复盘追问
1. "标签晚一天出"的 SLA 当时是谁拍板的？业务方的时效需求有没有被结构化地收集过（而不是事后投诉）？
2. 失败重试链上线后跑过全量演练吗？人工兜底的 0.x% 每天谁在处理，工单闭环如何度量？
