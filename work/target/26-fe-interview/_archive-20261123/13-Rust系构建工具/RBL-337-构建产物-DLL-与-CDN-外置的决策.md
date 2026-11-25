---
title: [RBL-337] DLL 与 CDN 外置大依赖的决策分析
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-337：DLL 与 CDN 外置大依赖的决策分析

**答**:
- DLL（预打包不变的依赖）：构建提速但产物管理复杂（DLL 更新需重发）、缓存收益在 hash 稳定下与普通 chunk 无差——现代工具（持久缓存/Rust 速度）下多数场景 DLL 已不必要
- CDN 外置（externals）：vendor 从产物剥离走 CDN 独立缓存——收益是业务发版不拉 vendor；代价是版本协调（页面引用的 vendor 版本与依赖声明一致性）、多应用共享 CDN vendor 的治理
- 决策框架：单应用小规模 → 不折腾（现代工具够快）；多应用同栈大规模 → vendor CDN 化收益显著（全局缓存复用 + 发布提速）；跨团队版本治理能力是前提
- 替代方案：Module Federation 的 shared 仲裁（运行时协商版本）适合微前端场景

```text
决策矩阵：
单应用：不需要 DLL/外置（工具已够快）
多应用同栈：vendor CDN 化（收益大，需版本治理）
微前端：MF shared 运行时仲裁
```
