---
title: [RBL-856] 场景题：CI 构建任务的失败重试语义——重试什么、不重试什么
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-856：场景题：CI 构建任务的失败重试语义——重试什么、不重试什么

**答**:
- 重试的判定维度：失败类型决定重试价值——1) **瞬态失败**（网络抖动/registry 超时/runner 抢占）重试有效；2) **确定性失败**（代码错误/配置错误/断言失败）重试无意义（浪费分钟数还掩盖问题）；3) **flaky**（时序依赖/资源竞争）重试会通过但问题应入根因库（RBL-836）。分类器：错误指纹匹配已知模式（网络超时关键词/退出码/重试历史）。
- 重试的策略分层：任务级重试（CI 层 automatic retry，只对瞬态白名单开启）vs 步骤级重试（构建器内部的网络调用重试——粒度更细成本更低）；「重试上限 + 退避」防雪崩（全局失败时的指数退避 + 熔断）。
- 重试的副作用审查：重试任务的「产物一致性」——重试成功的产物与首次失败的差异（确定性构建 RBL-543 保证重试产物相同——不可复现的构建连重试都危险）。
- 重试的度量：重试成功率按失败类别统计——「网络类重试成功率高（值得）、代码错误类为 0（不该重试）」数据驱动调整白名单；重试率上升 = 环境退化信号。
- 追问钩子：为什么「确定性失败重试」比「不重试」更糟？——浪费 CI 分钟（×2 成本）且给开发者「也许再跑一次就好了」的错误心理暗示（掩盖代码问题延迟修复）；重试的价值必须来自「失败原因在两次间可能消失」（瞬态）——重试语义的本质是「对随机性的正确建模」，把确定性失败纳入重试 = 随机化确定性问题的处理。

```javascript
// 失败分类与重试策略
const RETRY_WHITELIST = [
  /ETIMEDOUT|ECONNRESET|502|503|registry.*timeout/i,   // 网络/registry
  /runner.*evicted|OOM(?!Leak)/i,                       // runner 瞬态（非代码 OOM）
];
const DETERMINISTIC = [
  /assert|expect|Cannot find module|SyntaxError|config.*invalid/i,
];
function shouldRetry(error, { attempts, maxAttempts = 2, history } = {}) {
  if (attempts >= maxAttempts) return false;
  const msg = String(error?.message ?? error);
  if (DETERMINISTIC.some(re => re.test(msg))) return false;       // 确定性失败不重试
  if (RETRY_WHITELIST.some(re => re.test(msg))) return true;
  // 未知错误：历史数据驱动（该指纹重试成功率 > 50% 才试）
  return (history?.successRate(errorFingerprint(msg)) ?? 0) > 0.5;
}
```
