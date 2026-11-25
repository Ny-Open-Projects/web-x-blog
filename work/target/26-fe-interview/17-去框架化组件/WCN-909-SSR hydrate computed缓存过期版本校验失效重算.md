---
title: [WCN-909] SSR hydrate 后 computed 缓存过期（stale cache）怎么主动失效与重算
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-909：SSR hydrate 后 computed 缓存过期（stale cache）怎么主动失效与重算

**答**：
- 结论先行：服务端算出的 computed 值被序列化带到客户端，若依赖的初始信号在 hydrate 前已变化，缓存就是过期的；必须在恢复阶段按依赖版本号校验，不一致则标脏重算。
- 协议设计：序列化时同时写入「信号值 + 版本号/时间戳」，客户端按相同顺序重建信号并恢复版本号，computed 首次读取做一次版本校验。
- 避免二次计算：若客户端重建后依赖版本与服务端一致，直接复用序列化结果（省一次昂贵计算），这就是「可恢复性」的核心收益。
- 边界：涉及时间/随机数/用户 Agent 的 computed 服务端与客户端必然不同，应标记为「不可序列化」并在 hydrate 后强制重算，否则 hydration mismatch。
- 追问钩子：面试官问「流式 SSR 分块到达时缓存怎么处理」——答：每个 island 带自己的版本戳，按块恢复并在各自 hydrate 时校验，互不影响。

```javascript
// hydrate 时按版本校验 computed 缓存
function hydrateComputed(serialized, deps) {
  const { value, versions } = serialized; // 服务端带来的值与依赖版本
  let cache = value, dirty = false;
  deps.forEach((d, i) => {
    if (d.version !== versions[i]) dirty = true; // 版本不一致 → 缓存过期
  });
  return { get value() {
    if (dirty) { cache = recompute(); dirty = false; }
    return cache;
  } };
}
function recompute() { return 'fresh-from-client'; }
const s = { value: 10, version: 2 };
console.log(hydrateComputed({ value: 'ssr', versions: [2] }, [s]).value); // ssr（复用）
s.version = 3;
console.log(hydrateComputed({ value: 'ssr', versions: [2] }, [s]).value); // fresh-from-client
```
