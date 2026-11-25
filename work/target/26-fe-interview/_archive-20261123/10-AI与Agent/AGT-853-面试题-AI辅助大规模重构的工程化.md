---
title: [AGT-853] 十万行的旧代码库要 AI 辅助重构（Vue2→Vue3），如何保证安全与可控？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-853：十万行的旧代码库要 AI 辅助重构（Vue2→Vue3），如何保证安全与可控

**答**：
- AI 重构的正确姿势是「codemod + AI 修正」而不是全量重写：确定性转换用 codemod（jscodeshift），AI 只处理 codemod 覆盖不了的语义等价改写（如 options API 转 composition 的复杂逻辑）。
- 分批小步：按模块分批（每批 ≤50 文件），每批跑全量测试+类型检查+视觉回归，失败即回滚该批；进度台账跟踪（已迁移/验证/失败清单）。
- AI 产出的 diff 必须可人工审：批量 PR 按模块拆分、每个 PR 带变更说明与测试证据，不搞万行巨 PR。

```javascript
async function aiRefactor(modules) {
  for (const mod of modules.slice(current, current + 50)) { // 小步分批
    const codemod = await runCodemod('vue2to3', mod);   // 确定性优先
    const aiPatch = await aiFixLeftovers(mod, codemod.report);
    const ok = await verify(mod, ['test', 'type', 'visual']);
    if (!ok) { await git.revert(mod); failures.push(mod); continue; }
    ledger.mark(mod, 'migrated');
  }
  return { progress: ledger.stats(), failures };
}
```

