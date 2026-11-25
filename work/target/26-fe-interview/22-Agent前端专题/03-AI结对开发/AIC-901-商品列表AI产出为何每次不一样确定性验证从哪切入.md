---
title: [AIC-901] 商品列表让 AI 生成的价格计算逻辑「这次和上次结果不一样」，确定性验证从哪里切入？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-901：商品列表让 AI 生成的价格计算逻辑「这次和上次结果不一样」，确定性验证从哪里切入？
**答**：
- 先区分「不确定性来源」：模型 temperature/top_p、模型版本、上下文顺序、外部依赖（时间/随机/接口）都会让输出漂移——结论：先归类再治理，别笼统说「AI 不稳定」。
- 工程手段固定可控项：temperature=0、锁定模型版本号（不用 latest）、上下文按稳定顺序拼装、把时间/随机数/ID 通过参数注入而非让 AI 自己取。
- 验证靠「同输入多次运行指纹一致」：对同一需求跑 N 次，归一化（去时间戳/id/空白）后比对哈希，不一致就报警。
- 追问钩子：能说出「不确定性分为模型侧与工程侧，工程侧可完全消除、模型侧用交叉验证容忍」的候选人，理解了确定性不是消灭随机而是管理随机。

```typescript
// 确定性验证：同输入多次运行，归一化后比指纹
function fingerprint(code) {
  const normalized = code
    .replace(/\d{4}-\d{2}-\d{2}T[\d:.]+Z?/g, '<TIME>')   // 抹掉时间戳
    .replace(/\b[0-9a-f]{8,}\b/gi, '<ID>')              // 抹掉随机 id
    .replace(/\s+/g, ' ').trim();
  let h = 0;
  for (const c of normalized) h = (h * 31 + c.charCodeAt(0)) | 0;
  return h >>> 0;
}
function verifyDeterminism(run, input, times = 5) {
  const prints = new Set();
  for (let i = 0; i < times; i++) prints.add(fingerprint(run(input, { temperature: 0, seed: 42 })));
  return { stable: prints.size === 1, distinct: prints.size };
}
// stable=true 说明工程侧可控项已固定；false 则先查模型版本/上下文顺序
```
