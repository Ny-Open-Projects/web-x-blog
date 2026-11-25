---
title: [SCN-703] SLA/SLO/错误预算怎么定义？前端看板的指标从哪来？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-703：SLA 体系与错误预算怎么定义？
**答**：
- 概念链：SLI（指标，如页面 P95 加载时长）→ SLO（目标，P95 ≤ 2.5s 且达标率 99.9%）→ SLA（对外承诺 + 违约条款）。内部看板盯 SLO，对外合同才看 SLA。
- 错误预算：预算 = (1 - SLO) × 时间窗口内的允许错误量；预算烧完（burn rate 超标）触发「冻结功能发布、优先稳定性」的机制——这是 SLO 体系的核心行动价值。
- 前端 SLI 选择：用户侧指标（LCP/INP/JS 错误率/接口成功率）优先于技术指标；每个 SLI 必须有明确测量口径（采样率/分位数算法/数据来源）。
- 指标分层：页面级 → 服务级 → 用户体验级（ journeys），看板从体验级下钻到页面级。
- 追问钩子：为什么不用平均值做 SLI——平均值掩盖长尾（P95/P99 才代表糟糕体验），而且对异常值不敏感导致预算失真。

```javascript
const SLO = {
  sli: 'page_lcp_p95',           // 指标
  target: 2500,                  // ms
  compliance: 0.999,             // 达标率（时间窗口内 P95 达标的天数比例）
  window: '30d',
  errorBudget: (1 - 0.999) * 30 * 24 * 3600_000,  // 30 天窗口的错误预算 ms·时间
};
function burnRate(fastBurn, slowBurn) {
  // Google SRE 双窗口：快窗（1h）抓突发，慢窗（6h）防抖
  if (fastBurn > 14.4 && slowBurn > 6) return 'PAGE_SRE';        // 立即告警
  if (fastBurn > 6 && slowBurn > 3) return 'TICKET';
  return 'OK';
}
```
