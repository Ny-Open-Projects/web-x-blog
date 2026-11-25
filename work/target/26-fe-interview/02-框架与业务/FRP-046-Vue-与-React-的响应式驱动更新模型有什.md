---
title: [FRP-046] Vue 与 React 的响应式驱动更新模型有什么本质差异？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-046：Vue 与 React 的响应式驱动更新模型有什么本质差异？

**答**：
- Vue 是 **push 模型**：数据变化（Proxy 拦截）时框架**主动知道**"谁在用这份数据"，精确把相关组件的更新 job 入队，更新粒度是组件。
- React 是 **pull 模型**：setState 只表达"这里可能变了"，框架不知道谁依赖它，默认从该 fiber **向下整树重算**，靠 memo/useMemo/shouldComponentUpdate 手动拦截。
- 带来的差异：Vue 改 state 后依赖它的 computed/watch 自动精确更新；React 必须重跑函数组件（所以 React 的 render 必须是纯函数、可重复执行）。
- React 选择 pull 是为了 Concurrent（可中断重算，最新状态总是对的）；Vue3 的响应式精确性使其天然知道"最小更新范围"，两者是设计取舍而非优劣。

```javascript
// 一一对应：同一需求的两种驱动模型
// —— Vue push 模型：框架知道依赖关系，只更新用到的组件 ——
// Child.vue
// <template>{{ props.count }}</template>
// 父组件改 user.name（未被 Child 使用）时，Child 的 render effect 不会被触发

// React pull 模型：父组件 setState 后默认整棵子树重跑
import { memo } from 'react';

function Parent() {
  const [user, setUser] = useState({ name: 'a', count: 0 });
  // setName 触发 Parent 重跑 -> 默认 Child 也重跑（即使它只用 name 不用 count）
  return <Child name={user.name} />;
}

// 需要手动声明依赖边界：
const Child = memo(({ name }) => {
  console.log('child render'); // memo + 引用稳定时才被跳过
  return <span>{name}</span>;
});

// Vue3 等价物：依赖收集天然完成"自动 memo"
// const count = computed(() => state.count); // 只在 state.count 变时重算
// 总结：Vue 依赖关系显式记录在案（track），React 靠开发者用 memo 系列补充声明
```

**追问**：

1. React 为什么做不到 Vue 那样的精确更新？→ 没有运行期的依赖收集，函数组件每次执行都会重建整棵 vnode，只能在重算之后用 bailout（props/state 全等）把子树跳过，省的是 patch 而不是 render。
2. React 的 bailout 在什么情况下会整体失效？→ 父组件 render 时新建了对象/函数 props、children 写成内联 JSX、或 context value 变化，浅比较失败会穿透 `memo`，这时候整棵子树照样重算。
3. Vue 的 push 模型有没有变慢的场景？→ 一次交互触发上千个 effect 时，调度队列的排序与逐个 patch 是分散开销，不像 React 那样可以按优先级整体延后，所以 Vue 侧更依赖虚拟列表和控制更新规模。
