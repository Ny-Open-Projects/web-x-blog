---
title: [RBL-237] sourcemap 在产物分析里怎么用
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-237：sourcemap 在产物分析里怎么用

**答**:
- 用途一：体积归因——source-map-explorer/webpack-bundle-analyzer 用 map 把压缩产物还原到「原始源码粒度」的体积贡献（比 chunk 粒度准确 10 倍）
- 用途二：错误定位——Sentry 等监控用 map 符号化压缩堆栈，发布时上传 map（私有，不进公网产物目录）
- 用途三：duplication 检测——不同 chunk 里同一模块的 map 指向同一源文件，可发现重复打包
- 工程注意：分析时产物与 map 必须同版本；map 参与指纹（源码变了 map 变）但不上 CDN（体积大）

```javascript
// 分析
const { explore } = require('source-map-explorer')
explore([{ code: 'dist/main.js', map: 'dist/main.js.map' }])   // 按源文件粒度的体积表
// 监控：release 时上传 map（Sentry），产物目录不部署 map
```
