---
title: [ENG-207] monorepo 公共包升级的协调节奏（breaking change 全仓跟进）怎么定？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-207：公共包 breaking change 怎么协调？
**答**：
- 升级编排：breaking change 先走 deprecation 周期（新 API 并存 + 旧 API 打弃用告警）→ 迁移 codemod 自动改调用方 → 全仓消费方迁移完 → 删旧 API 发 major。
- codemod 是关键：手改几十个消费包不现实；jscodeshift/ast-grep 脚本进包仓库（随包发布），升级 PR 里自动跑并展示 diff——迁移成本从「团队协商」变「一键执行」。
- 兼容期度量：deprecation 告警的调用点数量随时间下降曲线，归零才允许 major。
- 升级窗口：全仓升级统一窗口（如双周升级日），避免各包版本漂移在中间态。
- 追问钩子：为什么 codemod 要随包发布而不是放中央仓库——codemod 与 API 变更强耦合（同 PR 审查、同版本发布），中央仓库会导致 codemod 滞后于 API 变更，迁移时无可用工具。

```javascript
// packages/ui/codemods/button-v2.js —— codemod 随包发布
module.exports = (file, api) => {
  const j = api.jscodeshift;
  return j(file.source)
    .find(j.JSXOpeningElement, { name: { name: 'Button' } })
    .forEach(p => { p.node.attributes.push(
      j.jsxAttribute(j.jsxIdentifier('variant'), j.literal('primary'))); })
    .toSource();
};
// CI 升级编排：npx @org/ui-codemods button-v2 packages/** && git commit -m "migrate"
```
