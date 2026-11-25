---
title: [Q7669] Agent 定时巡检任务调度密度容量账
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7669 · Agent 定时巡检任务调度密度容量账：500 个巡检 Agent 挤在同一分钟

难度：P6-P7 | 标签：容量规划、调度、Agent 运维

**问**：500 个 Agent 定时巡检任务（监控数据源、清理过期记忆、生成日报）都配在整点触发，导致整分钟内 LLM API 并发超限、任务互相挤压且后端库被巡检查询打满。巡检任务的调度密度容量账怎么算？"错峰"怎么工程化而不是手工改 cron？

**答**：结论：巡检密度的账是三维乘积：**任务数 × 单任务资源（token/DB 查询/内存）× 时间密度**。整点齐发的问题是把"日总量"没有问题的工作负载集中成"分钟峰值"——账要按峰值算：峰值并发 = 每分钟触发任务数 × 单任务时长 / 60s × 重试放大。工程化错峰三件套：① 触发时间打散（哈希 key 取模分桶到窗口内随机时刻）；② 全局并发闸门（调度器层 semaphore，超出排队）；③ 优先级分档（核心巡检优先，报表类让路）。

取舍与实战：
1. 打散公式：`trigger = slot_start + hash(task_id) % window_seconds`——确定性哈希保证同一任务每次落在相同偏移（可预期、可解释），比纯随机更利于排查；窗口大小 = 任务数 × 单任务时长 / 允许并发。
2. 全局闸门是兜底不是主策略：仅靠闸门会造成排队积压与到期拥挤（Q7143 leader 选举防重跑解决的是"重复执行"，本卡解决"密度"，两者正交都要有）。
3. LLM 巡检的 token 预算单独记账：巡检类调用量稳定可预测（任务数 × 频率 × 每 token），用独立 API key/预算池（Q7582），避免巡检流量与用户流量抢配额——巡检可以限流降级，用户流量不能。
4. 重试放大要入账：巡检失败重试 3 次 = 密度 ×3；重试也要进闸门与打散（重试时刻再次哈希分桶），否则失败潮会自我放大（Q7665 429 风暴同构）。

```python
"""巡检调度打散与全局并发闸门（标准库演示，可运行）"""
import hashlib, threading, time

def jittered_trigger(task_id: str, slot_epoch: int, window_s: int = 900) -> int:
    """确定性打散：同一任务同一窗口恒定偏移"""
    h = hashlib.sha256(f"{task_id}:{slot_epoch}".encode()).digest()
    return slot_epoch + int.from_bytes(h[:4], "big") % window_s

class ConcurrencyGate:
    def __init__(self, limit: int):
        self.sem = threading.BoundedSemaphore(limit)

    def run(self, task_id: str, fn):
        with self.sem:                        # 全局闸门：超出即排队
            return fn(task_id)

# 500 个任务打散到 15 分钟窗口，验证峰值密度
tasks = [f"inspect-{i}" for i in range(500)]
slot = int(time.time()) // 900 * 900
triggers = [jittered_trigger(t, slot) for t in tasks]
per_min = max((triggers.count(slot + m * 60) for m in range(15)), default=0)
print(f"窗口内每分钟最多触发: {per_min} 个（均分期望 ~33）")
assert per_min < 100
gate = ConcurrencyGate(limit=10)
done = gate.run("inspect-0", lambda tid: f"done:{tid}")
print(done)
```

**追问 1**：为什么"确定性哈希打散"优于"每次随机延迟"？
**提示**：确定性偏移让巡检时刻可预测可复现（排查"任务为什么 02:37 跑"有据可查），且重启用同一 key 重算即得相同调度，不引入新扰动；纯随机让调度时间不可审计。

**追问 2**：闸门排队导致的"任务迟到"怎么处理，巡检超时还有意义吗？
**提示**：巡检大多容忍分钟级延迟但要设 deadline 超过即跳过本次并记录（stale 数据比重复执行危害小）；高优先级巡检用独立闸门池，与报表类隔离，避免被低优任务排到超时。

## 背诵要点
- 巡检账按峰值算：峰值并发 = 每分钟触发数 × 单任务时长 × 重试放大；日总量没问题≠分钟峰值没问题。
- 错峰三件套：确定性哈希打散（任务+窗口 key）、全局并发闸门兜底、优先级分档隔离。
- 巡检 LLM 流量独立预算池，可降级；重试也进闸门与打散，防失败潮自我放大。

## 复盘追问
- 如何从调度日志反推"整点齐发"的实际峰值并发，验证打散前后的账差？
- 巡检任务 deadline 跳过后，下游对"本次巡检缺失"的感知机制（staleness 标记）怎么设计？
