---
title: [MFW-313→MFW-313] App Router 测试金字塔落地
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-313：App Router 测试金字塔

**答**:
- 三层：①单元（Action/数据函数纯逻辑，mock 注入）②路由集成（渲染工具跑 RSC 树断言关键结构 + Next 测试服务器的缓存语义 mock——tag/重验证行为可断言）③E2E prod 冒烟（build+start 走关键路径——缓存头/ISR/重定向全链真语义）
- Next 特有 mock 纪律：fetch mock 必须保留 tag/revalidate 通道（裸 msw 会丢缓存语义——用 next 自带缓存 mock 或包装层透传）
- 断言重心：路由级测「数据域分派正确」（该静态的静态——build 标记断言）而非组件像素；Action 测「权限+校验+副作用」三件
- 比例与门槛：单元 70 / 集成 20 / E2E 10；E2E 只锁不可拆关键流（下单/支付/登录）

```text
三层：单元（Action 三件）→ 集成（RSC 结构+缓存语义 mock）→ prod E2E（头/ISR 真语义）
红线：缓存类断言只在 build+start 下有效
```
