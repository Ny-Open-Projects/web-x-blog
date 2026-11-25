---
title: [BLD-251] 构建缓存与远程缓存的键对齐怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-251：缓存键对齐怎么做？
**答**：
- 对齐问题：本地持久缓存（webpack/vite）与 CI 远程缓存（turbo）键体系不同——本地键是「模块级」（内容+配置），远程键是「任务级」（包+任务）；两层命中不冲突但语义要分清。
- 对齐手段：构建器把「影响产物的全局因素」声明完整（env/version/插件），使本地模块级缓存与远程任务级缓存对同一输入得出一致判定——键输入清单是单一事实源（SCN-ENG-287）。
- 键版本化：键算法变更时版本前缀隔离（旧键全 miss 不误命中）。
- 可观测：两层命中率分开统计（本地/远程），异常定位到层。
- 追问钩子：为什么本地「模块级」与远程「任务级」缓存要分两层而不是统一——模块级粒度细（改一个文件只重转一个模块——dev 速度）；任务级粒度粗但可跨机器共享（CI 团队复用）；统一成一种粒度要么牺牲 dev 粒度要么牺牲共享性——两层各司其职，对齐的是「输入判定」而不是粒度。

```javascript
// 键输入单源
const cacheInputs = { env: declaredEnvs, toolVersion, presetVersion, lockHash };
// 本地模块级
webpack.cache = { type: 'filesystem', version: hash(cacheInputs) };
// 远程任务级
turbo.run('build', { inputs: cacheInputs });          // 同一输入判定源
```
