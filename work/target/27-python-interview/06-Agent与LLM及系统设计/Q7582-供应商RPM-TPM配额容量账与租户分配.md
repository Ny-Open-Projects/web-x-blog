---
title: [Q7582] 供应商 RPM/TPM 配额容量账与租户分配
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7582 · 供应商 RPM/TPM 配额的容量账与租户分配

难度：P7 ｜ 标签：LLM 网关 / 配额 / 容量规划

**问**：LLM 供应商给的是按组织计的 RPM（每分钟请求数）与 TPM（每分钟 token 数）配额。接入租户增多后 429 频发。这套配额怎么建模成容量账？租户间怎么分配？

**答**：
- **结论**：供应商配额本质是"双维度令牌桶"：请求维度（RPM）与 token 维度（TPM，且 prompt+completion 都计），二者独立限流先到先限。容量账建模：`并发承载 = min(RPM/平均RPS需求, TPM/平均TPS需求)`；关键不等式是 TPM/RPM = 平均每请求 token 数——当业务请求平均 token 高于配额隐含均值时，TPM 先爆；反之 RPM 先爆。租户分配则是在共享配额上做多租户公平：静态切分（每租户子令牌桶）防止互相挤占，但整体利用率低（A 空闲 B 饿死）；动态加权公平队列（按租户权重 loan 配额）利用率高但实现复杂且要有租户级观测。
- **取舍**：静态子桶 vs 动态公平队列：租户少（<20）且 SLA 明确用静态子桶 + 借用上限（空闲租户可被借用 50%）；租户多且长尾大用动态队列。超售比（oversubscription）：配额利用率实际只有 40-60%（白天低谷），可以按 1.5-2 倍超售多个供应商通道，代价是高峰的排队延迟与 429 重试成本。
- **实战**：落地：① 网关层对每租户维护两个本地令牌桶（RPM/TPM），本地预限流而不是等 429——429 再重试的吞吐损失远大于预限流；② TPM 预估用 prompt token 计数（tiktoken/各家 tokenizer）在请求前判定"这发必超"直接排队；③ 观测按租户出"配额利用率 × 429 率"矩阵，指导扩容申请与权重调整；④ 多供应商通道按成本/配额做路由（参考成本路由卡）。

```python
# 双维度令牌桶 + 租户子桶预限流（纯标准库）
# 基线：Python 3.9+

from dataclasses import dataclass


@dataclass
class DualTokenBucket:
    rpm: int
    tpm: int
    req_tokens: float = 0.0   # RPM 剩余
    tok_tokens: float = 0.0   # TPM 剩余

    def allow(self, est_tokens: int) -> tuple[bool, str]:
        if self.req_tokens < 1:
            return False, "RPM 耗尽"
        if self.tok_tokens < est_tokens:
            return False, f"TPM 不足(需{est_tokens})"
        self.req_tokens -= 1
        self.tok_tokens -= est_tokens
        return True, "ok"


def implied_avg_tokens(rpm: int, tpm: int) -> int:
    return tpm // rpm  # 配额隐含的平均每请求 token 数


def main() -> None:
    rpm, tpm = 500, 200_000
    print("配额隐含均值:", implied_avg_tokens(rpm, tpm))  # 400 tok/req
    # 业务均 800 tok/req：TPM 先爆
    bucket = DualTokenBucket(rpm, tpm, req_tokens=rpm, tok_tokens=tpm)
    results = [bucket.allow(800) for _ in range(300)]
    tpm_exhaust = sum(1 for ok, _ in results if not ok and "TPM" in _)
    print(f"300 请求中 TPM 拒绝 {tpm_exhaust} 个")
    assert tpm_exhaust > 100  # TPM 是先爆的维度

    # 租户静态子桶 + 50% 借用
    tenants = {"a": DualTokenBucket(rpm // 2, tpm // 2, rpm // 2, tpm // 2),
               "b": DualTokenBucket(rpm // 2, tpm // 2, rpm // 2, tpm // 2)}
    ok, msg = tenants["a"].allow(400)
    print("租户a:", ok, msg)
    assert ok


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"收到 429 再重试"的方案吞吐损失大？
→ 一句话提示：429 意味着请求已计入供应商侧压力且重试窗口按响应头/指数退避拉长，配合并发风暴会放大抖动；本地预限流把排队前置，吞吐平稳且省重试 token。

**追问 2**：TPM 预估不准（completion 长度未知）怎么办？
→ 一句话提示：按 prompt 精确 + completion 用 P95 历史值预算，扣减时"预算扣减-完成后对账回补"，多扣少补保证不越限。

## 背诵要点
- 双维令牌桶：RPM 与 TPM 独立限流，先到先限；判据是业务均 token vs 配额隐含均值（TPM/RPM）。
- 预限流优先于 429 重试；TPM 预估 = prompt 精确 + completion P95，完成后对账回补。
- 租户分配：<20 租户用静态子桶 + 50% 借用；长尾大用动态加权公平队列；可按 1.5-2 倍超售多通道。

## 复盘追问
- 为什么配额利用率只有 40-60%？提示：请求在时间上不均匀（高峰集中在分钟级脉冲），分钟桶模型下峰值利用率天然受限，这正是超售与多通道路由的空间。
- 供应商扩容申请要带什么数据？提示：租户级 RPM/TPM 利用率矩阵、429 率与排队延迟分布、业务增长的 token 预测曲线。
