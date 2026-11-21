---
title: [ARC-021] Monorepo 的包版本策略怎么选？changesets 如何工作？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-021：Monorepo 的包版本策略怎么选？changesets 如何工作？
**答**：
- fixed 模式：所有包统一版本，一致性好但会"陪跑发版"，适合强耦合包群（如组件库一族）。
- independent 模式：各包独立 semver，发布精准但心智负担高，适合松散工具包。
- changesets 的流程：开发时 `changeset` 声明变更意图 → PR 携带变更文件 → 合并后 CI 自动汇总发版并写 CHANGELOG，把"发版"从人肉变成 PR 驱动。

```text
# changesets 工作流
1) feat 分支上执行：pnpm changeset
   → 选择 bump 类型（patch/minor/major）+ 写变更摘要
   → 生成 .changeset/xxx-yyy.md  与代码一起提交
2) PR review：变更文件就是"发版意图"，评审可见
3) 合并入 main：CI 版本机器人汇总所有 changeset
   → 消耗 changeset 文件、升版本、写 CHANGELOG、自动 publish
```

```markdown
<!-- .changeset/lucky-lions-run.md —— PR 中携带的变更声明 -->
---
'@corp/ui': minor
'@corp/design-tokens': patch
---

feat(ui): Button 增加 loading 态；同步 token 间距规范
```
