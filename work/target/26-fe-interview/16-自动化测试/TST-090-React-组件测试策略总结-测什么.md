---
title: [TST-090] React 组件测试策略总结：测什么、不测什么？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-090：React 组件测试策略总结：测什么、不测什么？
**答**：
- 测什么（用户视角行为）：关键文案与数据展示、交互触发的外部回调与状态变化、分支条件渲染（loading/error/empty）、异步加载三态、错误边界、路由跳转、卸载清理。
- 不测什么：内部 state 命名、渲染次数、CSS 样式细节、组件库自身行为（表单库的校验引擎）、无业务含义的纯展示片段（可快照兜底但别较真）。
- 结构约定：一个组件一个 test 文件；公共包裹（router/store/provider）收敛到 renderWithProviders；mock 面收敛到网络与浏览器 API 两类。
- 组合拳：role/label 查询保 a11y、jest-dom 断言可读、userEvent 保真实、MSW 保网络真实语义。
- 面试话术收尾：给一个真实案例——「重构订单列表 DOM 时测试全绿零修改」或「act 警告揪出未清理的轮询定时器」，证明策略来自实战。

```javascript
// 组件测试的「测/不测」速查表（白板可写）
const policy = {
  test: [
    '用户可见的关键渲染（文案/数据/分支）',
    '交互回调契约（参数/次数/不触发场景）',
    '异步三态与错误边界',
    '卸载清理（监听/定时器/请求取消）',
    '路由与跳转',
  ],
  skip: [
    '内部 state 与实现细节',
    '三方库内部行为',
    '像素级样式',
    '无分支的纯展示碎片',
  ],
  tool: { query: 'getByRole/label', interaction: 'userEvent', net: 'MSW', assert: 'jest-dom' },
};
```
