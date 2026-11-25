---
title: [MP-068] Taro 与 uni-app 如何做选型决策？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-068：Taro 与 uni-app 如何做选型决策？
**答**：
- **技术栈**：团队以 React 为主选 Taro（Taro 对 React 支持最好）；以 Vue 为主选 uni-app（也可选 Taro 的 Vue3 支持）。
- **端覆盖**：要发 App（原生渲染）优先 uni-app（nvue/weex）；只发各家小程序 + H5 两者均可。
- **生态**：uni-app 插件市场/DCloud 工具链更全；Taro 背靠京东，React 生态与多端测试（jest）支持好。
- **复杂度**：强动态性 UI（拖拽、Canvas 密集）注意运行时开销，两框架都要按原生优化思路写。

```javascript
// 选型评估表（伪代码化）
const decision = {
  teamStack: 'react',        // react → taro；vue → uni-app
  targets: ['weapp', 'alipay', 'tt', 'h5'],   // 无 App 需求
  needNativeApp: false,      // true → uni-app nvue 优先
  ecosystem: 'taro-react-ecosystem-ok'
}
const framework = decision.needNativeApp ? 'uni-app' : 'taro'
```
