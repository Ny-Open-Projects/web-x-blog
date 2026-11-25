---
title: [AIC-072] 复杂交互（如拖拽排序 + 撤销）怎么向 AI 描述？「状态机描述法」是什么？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-072：复杂交互（如拖拽排序 + 撤销）怎么向 AI 描述？「状态机描述法」是什么？
**答**：
- 痛点：交互类需求用自然语言描述容易漏「中间态」和「打断情况」（拖拽中右键、拖到边界、连点撤销），AI 会按最简路径实现。
- 状态机描述法：把交互抽象成「状态集合 + 事件转移表」——states（idle/dragging/committing）、events（pointerdown/move/up/escape）、transitions，直接给 AI 一张表，歧义归零。
- 配套三件：边界规则（能不能拖出容器）、异常规则（transition 中收到新事件怎么办）、验收场景（给 3 个「必须能处理」的打断场景）。
- 状态机描述同时是测试用例清单——每条转移对应至少一个测试，交互测试从「凭感觉」变成「按表全覆盖」。
- 追问钩子：这个方法通用化就是「先写契约再写实现」，和 TDD 的精神一致，只是契约形式换成了转移表。

```javascript
// 拖拽排序的状态机描述（直接作为 prompt 输入）
const dragFSM = `
states: idle | dragging | committing
transitions:
  idle --pointerdown(item)--> dragging
  dragging --pointermove--> dragging (预览位置更新，原位置占位)
  dragging --pointerup--> committing (异步提交顺序，提交前显示 pending)
  dragging --escape/blur--> idle (还原顺序)
  committing --fail--> idle (toast 错误，顺序还原)
验收场景：拖拽中按 ESC；提交中再次拖拽（必须排队或禁止）；提交失败后重试。`;
```
