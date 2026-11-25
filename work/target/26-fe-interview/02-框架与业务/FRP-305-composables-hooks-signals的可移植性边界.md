---
title: [FRP-305] composables/hooks/signals 的可移植性边界
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## FRP-305：composables/hooks/signals 的可移植性边界

**答**：
- 三者本质差异：hooks（调用顺序绑定组件生命周期，不可脱离 React）、composables（依赖注入 + 作用域，Vue 内可复用但依赖 reactivity）、signals（独立运行时，无框架绑定）——可移植性 signals > composables > hooks
- 可移植层抽取策略：逻辑分「纯计算（框架无关）/副作用（框架绑定）」——纯计算抽 utils，状态内核抽独立库（zustand/nanostores），框架层只剩胶水
- nanostores 模式：原子 store + 各框架适配包（@nanostores/react/vue）——逻辑一次编写三端消费的代表
- 不可移植的陷阱：hooks 内的 useEffect 副作用、composables 的 inject 依赖——「逻辑复用」边界画在哪是架构决策
- 评估公式：可移植性收益 = 重复代码量 × 框架数量 - 抽象成本——两个框架以下通常不值得抽独立内核

```javascript
// nanostores 风格: 状态内核框架无关
import { atom, computed } from 'nanostores';
export const cart = atom([]);
export const total = computed(cart, (items) => items.reduce((s, i) => s + i.price, 0));
// react: useStore(total); vue: useStore(total); solid: useStore(total)
```
