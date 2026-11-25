---
title: [RBL-167] 缓存命中率突然掉了怎么排查？（缓存失效风暴）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-167：缓存命中率突然掉了怎么排查？（缓存失效风暴）

**答**：
- 先确认现象：命中率 = 命中数/总构建数，从 CI 日志或缓存服务端统计取数；掉到 0 与掉一半的排查路径不同。
- 掉 0 的常见原因：1) key 里有不稳定成分——时间戳、commit hash、随机数进了 hash（一次 key 踩中全失效）；2) lockfile 真实变更（正常失效）；3) runner 架构/OS 变了（key 含 runner.os）；4) 缓存容量被 LRU 淘汰（存量超限）。
- 掉一半：某些包频繁变更把共享缓存挤出（大包产物把容量占满）；或分支间 key 不共享导致首建 miss——策略上 main 与 PR 分开、restore-keys 兜底。
- 防御：key 回归测试（RBL-165）、命中率监控告警（连续 N 次 <阈值报警）、key 版本化便于事故时快速 bump。
- 追问钩子：能说出"先看一个真实 miss 的 job 的 key，逐项 diff 上次命中的 key"这一具体排查动作，比泛泛而谈强得多。

```bash
# 实战排查脚本思路：取出同一 job 最近两次构建的 key 并 diff
# CI 日志约定输出：CACHE_KEY=build-ubuntu-lock-abc123-src-def456-v3
grep -o 'CACHE_KEY=[^ ]*' job-1400.log > k1   # 上次（命中过）
grep -o 'CACHE_KEY=[^ ]*' job-1800.log > k2   # 这次（miss）
diff k1 k2
# diff 显示 src 段变化 → 再用 scripts/build-fingerprint.mjs 分别对两次 commit
# 跑一遍，逐目录 hash 对比，定位是哪个目录的哪个文件造成 miss：
# node scripts/tree-diff.js commitA commitB --path packages/web/src
```
