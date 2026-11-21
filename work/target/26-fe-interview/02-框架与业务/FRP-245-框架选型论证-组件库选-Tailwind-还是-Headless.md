---
title: [FRP-245] 组件样式方案：Tailwind 还是 Headless UI 还是全家桶组件库？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-245：Tailwind、Headless、组件库怎么选？
**答**：
- 组件库全家桶（AntD/Element）：开发效率最高、一致性内置——适合中后台、快交付；代价：定制难、体积、视觉同质。
- Headless（Radix/Headless UI）+ 自定义样式：交互逻辑可靠（a11y/键盘）、视觉自由——适合品牌向产品；代价：样式全自建工作量。
- Tailwind：原子样式与任意方案兼容，design token 治理是关键——搭配 Headless 是主流「自由派」组合。
- 判据：中后台标准化 → 组件库；C 端品牌设计 → Headless + Tailwind；混合 → 分域（管理端组件库、用户端 Headless）。
- 通用原则：样式方案选型的本质是「设计一致性来源」放在哪（库/团队/约定）。
