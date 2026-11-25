---
title: [R19-141] 如何封装一个 Suspense 可用的数据获取层（fetch 缓存版资源模式）？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-141：如何封装一个 Suspense 可用的数据获取层（fetch 缓存版资源模式）？
**答**：
- 资源模式三件套：发起请求返回"可读的 promise 包装"、read() 在未就绪时 **throw promise**、Suspense 捕获后显示 fallback，resolve 后重试渲染。
- 缓存以 `key -> resource` 存储：同一 key 第二次 read 直接命中，不再发请求；写入时同步放入，天然去重。
- throw promise 必须是**同一个 promise 实例**（React 内部用 promise status 判断），所以缓存对象里存的 promise 不能被重复创建。
- 错误路径：promise reject 后 read 里 rethrow，交给 ErrorBoundary；需要重试时删除缓存 key 重新发起。
- 生产环境推荐用框架级方案（TanStack Query 的 suspense 模式 / RSC），手写版用于理解机制。

```jsx
// suspense-resource.js —— fetch 缓存版资源模式
const cache = new Map(); // key -> { promise, status, result, error }

export function createResource(fetcher, key) {
  if (!cache.has(key)) {
    const record = { status: 'pending', promise: null, result: null, error: null };
    record.promise = (async () => {
      try {
        record.result = await fetcher();
        record.status = 'success';
      } catch (e) {
        record.error = e;
        record.status = 'error';
      }
    })();
    cache.set(key, record); // 立即写入缓存：并发调用同一个 key 不会重复请求
  }
  return {
    read() {
      const record = cache.get(key);
      if (record.status === 'pending') throw record.promise; // React 捕获 promise
      if (record.status === 'error') throw record.error;     // 交给 ErrorBoundary
      return record.result;
    },
    invalidate() { cache.delete(key); }, // 手动失效，下次 read 重新请求
  };
}

// UserList.jsx —— 组件侧用法
import { Suspense } from 'react';
import { createResource } from './suspense-resource';

const userResource = createResource(
  () => fetch('/api/users').then(r => r.json()),
  '/api/users',
);

function UserList() {
  const users = userResource.read(); // 未就绪时 throw promise
  return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}

export function Page() {
  return (
    <Suspense fallback={<p>加载用户中...</p>}>
      <UserList />
    </Suspense>
  );
}
```
