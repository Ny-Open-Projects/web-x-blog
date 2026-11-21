---
title: [MFW-301] Next.js 15 稳定化特性对架构决策的影响
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-301：Next 15 稳定化特性与架构影响

**答**:
- 关键稳定化与语义变化：缓存默认值反转（fetch/GET 路由默认不再缓存——「隐式缓存时代结束」，需显式声明缓存策略）、Turbopack Dev 稳定（本地体验换引擎）、Forms/useActionState 简化表单流、Request-Error 钩子（onRequestError 全局哨兵挂点）
- 架构影响：升级 15 的首要工作是「缓存审计」——旧隐式缓存依赖的页面语义全变（要么静态化声明要么接受动态默认）；建议以路由清单逐个核对 build 输出标记
- 决策建议：新项目直接 15 语义起步（显式缓存心智更健康）；存量升级当成一次「缓存策略重构专项」而非版本号 bump
- 面试表达：能说出「默认值反转改变了什么心智」比背 changelog 高一档

```text
15 三件事：缓存默认反转（显式化） / Turbopack Dev 稳定 / onRequestError 全局哨兵
升级即专项：路由级缓存策略清单核对（build 标记逐行审）
```
