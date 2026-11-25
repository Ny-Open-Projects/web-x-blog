---
title: [FRP-171] Vue 与 React 的"GC 友好度"对比：响应式自动清理 vs fiber 释放？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-171：Vue 与 React 的"GC 友好度"对比：响应式自动清理 vs fiber 释放？

**答**：
- Vue 的优势在**响应式图自清理**：组件卸载 → scope.stop() 自动把该组件所有 effect 从依赖集合剪除——store 里的数据变化不会再引用已卸载组件，悬挂引用在框架层被消灭。
- React 的 fiber 本身是可释放的：commit 后 alternate 交换、旧 fiber 与 hooks 链随引用消失可被 GC；但**外部订阅**要靠开发者手动 cleanup——忘写 useEffect cleanup 就泄漏。
- 泄漏形态不同：React 泄漏 = 外部 store 长持 fiber 闭包（组件树整棵滞留内存）；Vue 泄漏主要剩两类——手动创建且脱离 scope 的 effect、手动挂在全局的 watch。
- 两者共同的高危点：定时器/事件监听/DOM 引用这类**非响应式资源**都需要手动清理，框架帮不了。

```javascript
// 简化实现，帮助理解两种内存模型
// —— React：泄漏靠人守 ——
function Clock() {
  const [now, setNow] = useState(Date.now());
  useEffect(() => {
    // 忘了 cleanup 的版本：
    // setInterval(() => setNow(Date.now()), 1000);   // 组件卸载后仍跑 -> 闭包持 fiber -> 泄漏
    const id = setInterval(() => setNow(Date.now()), 1000);
    return () => clearInterval(id);                  // 手动断开
  }, []);
  return <span>{now}</span>;
}
// 泄漏链：interval -> setNow 闭包 -> fiber -> 整棵组件树 + hooks 链 无法回收

// —— Vue：依赖自动剪除 ——
const store = reactive({ tick: 0 });
// 组件 setup：
const scope = effectScope();
scope.run(() => {
  watchEffect(() => console.log('tick', store.tick));  // 自动注册进 scope
});
// 组件卸载：框架自动 scope.stop() —— 从 store 的依赖集合里剪除该 effect
// 结果：store.tick++ 不再触发已卸载组件的任何代码，响应式图无悬挂引用
setInterval(() => store.tick++, 1000);                  // 这个仍要自己清（非响应式资源）

// —— React 的 fiber 释放本身是健康的 ——
function commitRoot() {
  // 双缓冲交换后，旧 workInProgress 树失去全部引用：
  // alternate 断开、effectList 清空 -> 可被 GC
  root.current = finishedWork;
  finishedWork.alternate = null;
  // 泄漏只发生在"外部世界"还持有 fiber 引用时：
  // devtools 缓存、全局事件回调闭包、未清理的 store 订阅
}

// —— 对比结论 ——
// 响应式依赖（Vue 强项）：自动清理 vs 手动 cleanup
// fiber/实例内存（React 强项）：树结构整体可释放 vs Vue 实例较小但依赖图常驻
// 共同短板：定时器/监听器/第三方实例 —— 都要手动管理
```
