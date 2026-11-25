---
title: [ENG-276] 构建系统的并发安全（同 commit 并发构建/发布竞态）怎么防？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-276：构建并发安全怎么防？
**答**：
- 发布锁：同一应用同时只允许一个发布流水线（CI mutex/锁服务），并发发布会导致产物互相覆盖与版本错乱。
- 缓存写入竞态：远程缓存同键并发写是安全的（内容寻址幂等），但「缓存键算法版本」变更时要分命名空间（新旧键隔离）。
- merge race：两个 PR 同时 merge，后者的 CI 基于 base 旧 commit 构建则产物不含前者——自动 rebase 重跑（merge queue 模式）。
- 发布队列：发布任务进全局队列（同应用串行/跨应用可并行），编排层消费。
- 追问钩子：为什么「merge queue」是并发构建问题的终极解——两个 PR 各自 CI 绿但合并后可能互相破坏（类型冲突/行为冲突）；merge queue 把「合并后整体再验证一次」变成默认动作，并发正确性由队列结构保证而非靠人小心。

```yaml
# 发布互斥
concurrency: { group: deploy-${{ app }}, cancel-in-progress: false }
# merge queue：合并后重验证
merge_queue: { group_size: 5, revalidate: on-merge }
```
