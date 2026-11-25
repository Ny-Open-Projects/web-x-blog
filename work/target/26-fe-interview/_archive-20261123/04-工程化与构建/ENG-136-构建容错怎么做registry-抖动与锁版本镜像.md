---
title: [ENG-136] 构建容错怎么做？registry 抖动与锁版本镜像怎么设计？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-136：构建容错怎么做？registry 抖动与锁版本镜像怎么设计？
**答**：
- CI 偶发失败的高频根因是 registry 抖动与第三方网络问题，要按可重试分类处理而不是盲目重跑整条流水线。
- 安装层容错：包管理器自带重试参数 + 内部 mirror 兜底（npmmirror/verdaccio），公网 registry 只作上游。
- 关键约束：版本解析必须以 lockfile 为准，镜像只缓存已解析版本，避免镜像滞后导致解析出不同版本。
- 极端预案：registry 全挂时用本地 pnpm store 或 pnpm fetch 预热的缓存完成 --offline 构建。

```ini
# .npmrc —— registry 容错与镜像策略
registry=https://registry.npmmirror.com          # 内部 mirror 作首选源
@corp:registry=https://verdaccio.corp.internal   # 内部包走私有源
fetch-retries=5                                  # 抖动重试参数
fetch-retry-mintimeout=2000
fetch-retry-maxtimeout=60000
fetch-timeout=300000
# 配套 CI 预热：每天 pnpm fetch 把 lockfile 依赖拉进镜像缓存
# registry 全挂时 CI 用 pnpm install --offline --frozen-lockfile 兜底
```

## 第二十七章 发布工程深化（ENG-137 ~ ENG-142）
