---
title: [R19-295] Next 里 Suspense 与 loading.js 的优先级与配合关系？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-295：Suspense 与 loading.js 的优先级与配合？
**答**：
- loading.js 本质是框架自动包的 Suspense fallback：段级（route segment）数据未就绪时展示。
- 手动 Suspense 更细粒度：段内某块数据单独等待时用手动边界，loading.js 只覆盖整段导航。
- 优先级：内层手动边界先接管（数据挂在手动边界内），段级 loading 处理「整段 RSC 渲染未完成」。
- 配合策略：页面骨架用 loading.js（段级视觉），页内局部用 Suspense（数据级视觉）。
- 坑：同一层级 loading.js 与手动 Suspense 都存在时，确认数据 promise 的位置——promise 挂在谁那里就谁显示 fallback。
