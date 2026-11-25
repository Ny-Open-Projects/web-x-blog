---
title: [RBL-348] 构建系统的 ESM/CJS 双包发布陷阱
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-348：构建系统的 ESM/CJS 双包发布陷阱

**答**:
- 双实例陷阱：同一包被 ESM 与 CJS 路径同时引用（exports 字段映射两个文件）→ 运行时两个实例（class instanceof 失败/单例失效/React hooks 报错）
- 防护：exports 条件互斥设计（import/require 各自指向且内部不互引）、dual 包内部公共逻辑抽 third 文件（双格式都从它引）、发布前 dual 包实例检测（are-the-types-wrong/publint）
- 构建侧：bundler resolve 条件正确（conditions 配置与运行时环境对齐——node 环境误用 browser 条件）
- 类型陷阱：types 条件顺序（types 必须先于 import/require）——TS 双读类型导致类型不一致报错

```json
"exports": {
  ".": {
    "types": "./dist/index.d.ts",
    "import": "./dist/index.mjs",
    "require": "./dist/index.cjs"
  }
}
// 陷阱：内部互引（mjs require cjs）→ 双实例
```
