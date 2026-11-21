---
title: [WCN-266] 异步派生（computed 依赖 fetch 结果）的建模模式？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-266：异步派生（computed 依赖 fetch 结果）的建模模式？
**答**：
- 信号库原生 computed 是同步的——异步用「资源信号」模式：状态机信号（idle/loading/data/error）。
- 竞态处理：请求携带版本号，过期响应丢弃（写前校验 epoch）。
- 派生缓存：相同输入不重复请求（computed 层做 memo + in-flight 合并）。
- 与 Suspense 对接：异步信号抛 promise（资源语义）让框架层处理边界。

```javascript
const userId = signal(1);
const user = computed.async(async (id) => {
  const epoch = ++reqEpoch;
  const res = await fetchUser(id);
  if (epoch !== reqEpoch) return SKIP;   // 过期响应丢弃
  return res;
});
// 视图：user.value.state === 'loading' ? spinner : data
r
```
