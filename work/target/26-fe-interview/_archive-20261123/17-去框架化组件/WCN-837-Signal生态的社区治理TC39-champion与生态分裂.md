---
title: [WCN-837] Signals 生态的「社区治理」怎么看？（TC39 Champion、SIG、生态分裂）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-837：Signals 生态的「社区治理」怎么看？（TC39 Champion、SIG、生态分裂）

**答**：
- 结论先行：Signals 是罕见地由「多框架厂商共同推动标准化」的提案（Preact/Solid/Vue/Angular 等参与），治理目标是「统一底层语义、保留框架调度自由」——理解治理能判断技术路线风险。
- 角色分工：TC39 champion 推动提案分阶段（Stage 0→4）；框架团队通过信号实现与反馈影响设计；SIG/工作组聚焦互操作与 polyfill 对齐。
- 生态分裂风险：各库早期 API 不一（signal()/createSignal/Signal.State）、相等性与调度语义不同——标准化的价值就是收敛这些差异，让跨库共享成为可能。
- 工程决策：不要押注单一库，依赖抽象层；关注提案 Stage 与 breaking changes；优先选与标准对齐的实现（如 signal-polyfill），降低未来迁移成本。
- 追问钩子：面试官会问「标准会不会阉割框架特性」——答：提案刻意只定义核心语义（值、依赖、Watch），把调度、批处理、生命周期留给框架，所以框架自由度仍在——这是多方差妥协的结果。

```javascript
// 用适配层 + 特性探测应对生态分裂与标准演进
function resolveSignalImpl() {
  if (globalThis.Signal?.State) return 'tc39';   // 原生标准
  try { require.resolve('signal-polyfill'); return 'polyfill'; } catch {}
  return 'legacy';                                // 退化为项目内实现
}
const IMPL = resolveSignalImpl();
const adapters = {
  tc39:     { make: v => { const s = new Signal.State(v); return { get: () => s.get(), set: n => s.set(n) }; } },
  polyfill: { make: v => { const s = new (require('signal-polyfill').Signal.State)(v); return { get: () => s.get(), set: n => s.set(n) }; } },
  legacy:   { make: v => ({ value: v, get() { return this.value; }, set(n) { this.value = n; } }) },
};
const s = adapters[IMPL].make(0);
```
