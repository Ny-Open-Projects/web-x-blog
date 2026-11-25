---
title: [1049] 线上坏任务怎么「原样重放」复现问题
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 调试]
type: 面试题
---

## 1049：线上坏任务怎么「原样重放」复现问题

**答**：
- 重放前提是完整记录：任务输入、每轮模型调用（prompt/参数/响应）、工具调用与返回、环境快照（配置版本、模型版本、知识库版本）——缺任何一项重放就失真。
- 重放模式三种：精确重放（mock 全部外部依赖按录制返回，验证编排逻辑）、半重放（工具 mock、模型真调，定位模型行为变化）、全真重放（全部真调，复现环境类 bug）；按归因需要选。
- 时间与环境因素：重放要还原「当时」的模型版本与配置（trace 里记录版本号），今天重放上周任务用今天的模型，结论可能完全不同。
- 追问钩子：重放会重复副作用吗？——精确/半重放工具全 mock 无副作用；全真重放必须在沙箱环境且写类工具替换，这是硬规矩。

```ts
async function replay(taskId, mode) {
  const rec = await trace.load(taskId);            // 完整记录 + 环境版本
  env.bind({ model: rec.env.modelVer, config: rec.env.config }); // 还原当时环境
  const mocks = mode === 'exact' ? mockAll(rec)
    : mode === 'half' ? mockToolsOnly(rec) : sandboxedLive();
  return orchestrator.run(rec.input, { mocks, record: true });   // 与原 trace diff
}
```
