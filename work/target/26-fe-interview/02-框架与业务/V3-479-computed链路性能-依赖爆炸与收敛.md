---
title: [V3-479] computed 链路性能：依赖爆炸与收敛
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## V3-479：computed 链路性能：依赖爆炸与收敛

**答**：
- 依赖爆炸形态：computed A 依赖 B，B 依赖 C...——修改底层 ref 触发整条链脏标记传播 + 顶层重算；链上任何一环依赖集合不稳定（条件分支读不同依赖）都会全链失效
- 收敛手段一：拆分细粒度 computed（每个只做单一职责），让「改 X 只重算与 X 相关的分支」而不是一个大 computed 全量重算
- 收敛手段二：控制依赖集合稳定——computed 内避免条件性读依赖（if 分支读不同 ref）；必须条件读时固定先读触发条件
- 收敛手段三：惰性确认——computed 只在「被读取」时重算（懒），无人读的链不花成本；模板里没用的 computed 不写（哪怕看起来该缓存）
- 量化：DevTools 侧用 `onRenderTriggered` + 手动 mark 链路；极端场景把热点 computed 的计算改为 ref + 显式更新（放弃自动追踪换确定性）

```javascript
// 反模式: 巨型 computed
const summary = computed(() => heavyCalc(a.value, b.value, c.value, d.value));
// 正解: 分层
const ab = computed(() => cheap(a.value, b.value));
const cd = computed(() => cheap(c.value, d.value));
const summary = computed(() => combine(ab.value, cd.value)); // 改 a 只重算 ab+summary
```
