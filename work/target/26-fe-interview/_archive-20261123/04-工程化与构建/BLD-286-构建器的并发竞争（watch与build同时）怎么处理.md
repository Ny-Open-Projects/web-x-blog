---
title: [BLD-286] 构建并发竞争（watch 与 build 同时跑）怎么处理？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-286：构建并发竞争怎么处理？
**答**：
- 竞争场景：dev watch 与 CI build 同时写同一产物目录（本地 watch 没停就触发了 CI 或手动 build）/多 terminal 同时 build——产物目录损坏（半写状态）。
- 治理：产物目录隔离（watch 写 dist-dev，build 写 dist-build——不同目标互不踩）、构建锁（目录锁文件——第二个构建等待或失败提示）、原子 emit（先写临时目录再 rename——目录级原子性）。
- 与远程缓存交互：并发构建争抢缓存写入——内容寻址幂等（SCN-ENG-276），无需锁。
- 追问钩子：为什么「原子 emit（临时目录 + rename）」比「构建锁」更根本——锁解决「不并发写」，但进程崩溃/断电仍会留下半写目录；rename 是文件系统级原子操作（要么完整出现要么不出现）——产物目录永远处于一致状态，锁只是并发控制，原子性才是正确性保证。

```javascript
// 原子 emit
await buildTo('.dist-tmp');                            // 先写临时目录
fs.renameSync('.dist-tmp', 'dist');                    // 原子替换
// 目录隔离
{ watch: { outDir: 'dist-dev' }, build: { outDir: 'dist' } }
```
