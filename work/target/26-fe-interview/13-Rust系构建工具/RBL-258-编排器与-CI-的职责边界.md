---
title: [RBL-258] 编排器与 CI 系统的职责边界怎么划
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-258：编排器与 CI 系统的职责边界怎么划

**答**:
- 分工：CI 管「何时跑、在哪跑、资源与权限」（触发/runner/机密/审批），编排器管「跑什么、以什么顺序、缓存」——越界是混乱之源
- 反模式：在 CI 层手写任务依赖（yaml depends_on 一堆 job）复制了编排器的图逻辑——维护两份真相；或编排器里做 CI 逻辑（发通知/审批）
- 协作点：affected 计算（编排器）输出给 CI 动态矩阵；CI 提供 cache 存储后端（编排器消费）
- 判断标准：需求变化时改哪边？「多跑哪个任务/什么顺序」改编排器；「何时触发/谁能触发」改 CI

```text
职责表：
CI：trigger / runner / secrets / approval / notify
编排器：task graph / caching / affected / 并行调度
共享：cache 后端、affected 结果传递
```
