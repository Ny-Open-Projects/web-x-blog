---
title: [OPT-024] SWR 思想在业务中如何落地？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-024：SWR 思想在业务中如何落地？

**答**：
- SWR = stale-while-revalidate 的数据请求库化：**先用缓存渲染，再发请求校验更新**，页面切换回来即时有内容。
- 核心机制：以 key（通常是 URL）为缓存的请求去重（同一 key 并发只发一次）、聚焦时 revalidate、错误重试、乐观更新。
- React 用 `swr` / `react-query(TanStack Query)`，Vue 用 `vue-query`；关键在 key 设计：key 变化 = 数据变化 = 自动重新请求。
- 配合 `keepPreviousData` 可实现分页无闪烁翻页。

```javascript
// 一一对应：swr 库的标准落地（缓存优先 + 后台校验）
import useSWR from 'swr';

const fetcher = (url) => fetch(url).then((r) => r.json());

export default function UserProfile({ uid }) {
  // key 相同的多个组件共享缓存，只发一次请求
  const { data, error, mutate, isValidating } = useSWR(`/api/user/${uid}`, fetcher, {
    revalidateOnFocus: true,      // 窗口聚焦时静默校验
    dedupingInterval: 2000,      // 2s 内相同 key 去重
    keepPreviousData: true,      // uid 变化时先显示旧数据，分页不闪烁
  });

  if (error) return <div>加载失败 <button onClick={() => mutate()}>重试</button></div>;
  if (!data) return <div>首次加载中...</div>;

  return (
    <div>
      <h3>{data.name} {isValidating ? '(更新中...)' : ''}</h3>
      {/* 乐观更新：先改本地缓存再发请求，失败回滚 */}
      <button onClick={async () => {
        await mutate({ ...data, followed: !data.followed }, { revalidate: false });
        try {
          await fetch(`/api/user/${uid}/follow`, { method: 'POST' });
          mutate(); // 成功后校验服务端真实值
        } catch {
          mutate(data, { revalidate: false }); // 回滚
        }
      }}>
        {data.followed ? '取消关注' : '关注'}
      </button>
    </div>
  );
}
```
