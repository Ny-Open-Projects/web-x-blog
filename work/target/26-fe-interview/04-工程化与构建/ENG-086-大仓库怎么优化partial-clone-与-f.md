---
title: [ENG-086] 大仓库怎么优化？partial clone 与 fetch depth 怎么用？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-086：大仓库怎么优化？partial clone 与 fetch depth 怎么用？
**答**：
- 浅克隆 --depth 1 只拉最近一次提交的快照，CI 场景提速最明显；增量用 git fetch --depth 1 origin main。
- partial clone --filter=blob:none 先拉提交与树、blob 按需下载，checkout 时才取需要的文件内容。
- sparse-checkout 只检出需要的子目录，monorepo 单包开发者不必拉全仓工作区。
- 组合使用最有效：clone --filter=blob:none --no-checkout + sparse-checkout set + 单分支 fetch 配置。

```bash
# 1. 浅克隆：CI 最常用，只拉最新一次提交
git clone --depth 1 --branch main https://github.com/org/repo.git

# 2. partial clone：提交与树全量，blob 按需下载
git clone --filter=blob:none --no-checkout https://github.com/org/repo.git

# 3. sparse-checkout：只检出需要的目录
cd repo && git sparse-checkout set --cone frontend packages/ui
git checkout main

# 4. 收窄 fetch 范围：只跟踪 main，减少本地引用体积
git config remote.origin.fetch '+refs/heads/main:refs/remotes/origin/main'
git fetch --prune origin
```

---

## 第二十章 环境与配置管理（ENG-087 ~ ENG-092）
