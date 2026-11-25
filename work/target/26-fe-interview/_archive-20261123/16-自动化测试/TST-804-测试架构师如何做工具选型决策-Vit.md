---
title: [TST-804] 测试架构师如何做工具选型决策（Vitest / Jest / Playwright / Cypress）？请用 ADR 框架说明
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-804：测试架构师如何做工具选型决策（Vitest / Jest / Playwright / Cypress）？请用 ADR 框架说明
**答**：
- 结论：选型不是比 star 数，而是用 ADR（架构决策记录）把「上下文—选项—决策—后果」显性化，让决策可追溯、可推翻。
- 决策维度：项目技术栈（ESM/TS）、团队规模、CI 环境、与现有基建的兼容、迁移成本、社区与维护活跃度。
- 示例取舍：Vitest 因 Vite 生态与 ESM 原生支持胜出；Playwright 因多浏览器与 tracing 优于 Cypress 的场景需具体论证。
- 一定要写「后果」：选型带来的隐性成本（学习曲线、插件缺口、迁移工期）要提前暴露，而不是上线后才发现。
- 追问钩子：如果你选的工具半年后社区不活跃了，ADR 里应该预留什么机制来触发重新评估？

```javascript
// ADR 模板：把选型过程结构化
const adr = {
  title: '单测框架选型：Vitest vs Jest',
  context: ['新项目全 ESM + Vite', '团队 15 人', 'CI 用 GitHub Actions'],
  options: [
    { name: 'Jest', pro: '生态成熟', con: 'ESM 支持繁琐、需 babel 转译' },
    { name: 'Vitest', pro: 'ESM 原生、复用 Vite 配置、快', con: '插件生态略少' },
  ],
  decision: 'Vitest',
  consequences: ['CI 提速 3x', '部分老 jest 插件需替换', '半年复盘一次'],
  reviewTrigger: '社区 6 个月无主版本更新 或 迁移成本 > 2 人周',
};
console.log(adr.decision, adr.consequences[0]);
```
