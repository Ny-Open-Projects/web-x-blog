---
title: [PER-812] RN 与小程序的启动性能对比：各端启动链路差异与优化手段映射
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-812：RN 与小程序的启动性能对比：各端启动链路差异与优化手段映射

**答**：
- RN 启动链路：Native init（引擎/模块注册）→ JS bundle 加载（字节码）→ JS 执行初始化 → 首帧渲染；瓶颈通常在 bundle 加载与 JS 执行。
- 小程序启动链路：微信壳初始化 → 逻辑层 App/Page 注册（主包 JS 执行）→ 渲染层 WXML 首屏 → setData 首次通信；瓶颈在主包体积与首次 setData。
- 手段映射表：bundle 体积 → 小程序分包；字节码预编译 → 小程序无对应（微信自己处理）；预渲染 → 小程序 Skyline/启动预渲染；首屏数据预取 → 两端都可用（容器预取 / 云函数预调用）。
- 统一认知：都是"引擎启动 + 代码加载 + 首帧"三段，先把分段耗时测准，再对号入座选优化，不做无分段的全局猜测。

```javascript
// 三端启动链路分段对齐表
const startupStages = {
  rn:   ['native-init', 'bundle-load', 'js-init', 'first-frame'],
  mp:   ['shell-init', 'logic-boot(主包执行)', 'render-first-wxml', 'first-setData'],
  h5:   ['container-warm', 'html-fetch', 'js-parse-execute', 'first-paint'],
};
// 对应优化手段
const opts = {
  'bundle-load': ['Hermes 字节码', 'bundle 拆分', '按需加载模块'],
  'logic-boot(主包执行)': ['主包瘦身', '分包', '启动预渲染'],
  'html-fetch': ['离线包', 'SSR', '预连接'],
  通用: ['数据预取', '骨架屏', '关键 CSS 内联'],
};
function alignReport(perStages) {              // 把各端分段映射到统一四段
  return perStages.map(s => ({ ...s, unified: mapStage(s.stage) }));
}
```
