---
title: [BLD-255] Source Map 模式选择（hidden/inline/external）怎么定？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-255：Sourcemap 模式怎么选？
**答**：
- 模式语义：inline（map 内联进产物——单文件但体积翻倍）、external（.map 独立文件+注释引用——公开但体积外挂）、hidden（生成 map 但产物无注释引用——监控平台消费）、eval（dev 快速映射）。
- 场景映射：dev → eval/cheap-module（快）、prod → hidden（上传监控平台，SCN-ENG-242 不泄源）、内部排障 → external（权限拉取）。
- cheap/module/eval 前缀语义：cheap 只映射到行（快）、module 含 loader 转换前源码（能还原 TS 原文）——dev 速度与还原精度的权衡。
- 追问钩子：为什么 prod 选 hidden 而不是 external——external 会在产物尾部留 `//# sourceMappingURL=xxx.map` 注释，任何人打开 DevTools 就能拉到完整源码（SCN-ENG-242 泄露）；hidden 生成 map 但不留引用——浏览器拿不到、监控平台按 buildinfo 主动上传消费——「能排障」与「不泄源」两全。

```javascript
// vite/webpack 模式映射
dev:   sourcemap: 'cheap-module-eval-source-map'      // 快
prod:  sourcemap: 'hidden-source-map'                 // 生成不引用（监控平台消费）
lib:   sourcemap: true                                // 库发布用 external（消费方排障）
```
