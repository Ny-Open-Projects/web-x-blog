---
title: [TST-035] Vitest 专题知识体系与面试应答策略总结
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-035：Vitest 专题知识体系与面试应答策略总结
**答**：
- 知识体系四层：① 工具定位（与 Jest/Vite 的关系、选型理由）；② 核心 API（vi.mock/spyOn/fn、fake timers、快照、钩子）；③ 工程配置（workspace、setupFiles、覆盖率、环境选择）；④ 原理层（Vite 管线转换、模块拦截、提升机制）。
- 高频考察点：vi.mock 提升陷阱（TDZ + vi.hoisted）、fake timers 测异步时间逻辑、部分 mock（importActual）、与 Jest 迁移对比——这几个是「用过」和「用透」的分水岭。
- 应答框架：先说结论（选型/机制一句话），再给机制分层解释，最后落到一个真实踩坑案例（如 CI 里 only 漏测、TDZ 报错排查）。
- 场景包装：回答尽量挂在业务上（订单超时用 setSystemTime、商品列表页用 vi.mock axios），体现工程判断而不是背 API。
- 追问准备：常被追问「为什么 Vitest 快」「mock 原理能不能手写」「覆盖率怎么设门禁」——分别对应 Vite 缓存、TST-006、覆盖率专题。

```javascript
// 一图流：Vitest 知识地图（面试自查清单）
const map = {
  选型: ['对比 Jest', 'ESM 原生', 'Vite 配置复用', 'workspace'],
  API: ['vi.mock/spyOn/fn', 'hoisted', 'fake timers', 'setSystemTime', '快照', 'each', 'expectTypeOf'],
  工程: ['setupFiles', '环境 jsdom/node', 'coverage', 'CI run/--ci', '迁移清单'],
  原理: ['Vite transform 管线', '模块拦截注册表', '提升编译'],
};
// 每项都能讲出「是什么 + 为什么 + 踩坑一次」即达标。
```
