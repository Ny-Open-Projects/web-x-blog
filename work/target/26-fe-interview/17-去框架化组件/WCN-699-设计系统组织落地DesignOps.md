---
title: [WCN-699] DesignOps 视角下，设计系统与研发协作流程如何设计？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-699：DesignOps 视角下，设计系统与研发协作流程如何设计？

**答**：
- 结论：DesignOps = 设计与研发的「接口人 + 流程 + 工具」——统一设计源文件规范、建立「设计→token→代码」自动流转、定义评审节奏。
- 实践：设计师维护 Figma 变量库并发布；token 自动生成并 PR 到代码库；组件变更走 Design+Frontend 联合评审；定期同步会对齐路线图。
- 追问钩子：最大的摩擦点是什么？通常是「设计改了代码没跟上」——需靠自动化管线和单一数据源解决，而非靠人盯。

```javascript
const FLOW = [
  { step: '设计', actor: 'Designer', output: 'Figma 变量库' },
  { step: '转换', actor: 'Pipeline', output: 'token JSON (自动生成 PR)' },
  { step: '评审', actor: 'Design+FE', output: '联合评审通过' },
  { step: '发布', actor: 'CI', output: '文档站 + npm 包' },
];
function nextStep(current) {
  const i = FLOW.findIndex(s => s.step === current);
  return FLOW[(i + 1) % FLOW.length];
}
console.log(nextStep('设计').output); // token JSON（自动生成 PR）
```
