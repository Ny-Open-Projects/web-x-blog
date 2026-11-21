---
title: [DP-238] 源码识别：useMemo/useRef/组件外缓存的备忘录层级？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-238：源码识别：useMemo/useRef/组件外缓存的备忘录层级？
**答**:
- 备忘录三层的生命周期差异：组件外（模块级 Map，全局共享）> useRef（实例级，随组件生灭）> useMemo（渲染级，deps 变就失效）——选错层级是缓存 bug 主因。
- 陷阱识别：useMemo 不保证语义缓存（React 可丢弃）、useRef 修改不触发渲染、模块级缓存注意 SSR 泄漏（跨请求共享）。
- 组合模式：正确做法是"缓存 key 设计 + 生命周期声明"——比如 RUM 聚合窗口用模块级 WeakMap（per-page），格式化器缓存用 useRef+lazy。
- 识别要点：面试场景题"计数器缓存放哪"——能按读写频率与生命周期选层就及格。

```typescript
// 三层备忘录对比
const moduleCache = new Map<string, Expensive>();      // 层1：全局（注意 SSR：per-request 重建）
function Component() {
  const refCache = useRef(new Map());                  // 层2：实例级（组件卸载即释放）
  const memoVal = useMemo(() => heavy(input), [input]); // 层3：渲染级（deps 变更失效）
  const get = (k) => {
    if (!refCache.current.has(k)) refCache.current.set(k, heavy2(k));
    return refCache.current.get(k);
  };
}
// SSR 陷阱：模块级缓存跨请求共享 → 用户 A 的数据泄漏给用户 B
// 正确：Next 里用 React.cache()（per-request memo）或依赖注入的 per-request store
```
