---
title: [CSS-180] JS 动态注入样式与直接改类，如何选择？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-180：JS 动态注入样式与直接改类，如何选择？

**答**：
- 原则：**离散状态用类，连续量用变量/内联，运行时未知的选择器才注入样式**。
- 改类（90% 场景）：浏览器可缓存类名对应规则、便于主题化与调试、动画可走 CSS transition。
- `style.setProperty('--x')`：拖拽坐标、进度条等每帧变化的连续量，写变量比拼整个 style 字符串快且不动其他属性。
- 注入 `<style>`/CSSOM：动态生成的组件（hash 类名）、按配置生成的规则集；高频路径用 `sheet.insertRule` 优于 innerHTML 重建。

```javascript
// 1. 离散状态：改类是标准答案
el.classList.add('is-open');
el.classList.toggle('is-active', cond);

// 2. 连续量：CSS 变量承载，CSS 侧 calc 消费
box.style.setProperty('--x', e.clientX + 'px');
box.style.setProperty('--progress', String(ratio));

// 3. 运行时未知选择器：注入样式表
const style = document.createElement('style');
style.textContent = `.widget-${hash} { width: ${cfg.width}px; }`;
document.head.appendChild(style);

// 4. 高频批量规则：CSSOM API
const sheet = style.sheet;
sheet.insertRule(`.widget-${hash} .item { color: ${cfg.color}; }`, sheet.cssRules.length);

// 5. 反例：每帧拼 style.transform 字符串覆盖全部内联样式
// el.style.cssText = `transform: translateX(${x}px)`  // 会清掉其他内联样式
```
