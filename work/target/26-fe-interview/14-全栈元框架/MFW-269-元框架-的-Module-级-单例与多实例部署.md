---
title: [MFW-269] 模块级单例在多实例部署下的语义（全局缓存陷阱）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## MFW-269：模块级单例 × 多实例

**答**:
- 陷阱：`const cache = new Map()` 模块级当「应用缓存」——serverless 每实例独立内存（数据各一份不同步）+ 实例随时回收（缓存说没就没）——单实例直觉在多实例全错
- 分级替代：请求级数据 → AsyncLocalStorage/per-request Map；跨请求共享 → 外部存储（Redis/KV）；只读计算结果 → 构建期物化（进产物）
- 判定问句：这个「全局变量」的生命周期声明是什么？跨实例吗？回收可接受吗？——三问不答清就是潜伏 bug
- 检测：lint 禁模块级可变导出（let 缓存对象）——dev 单实例看不出、生产多实例随机错（最难查的一类线上怪问题）

```javascript
// ❌ 多实例下语义破碎
const sessionCache = new Map()                    // 每实例一份 + 随机回收
// ✅ 分级
const sessionCache = redisClient                  // 跨实例共享
const reqScoped = als.getStore()                  // 请求级
const COMPILED = buildAtBuildTime()               // 构建期物化进产物
```
