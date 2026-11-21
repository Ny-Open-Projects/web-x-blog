---
title: [RBL-334] 构建产物与 HTTP 缓存策略联动
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-334：构建产物与 HTTP 缓存策略联动

**答**:
- 黄金组合：contenthash 文件名 + immutable + max-age=1y（产物）；html 不缓存或 short（入口每次校验）——产物变 = URL 变，天然缓存安全
- 构建配合：hash 分层正确（runtime 独立 chunk，业务变更不污染 runtime hash）；不要在产物内容里放构建时间戳（破坏缓存）
- 边界：HTML 里引用的产物 URL 由 manifest 注入（部署系统生成 html）——html 与产物版本必须原子发布（半更新 = 引用旧 hash 已删除产物 = 白屏）
- 验证：线上拉真实响应头核对 + 回滚演练（旧 html 引用旧产物，产物保留 N 版本）

```text
策略：产物 immutable+1y / html no-cache / manifest 注入引用
红线：html 与产物原子发布；产物保留 N 版本支持回滚
```
