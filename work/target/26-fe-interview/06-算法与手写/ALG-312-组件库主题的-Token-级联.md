---
title: [ALG-312] 设计 Token 级联：基础 token → 语义 token → 组件 token 的三层变量体系（换肤只改一层）？
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

**场景**：主题换肤（品牌色/暗色/紧凑密度）：三层 token——基础层（blue-500 原子值）→ 语义层（primary/success/danger）→ 组件层（button-bg 引用语义）。换肤只改基础层或语义层，组件层不动——一处改全站生效。

**思路**：CSS 变量三层引用链 + 主题切换只覆写对应层；密度主题（compact）改的是间距层。

```css
:root {
  /* 基础层：原子色板（与品牌无关的设计规范） */
  --blue-500: #09f; --blue-600: #08d; --gray-100: #f5f5f5; --gray-900: #222;
  --space-2: 8px; --space-4: 16px; --radius: 8px;
  /* 语义层：业务语义（换肤只改这层） */
  --primary: var(--blue-500); --primary-hover: var(--blue-600);
  --bg: #fff; --text: var(--gray-900);
  /* 组件层：组件引用语义（换肤永不动） */
  --button-bg: var(--primary); --button-padding: var(--space-2) var(--space-4);
}
[data-theme='dark'] { --primary: #4cf; --bg: #121212; --text: #eee; }     /* 只改语义层 */
[data-density='compact'] { --space-2: 4px; --space-4: 8px; --radius: 4px; } /* 密度改基础层间距 */
.btn { background: var(--button-bg); padding: var(--button-padding); }      /* 组件层引用 */
/* 换肤收益：品牌定制 = 覆写语义层 10 个变量（不是全站 CSS 重写）；
   组件层零改动 —— 新组件自动继承主题（引用语义层的组件无需适配） */
```

**评分点**：
- 三层级联（基础/语义/组件）与"换肤只改一层"——本题核心。
- 密度主题改基础层间距（变量级联传播）。
- 组件层引用语义层的自动继承。
- 与 PER-403 的联动（变量切换不触发选择器重匹配）。
