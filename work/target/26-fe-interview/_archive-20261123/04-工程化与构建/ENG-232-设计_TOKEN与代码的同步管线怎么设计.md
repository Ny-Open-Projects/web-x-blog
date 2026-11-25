---
title: [ENG-232] Design Token 与代码的同步管线（Figma→代码）怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-232：Design Token 同步管线怎么设计？
**答**：
- 管线：Figma Variables（单源）→ 导出 JSON → Style Dictionary 转换（CSS 变量/TS 常量/Android/iOS）→ 包发布 → 各端消费——token 变更走包发布流程（可评审可回滚）。
- 变更分级：token diff 自动分 semver（新增 token=minor、改值=patch 视语义、删除=major），与 SCN-ENG-204 版本机制打通。
- 校验关卡：对比度校验（无障碍）进 token 管线、命名规范 lint、与旧 token 的映射表（重命名不破坏存量）。
- 消费端防漂移：禁止组件内硬编码色值（lint 检查 hex/rgb），强制引用 token——不然 token 管线形同虚设。
- 追问钩子：为什么 token 要「包发布」而不是直接同步进组件库源码——发布可独立版本化（设计侧改 token 不需要组件库发版）、可回滚、可被多组件库共享；源码直写让 token 与组件库版本耦合。

```bash
# 管线
figma-tokens export > tokens.json
style-dictionary build   # -> css vars / ts consts / ios / android
pnpm publish @org/tokens # diff -> 自动 semver
```
```javascript
// lint: 禁硬编码色值
{ "rules": { "no-inline-color": "error" }, "allow": ["var(--*)"] }
```
