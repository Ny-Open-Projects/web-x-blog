---
title: [WCN-506] 美团多品牌场景：语义层 → 组件层 → 品牌层三级 Token 映射如何设计？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-506：美团多品牌场景：语义层 → 组件层 → 品牌层三级 Token 映射如何设计？

**答**：
- 结论：三层解耦——语义 token（如 color.action）不写死值，品牌层注入具体值，组件只消费语义层。
- 映射链：品牌变量 → 语义 token → 组件内部 var(--sem) 引用，组件代码永远不出现品牌色值。
- 切换品牌即换一层 CSS 变量覆盖，无需重编译组件；用 @property 注册保证类型与过渡。
- 追问：某品牌想微调单个组件的颜色怎么办？（答：组件层提供 --ds-x-override 插槽变量，优先级介于语义与品牌间）

```javascript
/* 品牌层 */
:root { --brand-primary: #ff5000; --brand-radius: 8px; }
/* 语义层：把品牌变量映射为语义 */
:root { --color-action: var(--brand-primary); --radius-md: var(--brand-radius); }
/* 组件层：只引用语义，暴露 override 插槽 */
my-btn { --ds-btn-bg: var(--color-action); }
/* 品牌微调：覆盖组件插槽变量即可 */
.brand-yellow my-btn { --ds-btn-bg: #ffd100; }

/* 品牌切换兜底：变量未定义时回退到系统色 */
:root { --color-action: var(--brand-primary, #1677ff); }
```
