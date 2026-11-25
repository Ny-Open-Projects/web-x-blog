---
title: [SCN-1232] AI 产品的计费与用量展示（token 消耗透明）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1232：AI 产品的计费与用量展示（token 消耗透明）

**答**：
- 展示：每次对话 token 用量（输入/输出/费用），会话累计与套餐余额。
- 预警：余额不足提醒（充值引导），用量超预期提示（长上下文警告）。
- 对账：用量明细导出（企业客户）。

```javascript
// 用量展示
function usagePanel(usage, balance) {
  return {
    thisMsg: { in: usage.inputTokens, out: usage.outputTokens,
      cost: +(usage.inputTokens * IN_PRICE + usage.outputTokens * OUT_PRICE).toFixed(4) },
    session: usage.sessionTokens,
    balance,
    warn: balance < 10 ? '余额不足，请充值' : null,
    longCtx: usage.inputTokens > 50_000 ? '上下文较长，费用较高' : null,
  };
}
```
