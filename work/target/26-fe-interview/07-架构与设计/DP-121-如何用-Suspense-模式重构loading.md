---
title: [DP-121] 如何用 Suspense 模式重构"loading 三件套"异步组件？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-121：如何用 Suspense 模式重构"loading 三件套"异步组件？（高频）
**答**：
- Suspense 模式的核心：组件直接"读"同步形态的数据，未就绪就 throw 一个 thenable，由最近的 Suspense 边界兜住显示 fallback——组件里不再出现 `if (loading)`。
- 落地手法：资源创建函数返回 `{ read() }`，内部缓存 Promise 结果（命中即同步返回），等效虚拟代理 + 备忘录（DP-032）。
- React 19 的 use() / 框架级 suspense 数据源已内置该机制；自实现用于理解原理与旧版本兼容。

```jsx
// 资源模式：把 Promise 包装成可"同步读"的资源（代理 + 缓存）
function createResource(promise) {
  let status = 'pending', result;
  const suspender = promise.then(
    (v) => { status = 'success'; result = v; },
    (e) => { status = 'error'; result = e; },
  );
  return {
    read() {
      if (status === 'pending') throw suspender;   // 未就绪：抛给 Suspense 边界
      if (status === 'error') throw result;        // 失败：抛给 ErrorBoundary
      return result;                               // 就绪：同步返回
    },
  };
}
const userCache = new Map();                       // 备忘录：同 key 不重复发起
function fetchUserResource(id) {
  if (!userCache.has(id)) userCache.set(id, createResource(api.getUser(id)));
  return userCache.get(id);
}
// 组件：没有 loading，没有 useEffect，直接读
function UserProfile({ id }) {
  const user = fetchUserResource(id).read();
  return <div>{user.name}</div>;
}
export default function Page() {
  return (
    <ErrorBoundary fallback={<b>加载失败</b>}>
      <Suspense fallback={<Spin />}>
        <UserProfile id={1} />
      </Suspense>
    </ErrorBoundary>
  );
}
```

**追问**：

1. read 抛 Promise 之后 React 怎么知道要重渲染，同一 resource 被两个组件读会怎样？ → 边界捕获 thenable 后在该 Promise resolve 时重试渲染；同一 resource 共享缓存只发一次请求，但 read 期间缓存被清空会让并发渲染读到不同值，造成撕裂。
2. 局部刷新会整块闪回 fallback，怎么只变暗不闪？ → 用 transition 的 isPending 或 useDeferredValue 保留旧内容，只有首次加载才进 fallback，避免在 transition 之外切 key。
3. React 19 的 use() 出来了还要自己写 createResource 吗，缓存 key 怎么设计？ → use() 直接吃 Promise，但每次渲染新建 Promise 会无限挂起，必须配合 cache 或数据层按 key 去重，key 要含请求参数与失效版本。
