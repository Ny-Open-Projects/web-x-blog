---
title: [1121] Agent 链路能像代码一样「断点调试」吗
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 调试]
type: 面试题
---

## 1121：Agent 链路能像代码一样「断点调试」吗

**答**：
- 可以，设计要点：编排器支持「暂停点」声明（在某 Agent 执行前后暂停），暂停时导出当前上下文/黑板状态；调试器 REPL 可检查、修改状态后继续——这就是 Agent 的断点调试。
- 修改后继续的价值：验证假设（「把这个错误工具结果改成正确的，后面会不会走对」）——是归因的利器，比改代码重跑快得多。
- 实现基础：确定性重放（同输入同路径）+ 状态快照序列化——没有这两个，断点调试无从谈起。
- 追问钩子：生产环境怎么用？——只读模式（只看不改）+ 沙箱 fork（复制一份状态到沙箱试改），生产严禁在线改状态。

```ts
const debug = orchestrator.debugSession(taskId, {
  breakpoints: ['after:searcher', 'before:coder'],
  mode: 'sandbox-fork',                     // 生产安全：沙箱试改
});
await debug.pause();                        // 命中断点
debug.watch('blackboard');
debug.set('searcher.result', corrected);    // 修改假设验证
await debug.resume();                       // 继续观察后续行为
```

