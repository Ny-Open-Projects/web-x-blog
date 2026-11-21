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
