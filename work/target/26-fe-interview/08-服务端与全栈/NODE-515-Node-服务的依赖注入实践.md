---
title: [NODE-515] Node 服务的依赖注入（DI 容器）实践与取舍如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-515：依赖注入实践与取舍
**答**:
- 为什么 DI：可测试性（依赖可替换 mock NODE-333）、生命周期集中管理（单例/请求级作用域显式化）、依赖关系可视化（防循环依赖）。
- Node 的取舍：完整 IoC 容器（NestJS 内建——大型结构化项目）vs 手工构造注入（createApp({ db, svc })——中小服务够用且零魔法）。决策：注入复杂度 < 3 层手工即可；超过（服务群/多实现切换）上容器。
- 请求级作用域：单例（连接池/缓存）与请求级（用户上下文/事务）分离——请求级用 ALS 实现隐式注入（NODE-421）或显式 ctx 传参（推荐显式——可追踪）。
- 配置注入：config 作为依赖注入（构造参数）而非直接读 process.env 散落（NODE-362 收口）。
- 防滥用：DI 不是目的——过度抽象（接口只有一个实现且不会多实现）是过度设计（ARC-400 判断力）；注入边界 = 可替换的真实需求点（DB/外部服务/时钟）。
```javascript
// 手工注入（中小服务推荐）
export function createApp({ db, redis, clock = systemClock, config }) {
  const orderRepo = new PgOrderRepo(db);
  const paySvc = new PaySvc({ orderRepo, clock, config });        // clock 可注入（测试固定时间）
  return express().use(routes({ paySvc }));
}
// 测试：createApp({ db: memDb, clock: fakeClock(2026-11-19) })   // 依赖可替换
```
