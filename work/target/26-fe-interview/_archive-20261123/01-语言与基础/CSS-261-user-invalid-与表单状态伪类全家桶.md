---
title: [CSS-261] :user-invalid 与表单状态伪类全家桶
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 表单]
type: 面试题
---

## CSS-261：:user-invalid 与表单状态伪类全家桶

**答**：
- :invalid 的问题：页面一加载必填空输入框就「红」——用户还没操作就报错，体验差
- :user-invalid/:user-valid：只在用户交互过（输入后失焦）才匹配——「用户实际触碰过」的校验态
- 全家桶：:required/:optional、:placeholder-shown（为空且显示占位）、:in-range/:out-of-range、:default（默认选中项）、:indeterminate
- 组合配方：`input:user-invalid { border-color: red }` + `input:placeholder-shown` 区分「没填过」与「填错了」
- 兼容：Chrome 119+/Safari 16.5+；老浏览器接受 :invalid 降级或用 :not(:placeholder-shown):invalid 模拟

```css
/* 未触碰不报错 */
input:user-invalid { border-color: #e33; background: #fee; }
/* 还没输入过 + 必填：中性提示 */
input:required:placeholder-shown { border-color: #ccc; }
/* 数字范围 */
input:out-of-range { border-color: orange; }
```
