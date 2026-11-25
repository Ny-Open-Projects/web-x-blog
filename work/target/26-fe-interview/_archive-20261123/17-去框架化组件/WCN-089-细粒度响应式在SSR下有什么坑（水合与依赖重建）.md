---
title: [WCN-089] 细粒度响应式在 SSR 下有什么坑？水合与依赖重建怎么处理？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-089：细粒度响应式在 SSR 下有什么坑？水合与依赖重建怎么处理？

**答**：
- 坑一：服务端渲染时组件函数只跑一次、effect 不该执行——Solid 在 SSR 中跳过 render effect、Vue vapor 服务端只输出静态标记；直接复用客户端 effect 逻辑会"在服务器上执行副作用"。
- 坑二：水合时序——客户端脚本恢复 signal 值前，用户可能已交互；必须"值快照先行"（HTML 序列化状态 + 脚本恢复），Qwik 是极致方案，Solid 用 `createResource` + streaming。
- 坑三：依赖是运行时收集的，服务端收集的依赖集在客户端无意义，水合后要重新跑一次组件/绑定建立客户端依赖图（重复一次渲染逻辑）。
- 坑四：`Date.now()`/随机数等非确定性 signal 初值导致服务端与客户端快照不一致（hydration mismatch），要把这类值放到客户端-only effect。
- 实践结论：细粒度 SSR 的正确姿势 = 服务端渲染快照 + 客户端重建依赖图 + 状态序列化恢复，三者缺一都会 mismatch。

```javascript
// Solid SSR 安全写法
function Clock() {
  const [time, setTime] = createSignal(undefined); // 非确定值不参与 SSR
  onMount(() => {                                   // 只在客户端执行
    setTime(Date.now());
    const t = setInterval(() => setTime(Date.now()), 1000);
    onCleanup(() => clearInterval(t));
  });
  // 服务端输出占位，客户端水合后 effect 接管，无 mismatch
  return <span>{time() ? new Date(time()).toISOString() : '--:--'}</span>;
}
```
