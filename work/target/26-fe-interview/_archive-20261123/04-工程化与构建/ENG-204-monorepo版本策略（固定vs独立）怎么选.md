---
title: [ENG-204] monorepo 版本策略（固定版本 vs 独立版本）怎么选？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-204：固定版本 vs 独立版本怎么选？
**答**：
- 固定版本（lockstep）：全仓一个版本号（Babel/Next 模式）——发布简单（一次发全部）、消费方升级一次到位；代价是无变更的包也发版（噪声）。
- 独立版本（independent）：各包独立 semver（Lerna independent 模式）——精确但发布心智重（记谁改了谁），跨包 breaking 升级要协调多个版本。
- 实践倾向：内部平台包用固定版本（强一致，升级原子），对外开源工具用独立版本（消费方节奏不同）。
- Changesets 是主流解法：变更 PR 里带 changeset 文件（声明影响的包与版本类型），发布时聚合生成 changelog 与版本 PR——声明式、可评审。
- 追问钩子：固定版本怎么解决「噪声发版」——CI 检测无变更的包 skip 发布（内容 hash 相同不发），版本号虽然跳但 registry 不产生真实新版本。

```jsonc
// .changeset/config.json —— 固定版本组
{
  "fixed": [["@org/ui-core", "@org/ui-icons", "@org/ui-tokens"]],
  "linked": [], "updateInternalDependencies": "patch", "access": "public"
}
```
```markdown
<!-- .changeset/xxx.md —— 变更声明 -->
---
'@org/ui-core': minor
'@org/ui-tokens': patch
---
Button 增加 loading 态
```
