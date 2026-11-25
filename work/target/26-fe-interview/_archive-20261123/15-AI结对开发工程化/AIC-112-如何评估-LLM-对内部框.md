---
title: [AIC-112] 如何评估 AI 工具对「内部框架/私有库」的支持质量？这决定了选型里什么权重？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-112：如何评估 AI 工具对「内部框架/私有库」的支持质量？这决定了选型里什么权重？
**答**：
- 为什么单独评估：模型对公开库（React 等）支持好是默认预期，但团队生产力大头在私有代码——内部框架支持差时，公开库的加成会被幻觉抵消。
- 评估方法：构造「内部框架基准任务集」——3~5 个用私有库完成的典型任务（建组件、调内部请求封装、用内部状态管理），测幻觉率（编造不存在的 API 比例）与一次通过率。
- 提升手段按有效性排序：上下文供给（贴 d.ts + 事实卡片）> MCP 接私有文档 > fine-tune（成本高收益不定）> 换模型（收效最小，因为私有数据它就是没见过）。
- 选型权重结论：私有支持能力应占选型权重 40%+（AIC-024 的能力维度细化），因为「对外补全好、对内幻觉多」的工具对存量业务是净伤害。
- 追问钩子：可复用的内部 API 事实卡片库是可迁移资产——换工具不用重建，这降低锁定的隐性成本。

```javascript
// 内部框架基准任务评测
const internalBench = [
  { task: '用 @corp/form 生成带校验的表单', expect: ['FieldRule', 'useFormState', 'SubmitBar'] },
  { task: '用 @corp/request 发起带重试的请求', expect: ['retryPolicy', 'interceptor'] },
];
async function evalInternal(tool) {
  const results = [];
  for (const b of internalBench) {
    const out = await tool.generate(b.task);
    const phantom = out.apis.filter(a => !b.expect.includes(a)); // 编造的 API
    results.push({ task: b.task, phantomCount: phantom.length });
  }
  return { hallucinationRate: sum(results.map(r => r.phantomCount)) / totalApis(results) };
}
```
