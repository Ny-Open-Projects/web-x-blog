---
title: [R19-032] 实现一个支持取消和竞态处理的 useFetch？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-032：实现一个支持取消和竞态处理的 useFetch？
**答**：
- 返回 data、loading、error 三元状态，url 变化时自动重新请求。
- 用 AbortController 在清理函数里取消旧请求，避免竞态覆盖。
- catch 中过滤 AbortError，防止取消请求被当作失败。
- 挂载中修改状态要小心组件已卸载：abort 后 setState 不再触发（React 18 起卸载后 setState 只是 no-op 不再警告）。

```jsx
import { useEffect, useState } from 'react';

function useFetch(url) {
  const [state, setState] = useState({ data: null, loading: true, error: null });

  useEffect(() => {
    const controller = new AbortController();
    setState({ data: null, loading: true, error: null });

    fetch(url, { signal: controller.signal })
      .then((res) => {
        if (!res.ok) throw new Error('HTTP ' + res.status);
        return res.json();
      })
      .then((data) => setState({ data, loading: false, error: null }))
      .catch((err) => {
        if (err.name !== 'AbortError') {
          setState({ data: null, loading: false, error: err });
        }
      });

    return () => controller.abort(); // url 变化或卸载时取消
  }, [url]);

  return state;
}
```

**评分点**：

1. `useEffect` 依赖数组必须含 `url`，cleanup 里执行取消——漏依赖导致 url 变化不重新请求，直接扣分。
2. 用 `AbortController` 并把 `signal` 传进 `fetch`，cleanup 里 `controller.abort()`——只用一个 `let cancelled` 标记位而不真正中断请求，带宽和竞态都还在，只能给部分分。
3. `catch` 中判断 `err.name === 'AbortError'` 后直接返回——不判断会把主动取消渲染成错误态，属于必扣项。
4. url 变化时立刻把 `loading` 置 true、`error` 清空、旧 data 清空——漏掉会出现"新请求还没回来但页面显示旧数据且没有 loading"的状态错配。

## 变体与延伸（补充）

**变体与延伸**：

1. 既然 cleanup 里已 abort，为什么还要过滤 AbortError？ → abort 会让 fetch reject 出 AbortError，不过滤就会被当成请求失败，页面闪一下错误态；这是"主动取消"与"真失败"的语义区分。
2. 怎样保证只采用最后一次请求的结果？ → 除 abort 旧请求外，再用自增 id 或 ref 记住 latest 序号，回包时比对不是最新就丢弃，覆盖 abort 尚未生效的竞态窗口。
3. url 不变但参数对象变了，依赖数组怎么写？ → 依赖里放序列化后的 query 字符串或原始类型字段；直接放对象会因引用每次新建而无限重请求，这是最常见的踩坑点。
