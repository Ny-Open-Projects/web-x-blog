---
title: [MFW-288] ISR 页面的 Link 预取一致性（prefetch 到旧页）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-288：ISR 预取一致性

**答**:
- 现象：用户停留列表页期间，Link prefetch 拉到的详情 RSC 是「当刻缓存版」——等用户真正点击导航时内容又更新过（再生成发生在停留期间）→ 客户端 Router Cache 里是旧 payload
- 语义澄清：Router Cache 的 staleTime（默认动态 30s/静态 5min）决定 prefetch 复用窗口——窗口内不重拉是设计（省流量）非 bug
- 调优：关键新鲜度页面 autoRevalidate（实验）或客户端进详情前手动 router.refresh 语义组件；把详情页 staleTime 调短（秒级）
- 产品解法：列表页展示「更新于 x 分钟前」（期望管理）+ 详情页顶部「内容可能有更新，点击刷新」横幅（数据源年龄透出）

```javascript
// 详情路由段调短 Router Cache
export const revalidate = 10                // ISR 也短
// 或关键页禁客户端缓存复用（实验配置/autoRevalidate）
// 兜底 UX：详情页数据龄横幅（generatedAt 透出）
```
