---
title: [AGT-879] 设计系统组件库大版本升级（弃用 props/新 API），AI 如何做迁移辅助与团队通知？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-879：设计系统组件库大版本升级（弃用 props/新 API），AI 如何做迁移辅助与团队通知

**答**：
- 升级知识包：组件库发布升级包（弃用清单/迁移映射/示例 diff），AI 迁移助手消费该包——AI 拿到的是结构化迁移知识而不是读 changelog 猜。
- 主动通知：repo 扫描发现使用弃用 API 的位置，自动开迁移 issue（带位置/建议改法/影响面），按团队分派。
- 双轨迁移：新代码 lint 阻断旧 API（增量不欠债），存量走 AI 迁移 PR 分批清——新债断源旧债清偿。

```javascript
const UPGRADE_KIT = {
  deprecated: [{ api: 'Button.type', instead: 'Button.variant' }],
  mapping: 'prop-mapping.json',
};
async function migrationPRs(kit) {
  const usages = await scanRepo(kit.deprecated);
  for (const team of groupByOwner(usages)) {
    await issues.create({ team, title: `组件库迁移：${team.count} 处`,
      body: ai.migrationGuide(usages, kit) });      // AI生成迁移指南
  }
  lint.block({ deprecated: kit.deprecated });       // 新代码阻断
  return batchPRs(ai.migrate(usages, kit.mapping), { perBatch: 20 });
}
```

