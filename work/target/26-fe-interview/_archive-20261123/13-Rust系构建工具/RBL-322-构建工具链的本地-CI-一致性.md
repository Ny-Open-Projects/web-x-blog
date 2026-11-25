---
title: [RBL-322] 本地构建与 CI 构建的一致性怎么保证
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-322：本地构建与 CI 构建的一致性

**答**:
- 漂移来源：Node 版本（engines 锁定 + volta/nvmrc）、OS 差异（路径/大小写/换行）、env 差异（本地 .env vs CI secrets）、依赖安装差异（lockfile 不 frozen）
- 一致性机制：工具链容器化（devcontainer/统一 Docker 构建）或统一 runtime 管理器；构建配置中禁「读本地环境」的分支逻辑（环境差异收敛为显式 env）
- 验证手段：本地构建产物 hash 与 CI 对比（同 commit 双跑 diff）进 CI 校验——一致性是可测的
- 「本地好 CI 坏」专项排查清单：大小写文件名（linux 敏感）、缺失 env、OS 依赖（node-gyp 平台差异）、时区依赖

```text
一致性基线：engines + lockfile frozen + env 显式化 + hash 双跑对比
排查清单：大小写 / 缺 env / 平台依赖 / 时区
```
