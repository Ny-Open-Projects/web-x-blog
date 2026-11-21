---
title: [MFW-254] Parallel/Intercepting Routes 的实践与坑
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-254：Parallel/Intercepting 实践与坑

**答**:
- Parallel Routes（@modal/@team 槽位）：同布局多独立流（各槽独立 loading/error）——仪表盘多面板场景；槽失败不互相污染（error.js 槽级隔离）
- Intercepting（(.)photo 从列表拦到弹窗）：URL 与 UI 解耦（分享链接直达详情页、站内点击是弹窗）——实现成本在「两套渲染都要维护」（弹窗版与整页版同组件复用）
- 高频坑：拦截路由刷新后走整页版（正确行为但用户以为 bug——弹窗状态与 URL 语义要设计一致）；@槽与子路由 children 冲突（路径重叠时匹配歧义——目录命名纪律）
- 使用建议：这两个特性是「UI 语义增强」不是常规路由——滥用（三层拦截）可读性崩塌，评审从严

```text
适用：仪表盘槽位（parallel） / 列表→详情弹窗（intercepting）
坑：刷新走整页（设计为特性）/ 槽路径重叠歧义 / 三层拦截不可维护
纪律：弹窗与整页共用组件；拦截深度 ≤1
```
