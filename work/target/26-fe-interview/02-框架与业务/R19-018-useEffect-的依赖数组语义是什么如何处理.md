---
title: [R19-018] useEffect 的依赖数组语义是什么？如何处理数据请求竞态？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-018：useEffect 的依赖数组语义是什么？如何处理数据请求竞态？
**答**：
- 依赖数组声明 effect "依赖哪些响应式值"，值变化时先执行上一次的清理函数，再重新运行 effect。
- 空数组只在挂载后运行一次；不写数组则每次渲染后都运行。
- 数据请求场景要处理竞态：快速切换 userId 时，旧请求可能后返回覆盖新数据。
- 推荐用 AbortController 取消旧请求，或用 ignore 标志位丢弃过期结果。

```jsx
function Profile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const controller = new AbortController();
    let ignore = false;

    fetchUser(userId, { signal: controller.signal })
      .then((data) => {
        if (!ignore) setUser(data);
      })
      .catch((err) => {
        if (err.name !== 'AbortError') console.error(err);
      });

    return () => {
      ignore = true;
      controller.abort(); // userId 变化时取消上一次请求
    };
  }, [userId]);

  return <p>{user ? user.name : '加载中'}</p>;
}
```
