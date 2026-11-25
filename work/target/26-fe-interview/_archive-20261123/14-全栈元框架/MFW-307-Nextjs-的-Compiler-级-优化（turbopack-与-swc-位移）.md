---
title: [MFW-307] 编译器级优化：Turbopack/SWC 迁移的行为核对清单
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-307：编译器迁移核对清单

**答**:
- 行为差异面：CSS 处理链（PostCSS 插件兼容子集）、MDX/自定义 loader 生态位、环境变量注入时机、代码分割粒度（chunk 边界变化 → 缓存命中率变化）
- 核对方法：fixture 双跑（RBL-462 AB 法）——产物 diff 三看（chunk 数/首屏集合/重复包检测）；性能预算双记（dev 启动/HMR 延迟/build 时长）
- 迁移半径控制：先 Dev 侧（Turbopack 收益最直接风险最小）后 build 侧；loader 生态缺口用「过渡双跑」（不兼容 loader 的路由留 webpack）——桥接期明确拆除日期
- 回退开关：配置级一键回 webpack（保存旧配置分支）——编译器升级必须保留 48h 回退窗

```text
核对：fixture 双跑三看（chunk/首屏/重复包）+ 双记性能
半径：Dev 先行 → build 后跟；生态缺口路由级过渡
回退：旧配置分支保留 48h
```
