---
title: [WCN-092] 笔试：手写 Signals 版乐观更新（Optimistic UI：先改后撤）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-092：笔试：手写 Signals 版乐观更新

**题目**：实现 `optimisticLike(store)`：① 点赞立即把 `liked=true/likeCount+1` 写入 store（乐观提交），UI 秒响应；② 请求成功后用服务端返回值校准；③ 失败自动回滚到提交前快照并提示；④ 并发多次点击时以"最后一次请求结果"为准，中间状态不覆盖已校准的值（用 pending 计数）；⑤ 返回 `{ toggle, pending }`。

**答**：

```javascript
import { createSignal, computed, untrack } from './mini.js';

export function createOptimisticLike(api) {
  const [liked, setLiked] = createSignal(false);
  const [count, setCount] = createSignal(100);
  const [pending, setPending] = createSignal(0);
  let inflight = 0;

  async function toggle() {
    const snapshot = { liked: untrack(liked), count: untrack(count) };
    const nextLiked = !snapshot.liked;
    // 乐观写入：立即生效
    setLiked(nextLiked);
    setCount(snapshot.count + (nextLiked ? 1 : -1));
    inflight++; setPending(inflight);
    try {
      const { liked: serverLiked, count: serverCount } = await api.like({ liked: nextLiked });
      inflight--; setPending(inflight);
      if (inflight === 0) {                 // 只在无并发时校准，避免中间结果覆盖
        setLiked(serverLiked); setCount(serverCount);
      }
      return true;
    } catch {
      inflight--; setPending(inflight);
      if (inflight === 0) {                 // 回滚到本次提交前快照
        setLiked(snapshot.liked); setCount(snapshot.count);
      }
      return false;
    }
  }
  return { liked, count, pending, toggle };
}
// effect(() => btn.classList.toggle('on', liked()));  // UI 直绑
```

**评分点**：
- 快照回滚语义（提交前状态），失败还原。
- inflight 计数处理并发：中间结果不覆盖，最后一个响应才校准/回滚（竞态考点）。
- 乐观写入与网络请求解耦，UI 直绑 signal 零延迟。
- untrack 读快照（避免在异步路径建立依赖）。
