---
title: [RBL-342] 构建编排器的进程生命周期管理
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-342：构建编排器的进程生命周期管理

**答**:
- 关键问题：spawn 的子进程树清理（kill 父进程子进程残留——dev server 挂着端口占用）、信号传递（SIGTERM → 子进程优雅退出 vs SIGKILL 兜底）、退出码聚合（多子进程失败聚合报告）
- 实现要点：spawn 用 detached 管理进程组（kill(-pid) 杀整组）、退出码收集聚合（哪个任务失败一目了然）、stdin/stdout 管道复用与缓冲
- 长驻任务（dev server）：编排器要支持「常驻进程类型」——不等待退出而是等健康检查通过（与一次性 build 任务生命周期不同）
- 观测：子进程内存/CPU 采样（资源画像数据源），超阈值杀掉并标记

```javascript
// 进程组管理
const child = spawn(cmd, args, { detached: true, stdio: 'pipe' })
const killTree = () => process.kill(-child.pid, 'SIGTERM')
// 健康检查型任务
await waitFor(child, 'ready')   // 常驻任务等 ready 信号而非 exit
```
