---
title: [R19-267] useTransition 的 isPending 与嵌套 startTransition 的语义？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-267：useTransition 的 isPending 与嵌套 startTransition 的语义？
**答**：
- isPending：当前 transition（该 hook 绑定的）尚未提交时为 true——用于显示加载态，但注意「旧 UI 仍显示」，pending 是「正在准备新内容」。
- 嵌套：transition 内再 startTransition（低优先级包裹高优），内部 transition 可独立中断；async action 用 awaitTransition？不存在——直接在 startTransition(async () => {}) 中 await，await 后的更新仍属该 transition。
- 竞态：连续两次 startTransition，后者自动取消前者未完成的渲染（保留最后意图）。
- 常用模式：startTransition(async () => { const d = await fetchData(); setData(d) })——await 后 setState 仍在 transition 内，数据到达才切换视图。
