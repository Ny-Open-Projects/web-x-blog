---
title: [WCN-833] Signals 标准化后，对现有库（Preact/Solid）的 breaking changes 如何应对？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-833：Signals 标准化后，对现有库（Preact/Solid）的 breaking changes 如何应对？

**答**：
- 结论先行：标准 API 与现有库的差异主要在「命名、相等性、调度归属、底层 Watch 语义」——应对之道是「适配层隔离 + 渐进迁移 + 双 API 并存」，别让业务代码直接绑定某一版实现。
- 常见差异点：标准用 `Signal.State/Computed`（get/set），Preact 用 `signal(v)` + `.value`，Solid 用 `createSignal` 返回 `[get,set]`；相等性策略、批量时机也可能不同。
- 应对策略：① 业务代码统一依赖自研适配层的 get/set 语义；② 用特性探测在原生与 polyfill 间切换；③ 迁移期新旧 API 并存（adapter 同时暴露两套），按模块逐步切换；④ 用 codemod 辅助机械替换。
- 风险控制：关注标准 Stage 变化，Pin 住 polyfill 版本，阅读 migration guide；对关键行为（相等性、批处理）写契约测试，保证迁移前后行为一致。
- 追问钩子：面试官会问「标准还没定就迁移会不会白做」——答：所以要用适配层把「业务语义」与「底层实现」解耦，迁移只换壳不动业务；这也是依赖倒置的价值。

```javascript
// 适配层：统一 get/set 语义，屏蔽底层 API 差异
function createAdapter(impl) {
  if (impl === 'tc39') {
    const S = globalThis.Signal;
    return {
      signal: (v) => { const s = new S.State(v); return { get: () => s.get(), set: (n) => s.set(n) }; },
      computed: (fn) => { const c = new S.Computed(fn); return { get: () => c.get() }; },
    };
  }
  // preact 风格
  return {
    signal: (v) => { const s = { value: v }; return { get: () => s.value, set: (n) => { s.value = n; } }; },
    computed: (fn) => ({ get: fn }),
  };
}
const api = createAdapter(typeof Signal !== 'undefined' ? 'tc39' : 'preact');
const s = api.signal(1); s.set(s.get() + 1);
```
