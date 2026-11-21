---
title: [FRP-099] 从订阅粒度对比 Zustand / Redux / Jotai / Context 的选型原理是什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-099：从订阅粒度对比 Zustand / Redux / Jotai / Context 的选型原理是什么？

**答**：
- **Context**：无订阅、渲染期读取，Provider value 引用变 → 所有消费者重渲染。适合低频"依赖注入"（主题/i18n），不适合高频业务 state。
- **Redux（connect/useSelector）**：单一 store + 每组件独立订阅 + selector 浅比较；通知是**全量广播**，性能靠"比较后跳过"。需要手写 selector 与记忆化，但 DevTools/中间件生态最完整。
- **Zustand**：同样是广播 + selector 比对，但去掉了 Provider/dispatch/action 样板，store 是模块级单例；选它的本质是"**Redux 的订阅模型 + 极简 API**"。
- **Jotai/Recoil**：**原子依赖图**，通知只沿依赖边传播，粒度最细（字段级），派生自动记忆化；适合大量派生状态/表单联动，代价是概念数量与调试复杂度。
- 判断口诀：**通知范围 × 比较成本 × 派生复杂度** 三轴选型——通知范围全量→订阅库，比较成本想省→原子化，需要时间旅行→Redux。

```javascript
// 简化实验，帮助理解不同订阅粒度的重渲染次数
const results = { context: 0, zustand: 0, jotai: 0 };

// 场景：state = { theme, count }，只改 count，观察 ThemeView 是否重渲染
// 1. Context：value 对象引用变 -> 所有消费者都重渲染
let ctxValue = { theme: 'dark', count: 0 };
const consume = (pick) => { results.context++; void pick(ctxValue); };
consume((s) => s.theme);            // 渲染 1
ctxValue = { theme: 'dark', count: 1 }; // 只改 count
consume((s) => s.theme);            // Context：无法跳过，重渲染 2（浪费）

// 2. Zustand：广播后 selector 比对快照，不变则跳过
const store = { theme: 'dark', count: 0 };
const zustandSub = (selector) => ({ last: selector(store), check() {
  const next = selector(store);
  if (next !== this.last) { this.last = next; results.zustand++; }
} });
const themeSub = zustandSub((s) => s.theme);
store.count = 1;                    // setState 广播
themeSub.check();                   // selector 快照 'dark' 未变 -> 跳过

// 3. Jotai：原子依赖图，通知根本不经过不相关 atom
const themeAtom = { subscribers: [], value: 'dark' };
const countAtom2 = { subscribers: [], value: 1 };
themeAtom.subscribers.push(() => results.jotai++);
countAtom2.value = 2;               // 写 countAtom：只通知 countAtom.subscribers
// themeAtom.subscribers 为空数组 -> 0 次通知，零成本

console.log(`Context 重渲染: ${results.context}（含 1 次浪费）`);
console.log(`Zustand 重渲染: ${results.zustand}（广播后比对跳过）`);
console.log(`Jotai 通知: ${results.jotai}（依赖图隔离，未广播）`);
```

## 十五、跨框架与编译原理
