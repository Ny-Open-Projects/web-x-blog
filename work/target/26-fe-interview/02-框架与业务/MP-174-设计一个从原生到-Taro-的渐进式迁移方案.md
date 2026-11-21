---
title: [MP-174] 设计一个从原生到 Taro 的渐进式迁移方案？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-174：设计一个从原生到 Taro 的渐进式迁移方案？
**答**：
- 可行性前提：Taro 3 运行时可加载**原生自定义组件**（taro 编译配置可直接引入原生页面/组件），支持"页面级"渐进。
- 路线：第一步**基建先行**——Taro 脚手架承载新需求页（新页面全部 Taro 写）；第二步按业务域把稳定页面逐个迁移（低风险页面先行）；第三步主包骨架（app.js/tabBar）最后切换。
- 风险控制：迁移前后同页面 **AB 对比**（埋点分版本），核心链路自动化回归；双栈期体积监控（运行时 + React 会增加包体）。
- 收益评估：迁移动机要成立（多端需求/生态/招聘），纯单端小程序强行迁移要算 ROI。

```javascript
// Taro 3 中复用原生页面/组件的渐进迁移
// config/index.js
module.exports = {
  compiler: 'webpack5',
  copy: { patterns: [{ from: 'src/native/', to: 'dist/native/' }] }  // 原生资源直通
}
// 新页面用 Taro：src/pages/new-feature/index.jsx
// 原生页面引用：app.config.js 的 pages 混合登记
export default {
  pages: [
    'pages/index/index',          // 原生保留
    'pages/new-feature/index'     // Taro 新页
  ],
  subPackages: [{ root: 'pkgTrade', pages: ['pages/confirm/confirm'] }] // 逐步迁移
}
```
