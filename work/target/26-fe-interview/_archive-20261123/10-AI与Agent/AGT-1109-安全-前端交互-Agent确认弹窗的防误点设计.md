---
title: [1109] 前端「Agent 请求执行危险操作」的确认弹窗怎么防误点
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 交互]
type: 面试题
---

## 1109：前端「Agent 请求执行危险操作」的确认弹窗怎么防误点

**答**：
- 防误点设计：高危确认不 用普通 confirm——输入确认（输操作对象名）、延时按钮（3 秒后可点，防手滑连点）、关键信息外显（操作对象、影响范围、不可逆提示放在按钮上方而非折叠）。
- 批量确认陷阱：「允许所有」类按钮在 Agent 场景是灾难（后续任意高危都自动过），要么禁用要么限定「同类型同目标」且可见可撤销。
- 弹窗内容防注入：弹窗文案来自 Agent 输出时要过滤诱导话术（「紧急」「立即」），影响范围由系统计算并展示，不信 Agent 自己声明的影响面。
- 追问钩子：确认疲劳怎么平衡？——按真实风险分级弹窗（低危免弹），把「弹窗预算」留给真正的高危；同时提供「操作回滚」降低对弹窗的依赖。

```ts
function dangerConfirm(op) {
  return modal({
    title: `确认${op.action} ${op.target}？`,
    show: { impact: computedImpact(op), irreversible: op.irreversible }, // 系统计算
    confirm: { type: 'type-to-confirm', text: op.target, delay: 3000 },
    neverAllowAll: true,                          // 禁「允许所有」
    contentSanitized: true,                       // Agent 文案过诱导过滤
  });
}
```
