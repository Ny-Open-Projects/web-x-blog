---
title: [ENG-242] Sourcemap 的工程策略（线上报错还原但不泄露源码）怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-242：Sourcemap 策略怎么做？
**答**：
- 分离发布：构建产出 sourcemap 但不上传到公开 CDN（hidden-source-map），而是上传到错误监控平台（Sentry release 关联）——用户侧拿不到源码，监控侧可还原堆栈。
- 版本关联：sourcemap 与 release/commit 绑定，报错事件按 buildinfo 匹配正确版本的 map（SCN-ENG-223 联动）。
- 保留策略：每个 release 的 map 保留期与该版本线上生命周期对齐 + 一段缓冲。
- 排障特权通道：内部排障工具按权限拉取 sourcemap 还原源码（审计记录）。
- 追问钩子：为什么 sourcemap 上公开 CDN 是风险——map 包含完整源码（业务逻辑/注释/可能的敏感串）；公开可下载等于源码泄露，hidden-source-map + 监控平台是「能排障」与「不泄源」的平衡点。

```javascript
// vite: build.sourcemap: 'hidden'   产出 map 但产物不引用
// Sentry 上传
sentry-cli releases files <sha> upload-sourcemaps dist --rewrite
// 版本匹配还原
errorReport.buildSha -> sourcemapStore[buildSha]  // SCN-ENG-223 buildinfo 联动
```
