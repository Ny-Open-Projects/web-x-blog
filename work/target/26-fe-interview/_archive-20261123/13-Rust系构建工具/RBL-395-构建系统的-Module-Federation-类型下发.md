---
title: [RBL-395] Module Federation 类型下发的构建实现
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-395：Module Federation 类型下发的构建实现

**答**:
- 问题：MF 消费远程模块无类型（体验黑洞）——类型下发 = remote 构建时产出 dts → 发布到类型服务 → host 构建/开发时拉取映射为虚拟模块
- 构建实现：remote 侧：exposes 模块生成 dts（api-extractor 或 tsc 分散）→ 打包类型清单发布；host 侧：类型服务代理（TS paths 指向本地缓存的 dts）
- 一致性风险：类型与实现漂移（remote 更新了接口但类型没重发）——类型发布与产物发布同流水线（原子发布契约）+ host 侧类型版本校验（运行时与类型版本比对告警）
- 降级：类型服务不可用 → host 侧 any 兜底 + 提示（开发不阻断）

```text
链路：remote dts 生成 → 类型服务发布 → host 虚拟模块映射
一致性：类型与产物原子发布 + 版本校验告警
降级：服务不可用 → any + 提示
```
