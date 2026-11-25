---
title: [WCN-958] WC 在非 DOM 端（小程序 / Flutter / RN）的适配边界：什么时候不该选
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-958：WC 在非 DOM 端（小程序 / Flutter / RN）的适配边界：什么时候不该选

**答**：
- 结论先行：WC 是浏览器 DOM 标准，跨到非 DOM 端（微信小程序、Flutter、React Native）时没有原生自定义元素——「一次实现到处运行」在这些端不成立。
- 可行路径：用编译/桥接把 WC 逻辑转成各端组件（如把 token/协议层复用、UI 层各端重写），但事件/slot/生命周期语义要重新映射，成本高。
- 不该选 WC 的信号：核心目标端是非 DOM 原生端、团队无跨端编译能力、组件强依赖 DOM API（MutationObserver/focus）；这时「统一设计语言 + 各端原生实现」更务实。
- 小程序兼容：小程序有自己的组件模型，WC 只能作为「逻辑与 token 规范的来源」，UI 需重写；可复用的是设计 token JSON 与交互规范。
- 追问钩子：面试官问「有没有跨端编译方案把 WC 编到小程序」——答：有（如基于统一 DSL 编译到各端），但那是「统一 DSL 多端输出」而非 WC 本身跨端，别混淆概念。

```javascript
// 跨端现实：复用 token/协议，UI 各端重写
const sharedSpec = {
  tokens: { primary: '#1677ff' },
  contract: { onClick: { payload: 'id' } },
};
function renderFor(platform, spec) {
  // WC 端直接消费 spec
  // 小程序/Flutter/RN：复用 spec.tokens 与 contract，UI 用各端原生组件重写
  return `${platform}: 复用 token=${spec.tokens.primary}，UI 用 ${platform} 原生实现`;
}
['web(wc)', 'mini', 'flutter', 'rn'].forEach(p => console.log(renderFor(p, sharedSpec)));
```
