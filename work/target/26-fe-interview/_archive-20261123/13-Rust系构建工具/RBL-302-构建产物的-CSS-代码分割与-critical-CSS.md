---
title: [RBL-302] 构建产物的 CSS 分割与 critical CSS 提取
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-302：构建产物的 CSS 分割与 critical CSS 提取

**答**:
- 分割策略：CSS 跟随 JS chunk（chunk 内联 style 或提取同名 .css）；与 JS 分离提取（单 CSS 入口 vs 每路由 CSS）——按路由分割最平衡
- Critical CSS：首屏内联（html head 里 <style>）+ 其余异步加载——内联量控制（预算 ~14KB），构建期用 puppeteer 扫首屏用到的选择器生成
- FOUC 防护：异步 CSS 加载完成前的兜底样式（最小骨架样式内联）；media 技巧（rel=stylesheet media=print onload 切换）
- 工程化：critical 清单 CI 校验（首屏渲染关键页截图对比，防 critical 失效）

```text
策略：路由级 CSS 文件 + 首屏 critical 内联（预算 14KB）+ 异步加载其余
构建期生成：puppeteer 扫描 → penthouse 生成 critical css → html 注入
```
