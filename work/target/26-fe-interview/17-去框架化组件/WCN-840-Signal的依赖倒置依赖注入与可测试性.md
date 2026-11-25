---
title: [WCN-840] Signal 的「依赖倒置」：怎么做依赖注入与可测试性设计？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-840：Signal 的「依赖倒置」：怎么做依赖注入与可测试性设计？

**答**：
- 结论先行：signal 应用常常「隐式依赖全局 signal」，导致单测互相污染——依赖倒置的做法是「通过参数/context 注入 signal 与调度器」，让组件不直接 import 全局实例，从而可替换、可隔离测试。
- 问题场景：组件内部直接 `import { authSignal } from '@/store'`——单测无法替换为假数据、并行测试串扰、SSR 下全局状态泄漏。
- 注入方式：① 构造函数/参数注入（把 signal 作为参数传入）；② context/provider 模式（WC 用 `@lit/context` 或自定义 context protocol，框架用 provide/inject）；③ 工厂函数注入依赖（createFeature(deps) 返回逻辑）。
- 可测试性：注入「假调度器」（同步 flush）让测试确定性；注入「假时钟/假网络」控制异步派生；每个测试用例新建 signal 实例，状态隔离。
- 边界：别为了注入而过度设计——全局的、真正无副作用的常量 signal（如配置）可以直接 import；需要隔离、需要替换、需要 mock 的才注入。
- 追问钩子：面试官会问「WC 里怎么做 signal 注入」——答：用 context protocol（沿 DOM 树向上查找 provider），或 ElementInternals/属性传入 store 引用，避免 import 全局单例。

```javascript
// 依赖倒置：feature 不直接 import 全局 signal，而是通过 deps 注入
import { signal, computed } from '@preact/signals-core';

function createCart({ storage, clock } = {}) {
  const items = signal([]);                         // 每个实例独立
  const total = computed(() => items.value.reduce((s, i) => s + i.price, 0));
  function add(item) { items.value = [...items.value, item]; storage?.save(items.value); }
  return { items, total, add };
}
// 生产：注入真实 localStorage / Date
const cart = createCart({ storage: localStorage, clock: Date.now });
// 测试：注入假依赖，状态完全隔离、可断言
const fakeStorage = { save: (v) => console.log('saved', v.length) };
const testCart = createCart({ storage: fakeStorage, clock: () => 0 });
testCart.add({ price: 10 });
console.log(testCart.total.value); // 10
```
