---
title: [AGT-851] AI 生成的代码（Copilot/Agent 产出）与人类代码混入仓库，CI 门禁要加什么？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-851：AI 生成的代码（Copilot/Agent 产出）与人类代码混入仓库，CI 门禁要加什么

**答**：
- 门槛不因 AI 降低：AI 代码走同一套 lint/类型/测试门禁，另加三项专属检查——AI 标记（commit 标注 ai-generated 便于审计与回溯）、幻觉 API 检查（调用不存在的 API/过期用法，靠类型检查+API 白名单）、测试缺口强制（AI 代码必须带对应测试，覆盖率门禁对 AI 代码更严）。
- 归因统计：PR 元数据记录 AI 生成比例，长期跟踪「AI 代码 vs 人工代码」的缺陷率/返工率——这是团队 AI 策略的数据基础。
- 安全扫描加严：AI 代码是供应链注入的高危面（幻觉包名），依赖名必须过包存在性校验。

```javascript
// CI 门禁：AI 代码专项检查
function aiGate(pr) {
  const aiFiles = pr.files.filter(f => f.aiGenerated);
  return {
    hallucinatedApi: typeCheck(aiFiles, { strict: true }),   // 幻觉API
    ghostPackages: aiFiles.flatMap(f =>
      f.imports.filter(i => !registry.exists(i.pkg))),       // 幻觉包
    testGap: coverage(aiFiles) < 0.9 ? 'AI代码需90%覆盖' : null,
    tagged: pr.metadata.aiRatio,                             // 归因
  };
}
```

