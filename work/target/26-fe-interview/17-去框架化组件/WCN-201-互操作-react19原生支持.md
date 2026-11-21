---
title: [WCN-201] React 19 对 Web Components 的原生支持改善了什么？还有哪些坑？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-201：React 19 对 Web Components 的原生支持改善了什么？还有哪些坑？
**答**：
- React 19 起自定义元素属性/事件可直接设置：props 作为属性传递（复杂对象设 property 而非 attribute）。
- 事件监听不再需要 ref + addEventListener hack——但自定义事件（非内置）仍要自行桥接或用事件目标声明。
- 剩余坑：attribute 序列化规则（对象不进 attribute）、SSR 端元素未被定义时输出为空标签。
- 迁移策略：旧版包装器（wrapper）逐步移除，先从「简单属性组件」开始验证。

```javascript
// React 19 直接使用
function Page() {
  return <goods-card sku="A1" count={3} on-add-cart={(e) => console.log(e.detail)} />;
}
// 坑：count 是对象时框架设 property；attribute 只有字符串
// SSR：customElements 未注册时渲染 <goods-card></goods-card>（无内容）
r
```
