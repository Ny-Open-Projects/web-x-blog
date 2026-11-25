---
title: [MFW-259] Nuxt/SvelteKit 共同深水：payload 序列化与状态恢复
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-259：Nuxt/SvelteKit 共同深水问题

**答**:
- 共同问题一：payload 瘦身（Nuxt 的 nuxt.payload / SvelteKit 的 data 序列化进 HTML）——大对象进 payload 页面重量爆（同 MFW-237 的 Next 版本）——server 端裁剪 + 只传渲染字段
- 共同问题二：组件状态跨导航恢复——SvelteKit snapshot API 显式声明可恢复 state（不受序列化限制）；Nuxt 用 useState + key 设计——「哪些状态值得恢复」是设计题不是 API 题
- 共同问题三：server/client 双运行时代码纪律——server-only 导入误入共享模块（两端都打包——行为分裂或构建错）——lint 边界规则
- 收束：换框架不换问题——payload/状态恢复/双端边界是元框架通用三题，答案结构可互相迁移

```text
通用三题（框架无关）：
① payload 瘦身（server 裁剪渲染字段）
② 状态恢复设计（snapshot/useState key 纪律）
③ 双端边界 lint（server-only 导入误入共享模块）
```
