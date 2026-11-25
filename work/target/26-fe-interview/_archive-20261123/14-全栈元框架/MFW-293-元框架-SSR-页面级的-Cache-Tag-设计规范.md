---
title: [MFW-293] Cache Tag 设计规范（从数据模型推导 tag 树）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 面试题
---

## MFW-293：Cache Tag 设计规范

**答**:
- tag 树从领域模型推导：`实体:id` → `实体:id:关系` → `视图:路由` 三层——写操作登记「影响闭包」（ZSM-344 失效映射表的元框架版）
- 命名纪律：tag 是代码契约（工厂函数单点定义 `postTags.detail(id)）——手写字符串散落=永不失效的缓存
- 粒度成本：tag 太细（每行一个）失效调用爆炸；太粗（全站一个）牵连重渲染——层级取「失效频率一致的数据组」
- 审计工具：构建期扫描全部 fetch 的 tag 集合 → 与写操作登记表比对（未登记的写 = 潜在脏缓存——CI 报告）

```javascript
// tag 工厂
export const tags = {
  post: { all: ['post'], of: (id) => [`post:${id}`, `user:${authorOf(id)}'`] },
  feed: (view) => [`view:${view}`],
}
// 写操作登记
const INVALIDATION = { 'POST /post': (r) => tags.post.of(r.id).concat(tags.feed('home')) }
// CI：fetch tags 集合 ⊆ 登记表展开集？未覆盖 → warn
```
