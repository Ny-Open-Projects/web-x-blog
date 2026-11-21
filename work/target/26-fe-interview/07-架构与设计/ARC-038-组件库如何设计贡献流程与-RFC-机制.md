---
title: [ARC-038] 组件库如何设计贡献流程与 RFC 机制？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-038：组件库如何设计贡献流程与 RFC 机制？
**答**：
- 分级：bug fix 走普通 PR；新组件/破坏性 API 必须先 RFC（动机、API 草案、竞品对比、无障碍与测试计划），评审通过才允许实现。
- 好处：把"API 设计"的讨论前置到代码之前，避免合并后反复 breaking。
- 流程配套：RFC 模板化、RFC 讨论限定时限（如两周）、结论落 ADR、实现 PR 关联 RFC 编号。

```text
rfcs/proposals/0042-tabs-lazy-mount.md
────────────────────────────────────
RFC-0042：Tabs 增加 lazyMount 与 keepMounted
状态：Accepting comments → 截止 2026-04-15
动机：大页面 20 个 Tab 全量挂载首屏 TTI 超 3s。
API 草案：
  <Tabs items={...} lazyMount />        // 首次激活才挂载
  <Tabs.Panel keepMounted />            // 卸载后保留 DOM 状态
竞品对比：Radix(支持, 分别两个字段) / AntD(destroyInactiveTabPane 反向控制)
无障碍：懒挂载不得破坏 aria-controls 关联，需补 axe 用例
测试计划：单测挂载时机 + Storybook 视觉基线 + 内存泄漏用例
实现 PR：!317（RFC 通过后才能合入，commit 关联 RFC-0042）
```

---

## 五、微前端架构（ARC-039 ~ ARC-050）
