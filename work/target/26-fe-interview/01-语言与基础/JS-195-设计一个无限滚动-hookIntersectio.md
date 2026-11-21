---
title: [JS-195] 设计一个无限滚动 hook？IntersectionObserver + 缓冲区怎么做？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-195：设计一个无限滚动 hook？IntersectionObserver + 缓冲区怎么做？

**答**：
- 哨兵元素放列表底部，IntersectionObserver 观察哨兵，进入视口即触发 loadMore；rootMargin 提前约一屏发起请求（缓冲），滚动全程无感加载。
- 状态机防重入：idle → loading → done/error；loading 或 done 时再次触发直接跳过，天然防抖。
- hasMore 终止：服务端返回 hasMore=false 时状态置 done，不再请求；哨兵也可 unobserve。
- 错误恢复：失败置 error，UI 显示重试按钮，点击重置 idle 触发重挂 observer 后自动重试。
- 超长列表配合虚拟滚动：只渲染可视区 + 上下缓冲，用 translateY 校准滚动位置；无限滚动负责"取数"，虚拟化负责"渲染"。

```javascript
// 1. useInfiniteScroll：哨兵观察 + 状态机 + 缓冲区（React 伪代码）
function useInfiniteScroll(fetchPage, { rootMargin = '400px' } = {}) {
  const sentinelRef = useRef(null);
  const [items, setItems] = useState([]);
  const [status, setStatus] = useState('idle');    // idle | loading | error | done
  const pageRef = useRef(0);
  const statusRef = useRef(status);
  statusRef.current = status;                      // 回调里读最新状态，避免闭包旧值

  const loadMore = useCallback(async () => {
    if (statusRef.current === 'loading' || statusRef.current === 'done') return; // 状态机防重入
    setStatus('loading');
    try {
      const { list, hasMore } = await fetchPage(pageRef.current + 1);
      pageRef.current += 1;
      setItems((prev) => [...prev, ...list]);
      setStatus(hasMore ? 'idle' : 'done');        // done 后永不再请求
    } catch (e) {
      setStatus('error');                          // 失败：UI 展示重试按钮
    }
  }, [fetchPage]);

  useEffect(() => {
    const el = sentinelRef.current;
    if (!el) return;
    const io = new IntersectionObserver(
      (entries) => entries[0].isIntersecting && loadMore(),
      { rootMargin },                              // 提前 400px 触发，缓冲加载
    );
    io.observe(el);
    return () => io.disconnect();                  // 卸载清理，防泄漏
  }, [loadMore, rootMargin, status]);              // error→idle 重挂即自动重试

  return { sentinelRef, items, status, retry: () => setStatus('idle') };
}

// 2. 组件用法
// function Feed() {
//   const { sentinelRef, items, status, retry } = useInfiniteScroll(
//     (page) => fetch(`/api/feed?page=${page}`).then((r) => r.json()),
//   );
//   return (
//     <div>
//       {items.map((it) => <Card key={it.id} data={it} />)}
//       {status === 'error'   && <button onClick={retry}>加载失败，点我重试</button>}
//       {status === 'loading' && <Spinner />}
//       {status === 'done'    && <p>没有更多了</p>}
//       <div ref={sentinelRef} style={{ height: 1 }} />  {/* 哨兵 */}
//     </div>
//   );
// }
```
