---
title: [DP-258] 源码识别：React Compiler 源码中的静态分析与自动 memo？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-258：源码识别：React Compiler 源码中的静态分析与自动 memo？
**答**:
- 静态分析：编译器对组件做数据流分析（哪些值来自 props/state、哪些可能变异），生成"依赖指纹"——把 useMemo/useCallback 的人工依赖声明自动化。
- 备忘录自动注入：编译产物把 JSX 分块 memo（每块按自己的输入指纹缓存），等价于"细粒度自动 useMemo"。
- 守卫策略：变异检测（对 props/state 的 mutation 触发保守处理——放弃该块缓存）保证正确性优先。
- 识别要点：能说清"为何手写 useMemo 常出 bug（依赖漏写）而编译器不会"——静态分析的输入完备性。

```javascript
// React Compiler 产物心智模型
// 源码：function Card({ user, onClick }) { return <div onClick={onClick}>{user.name}</div> }
// 编译产物（等价伪码）：
function Card(t0 /* user */, t1 /* onClick */) {
  const t2 = useMemo(() => {                    // 自动注入：块级备忘录
    const user = t0;                            // 输入指纹：t0 引用 + t1 引用
    return <div onClick={t1}>{user.name}</div>; // JSX 块缓存
  }, [t0, t1]);
  return t2;                                    // t0/t1 未变 → 复用缓存 JSX（skip re-render 该块）
}
// 静态分析保证：if (user.name 被本地修改) → 检测变异 → 该块不缓存（保守回退到全量渲染）
```
