---
title: [RBL-539] dev server 与 HMR 的增量服务：产物内存化与按需编译
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-539：dev server 与 HMR 的增量服务：产物内存化与按需编译

**答**：
- dev server 的性能核心：**产物内存化**（编译产物不落盘，HTTP 直接从 Rust 内存 serve）+ **按需编译**（浏览器请求什么编译什么——模块级 lazy）。
- 按需编译的实现：dev server 拦截模块请求 → 视为「编译任务」——只编译请求路径的依赖闭包（不是全量构建）；未请求的页面模块零编译成本——这是「dev 快于 build」的本质（build 必须全量）。
- 内存产物的 HTTP 服务：ETag（内容 hash）+ 304 协商缓存——浏览器二次刷新零传输；Cache-Control: no-cache（协商缓存而非强缓存——保证 HMR 一致）。
- HMR 推送通道：WS 单连接（更新事件）+ HTTP 轮询兜底——推送内容只含「变更模块列表 + 新产物 hash」，浏览器按需拉取变更产物。
- dev 与 build 的产物一致性：dev 内联 CSS/style 注入、无压缩、有 HMR runtime——「dev 与 build 产物不同」是已知 trade-off，但**模块图必须一致**（否则 dev 能跑 build 挂）——模块图一致性测试是正确性工程（RBL-626）的重点。
- 追问钩子：dev server 的「按需编译」与 build 的「全量编译」共用同一模块图构建逻辑——抽象成「可部分求值的编译图」（RBL-518 任务图）是架构统一的关键。

```javascript
// dev server 增量服务
const DEV_SERVER = {
  产物内存化: '编译产物不落盘——Rust 内存直接 serve HTTP（ETag 内容 hash + 304 协商）',
  按需编译: {
    core: '浏览器请求什么编译什么（模块级 lazy）——未请求页面零成本',
    essence: 'dev 快于 build 的本质：build 必须全量',
  },
  缓存策略: 'Cache-Control: no-cache（协商非强缓存）——保证 HMR 一致',
  HMR通道: 'WS 推送（变更列表+产物 hash）+ HTTP 轮询兜底——浏览器按需拉取',
  一致性: 'dev/build 产物允许不同（CSS/压缩/HMR runtime）但模块图必须一致——dev 能跑 build 挂是正确性事故',
  架构统一: 'dev 按需 + build 全量 = 同一「可部分求值的编译图」（RBL-518 任务图）',
}
```
