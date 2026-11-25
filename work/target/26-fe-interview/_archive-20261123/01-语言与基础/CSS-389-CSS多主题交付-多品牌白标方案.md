---
title: [CSS-389] CSS 多主题交付：多品牌白标方案
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## CSS-389：CSS 多主题交付：多品牌白标方案

**答**：
- 白标需求：同一代码交付多品牌（不同 logo/色板/圆角/字体）——实现载体：语义 token 层按品牌注入（构建期多 bundle 或运行时变量注入）
- 构建期方案：按品牌出独立 CSS bundle（token 层替换编译）——体积小、无运行时成本，代价是构建矩阵与发布流程复杂
- 运行时方案：单一 CSS + 品牌变量集（JSON → CSS 变量注入 :root）——灵活（运营可配），代价是变量失效面与「非法值」校验
- 混合策略：静态品牌资产（色板/字体）构建期注入，运营可调项（活动主题色/横幅）运行时注入——按变更频率分层
- 交付校验：品牌 token 完整性测试（每个语义变量在所有品牌下有值 + 对比度检查）——白标翻车常见于「某品牌漏配 hover 色」

```javascript
// 运行时品牌注入
const brand = await api.get('/api/brand'); // { primary: '#0a6cff', radius: 12 }
if (!isValidBrandToken(brand)) brand = DEFAULT_BRAND;   // 校验兜底
for (const [k, v] of Object.entries(brand)) r.style.setProperty(`--brand-${k}`, v);
```

```css
:root { --btn-bg: var(--brand-primary, #1677ff); --btn-radius: var(--brand-radius, 6px); }
```
