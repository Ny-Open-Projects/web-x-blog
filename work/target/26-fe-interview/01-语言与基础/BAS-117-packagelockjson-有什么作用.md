---
title: [BAS-117] package-lock.json 有什么作用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-117：package-lock.json 有什么作用？
**答**：
- 锁定整棵依赖树的精确版本与下载地址，任何机器装出完全相同的 node_modules。
- package.json 的 `^1.2.3` 是版本范围，不同时间安装可能拿到不同次版本，酿成"我本地好好的"事故。
- lock 文件必须提交；CI 用 `npm ci` 严格按 lock 安装（要求 lock 与 package.json 同步），本地升级用 npm update 或显式 install 更新 lock。

```bash
npm ci             # 严格按 lock 安装，先删 node_modules，CI 首选
npm update lodash  # 在 semver 范围内升级并更新 lock
npm ls lodash      # 查看依赖树中 lodash 的实际版本
```
