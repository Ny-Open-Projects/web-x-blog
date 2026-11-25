---
title: [WCN-816] 组件平台如何与 SRE 协作定义 SLO 和错误预算？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-816：组件平台如何与 SRE 协作定义 SLO 和错误预算？

**答**：
- 结论先行：SLO（服务等级目标）是「用户体验的量化承诺」，错误预算是「允许犯错的额度」——两者把「组件稳不稳」从主观感受变成可执行的发布闸门。
- 定义 SLI（指标）：组件加载成功率、注册成功率、交互事件失败率、首屏渲染耗时——选真正影响用户的信号，而非「服务器 CPU」这种内部指标。
- 定 SLO：如「组件加载成功率 ≥ 99.9%（月度）」，由 SRE 与平台共同商定，参考历史基线与业务容忍度，别一拍脑袋定 99.99%。
- 用错误预算治理：预算充足时可加快发布与创新；预算耗尽时冻结非必要发布、优先修稳定性——这让「快」与「稳」有客观裁决依据。
- WC 特殊点：组件是分发到业务方页面运行的，平台无法直接控制宿主——要通过监控 SDK 回传真实环境的 SLI，并在 SLO 中明确「平台可控部分」（如 CDN 可用性、组件自身错误）与「宿主责任部分」的边界。
- 追问钩子：面试官会问「组件在宿主里崩了算谁的」——答：用可观测数据归因——若错误来自组件自身代码则算平台预算，若来自宿主注入的非法参数则算宿主，边界写进 SLA。

```javascript
// 错误预算计算：30 天窗口，99.9% 目标
function errorBudget({ totalRequests, slo = 0.999 }) {
  const allowedErrors = Math.floor(totalRequests * (1 - slo));
  return { allowedErrors, burned: 0, remaining: allowedErrors };
}
function canShip(budget, currentErrors) {
  return currentErrors < budget.allowedErrors; // 预算未耗尽才允许发布
}
const budget = errorBudget({ totalRequests: 1_000_000 });
console.log('允许错误数:', budget.allowedErrors, '可发布:', canShip(budget, 800));
```
