---
title: [WCN-996] 终极反驳：「既然 WC 这么好，为什么 React / Vue 仍是主流」怎么回应
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-996：终极反驳：「既然 WC 这么好，为什么 React / Vue 仍是主流」怎么回应

**答**：
- 结论先行：WC 与框架不是替代关系——WC 是「组件互操作标准」，React/Vue 是「应用开发范式」；主流框架胜在应用层的状态管理、路由、工程化与生态，WC 补的是跨框架复用与隔离这一层。
- 定位差异：框架解决「怎么写复杂应用」（响应式、组件组合、工具链），WC 解决「组件怎么跨框架复用与封装」（标准、隔离、生命周期）；两者正交，常组合使用。
- 现实原因：框架开发体验成熟、招聘池大、生态丰富；WC 在复杂状态/SSR/类型/调试上仍有短板，所以应用层仍是框架主导。
- 趋势判断：标准在补齐（DSD、ElementInternals、Signals 提案、React 19 WC 支持），编译式框架（Solid/Vapor/Qwik）让「框架的归框架、标准的归标准」更清晰。
- 追问钩子：面试官问「那你为什么还要去框架化」——答：不是去掉框架，而是「把复用层标准化、把运行时成本前移」，在跨端/多团队/性能敏感场景拿到框架单独给不了的收益。

```javascript
// 定位：两者正交，组合使用
const roles = {
  framework: ['应用状态', '路由', '组件组合', '工程化', '开发体验'],
  webComponents: ['跨框架复用', '样式隔离', '标准生命周期', '设计与实现解耦'],
};
function choose(concern) {
  return roles.framework.includes(concern) ? '框架主导'
       : roles.webComponents.includes(concern) ? 'WC 主导' : '组合';
}
console.log(choose('路由'), choose('跨框架复用'), choose('复杂组件库'));
// 框架主导 / WC 主导 / 组合
```
