---
title: [AGT-858] 依赖升级（尤其 breaking change）用 Agent 自动化，流程与安全网怎么设计？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-858：依赖升级（尤其 breaking change）用 Agent 自动化，流程与安全网怎么设计

**答**：
- Agent 升级流程：检测（新版+breaking 变更摘要）→ 影响面分析（哪些包用到变更的 API）→ 自动适配（Agent 改代码+跑测试）→ 分批 PR（每依赖一个 PR，标注 breaking 点与改动）→ 合并策略（全绿自动合，存疑人工）。
- 安全网：升级 PR 必须带行为回归（关键路径 E2E），比单测更能抓住 breaking；锁文件与 semver 策略不动（Agent 不改版本策略）。
- 回滚预案：升级后 N 天内的错误率监控挂钩（错误激增自动提示回滚该依赖）。

```javascript
async function autoUpgrade(dep) {
  const breaking = await changelog.breaking(dep);
  const files = usageScan(dep, breaking.apis);     // 影响面
  const pr = await agent.adapt(files, breaking);
  pr.addChecks({
    unit: affectedTests(files),
    e2e: CRITICAL_PATHS,                           // 行为回归
  });
  monitor.link(pr, { metric: 'errorRate', window: '7d',
    onSpike: () => suggestRevert(dep) });          // 回滚挂钩
  return pr;
}
```

