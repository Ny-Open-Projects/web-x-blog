---
title: [R19-040] Suspense 的工作原理是什么？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-040：Suspense 的工作原理是什么？
**答**：
- 子组件渲染时如果数据未就绪，可以 throw 一个 Promise，React 捕获后展示最近的 Suspense fallback。
- Promise resolve 后 React 重新尝试渲染该子树，然后替换 fallback。
- 数据源可以提前在组件树外创建，实现"请求先于渲染"，减少请求瀑布。
- 多个 Suspense 边界可以分段加载，各边界独立展示骨架屏。

```jsx
// Suspense 原理的最小实现：promise 未完成时 throw 出去
function createResource(promise) {
  let status = 'pending';
  let result;
  const suspender = promise.then(
    (value) => {
      status = 'success';
      result = value;
    },
    (error) => {
      status = 'error';
      result = error;
    }
  );
  return {
    read() {
      if (status === 'pending') throw suspender; // 触发 suspend
      if (status === 'error') throw result;
      return result;
    },
  };
}

const userResource = createResource(fetchUser());

function Profile() {
  const user = userResource.read();
  return <h1>{user.name}</h1>;
}

export default function App() {
  return (
    <Suspense fallback={<p>加载中...</p>}>
      <Profile />
    </Suspense>
  );
}
```
