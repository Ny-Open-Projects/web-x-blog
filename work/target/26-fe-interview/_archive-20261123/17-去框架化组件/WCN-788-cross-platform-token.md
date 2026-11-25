---
title: [WCN-788] 跨端（Web/小程序/Native）设计系统 token 如何统一并抹平差异？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-788：跨端（Web/小程序/Native）设计系统 token 如何统一并抹平差异？

**答**：
- 结论：用平台无关的 token JSON 作为单一数据源，按平台生成器输出不同格式（Web→CSS 变量、小程序→WXSS、Native→主题对象/资源）；语义 token 统一，物理值（如阴影、单位）按平台适配。
- 差异抹平：抽象「设计单位」转换（如 dp/px/rem），能力差异（如模糊、滤镜）提供降级值；一致性用 token hash 校验。
- 追问钩子：Native 不支持 CSS 变量这类动态能力，主题切换怎么做？考察「运行时重建样式对象 + 全量刷新」的替代方案。

```javascript
const tokens = { color: { primary: '#06f' }, space: { md: 16 } };
function genWeb(t) { return `:root{ --primary:${t.color.primary}; --space-md:${t.space.md}px }`; }
function genMini(t) { return `page{ --primary:${t.color.primary}; padding:${t.space.md}rpx }`; }
function genNative(t) { return { primary: t.color.primary, spaceMd: t.space.md * 2 }; } // dp 换算
console.log(genWeb(tokens));
console.log(genMini(tokens));
console.log(genNative(tokens));
```
