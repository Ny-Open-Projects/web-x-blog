---
title: [RBL-272] 产物里的构建期注入（define/runtime 注入）怎么排查问题
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-272：产物里的构建期注入怎么排查问题

**答**:
- 常见坑：DefinePlugin 值意外替换（标识符撞名如 `__VUE__` 全局替换）、环境变量漏传（CI 上 undefined 注入运行时炸）、JSON 序列化注入（对象注入变成字面量 vs 引用）
- 排查手段：产物 grep 注入值（确认注入结果）、构建日志列出 define 映射、runtime 注入点断点（版本文件/env 清单核对）
- 治理：define 键名加前缀约定（__APP_xxx）降低撞名；env 注入白名单（schema 校验缺失即构建失败）；产物带 envHash 供线上核对
- 验证：注入后跑一次运行时冒烟（关键页打开不炸）——注入问题往往到运行时才暴露

```javascript
// define 白名单校验（构建期）
const allowed = ['__APP_API__', '__APP_VERSION__']
Object.keys(define).forEach((k) => { if (!allowed.includes(k)) throw new Error(`define 撞名风险: ${k}`) })
// 产物核对
grep -o '__APP_API__' dist/main.js   # 应为 0（已替换为具体值）
```
