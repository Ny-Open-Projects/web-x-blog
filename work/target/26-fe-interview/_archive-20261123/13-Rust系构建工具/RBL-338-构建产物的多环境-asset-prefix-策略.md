---
title: [RBL-338] 构建产物的多环境 assetPrefix 策略
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-338：构建产物的多环境 assetPrefix 策略

**答**:
- 场景矩阵：本地 dev（相对路径/localhost）、测试（测试 CDN 域）、生产（生产 CDN 域）、多 region（就近 CDN）——assetPrefix 是「构建期可定、部署期可变」的张力点
- 方案：相对路径（./static/）部署灵活性最高（同产物任意域名可用）；绝对 CDN 域（构建期注入）控制力强但环境耦合——同产物多 CDN 用相对路径 + 运行时注入或 pathRewrite
- 一致性校验：产物内 url() / publicPath 全链路一致性（JS 引用的字体/图片路径与 CSS 引用一致——漏配导致 404 资源）
- 回退机制：CDN 域不可用时 fallback 主域（构建产物带多域探测脚本，或部署层域名解耦）

```text
策略：相对路径灵活 / 绝对路径可控；同产物多 CDN → 相对 + pathRewrite
校验：产物内资源引用全链路一致性扫描
```
