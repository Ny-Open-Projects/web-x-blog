---
title: [AGT-854] Monorepo 几百个包，AI 编码助手的上下文怎么喂（包依赖图/影响面/精选上下文）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-854：Monorepo 几百个包，AI 编码助手的上下文怎么喂（包依赖图/影响面/精选上下文）

**答**：
- 上下文按「任务影响面」精选：先用包依赖图算出受影响包集合，只喂相关包的接口签名+目标文件全文，而不是整个 repo——上下文质量决定 AI 产出质量。
- 仓库级知识文件分层：根级 ARCHITECTURE.md（全局约束）+ 包级 README（约定）+ 任务级相关代码；AI 工具按层加载（rules 工程化，AGT/AIC 系列联动）。
- 影响 Sage：AI 改动后自动跑 affected 测试（构建编排器的 affected 计算），AI 的改动与人类改动同权进流水线。

```javascript
function buildAIContext(task) {
  const affected = depGraph.affectedOf(task.files);  // 影响面包
  return [
    loadRoot('ARCHITECTURE.md'),                     // 全局约束
    ...affected.map(p => loadInterfaces(p)),         // 接口签名
    ...task.files.map(f => loadFull(f)),             // 目标全文
  ].join('\n---\n');
}
function aiAffectedCheck(pr) {
  return buildAffected(pr.changedFiles);             // 与人类同权
}
```

