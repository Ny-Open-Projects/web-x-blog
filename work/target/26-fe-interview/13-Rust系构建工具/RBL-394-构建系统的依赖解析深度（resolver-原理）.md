---
title: [RBL-394] 构建系统的依赖解析（resolver）原理
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-394：构建系统的依赖解析（resolver）原理

**答**:
- 解析规则链：相对路径（文件/目录/index）→ package 入口（exports 字段优先 → module → main）→ 条件解析（import/require/browser/node conditions）→ alias
- 性能面：解析是高频 IO 操作（每 import 一次 stat 系列）——oxc-resolver/enhanced-resolve 的缓存（目录解析结果缓存）与并行 stat 是提速关键
- 正确性坑：exports 字段的存在改变解析行为（老 bundler 忽略 exports → 解析到不同文件）、symlink realpath 语义（RBL-347）、条件顺序敏感
- 工程实践：resolve.alias 收敛（团队统一别名清单防不一致）、tsconfig paths 与 bundler resolve 的一致性校验（两边解析结果必须一致）

```text
规则链：相对 → exports → main → conditions → alias
性能：缓存 + 并行 stat；坑：exports 语义 / realpath / 条件顺序
一致性：tsconfig paths ↔ bundler resolve 对齐
```
