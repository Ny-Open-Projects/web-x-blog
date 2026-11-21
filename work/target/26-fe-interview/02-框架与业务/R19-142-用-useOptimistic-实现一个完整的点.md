---
title: [R19-142] 用 useOptimistic 实现一个完整的点赞+评论列表？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-142：用 useOptimistic 实现一个完整的点赞+评论列表？
**答**：
- useOptimistic(state, reducer)：读取时把 pending action 用 reducer 叠加在真实 state 上展示，transition 结束后叠加层自动清空。
- 更新必须在 `startTransition`（React 19 支持 async transition）内进行：先 addOptimistic，再 await 真实请求。
- 失败处理：请求抛错时 React 回滚到真实 state，配合 catch 里的 toast 提示即可，无需手动回滚代码。
- 注意 useOptimistic 不能在列表项"各自持有一份真实值"时使用——真实值必须来自同一父级 state，否则回滚后不一致。

```jsx
// Feed.jsx —— useOptimistic 点赞 + 评论列表实战
import { useOptimistic, useState, startTransition, useRef } from 'react';

export function Feed({ initialPosts }) {
  const [posts, setPosts] = useState(initialPosts);
  const inputRef = useRef(null);

  // 乐观层：对真实 posts 做"叠加式"变更
  const [optimisticPosts, addOptimistic] = useOptimistic(
    posts,
    (current, action) => {
      switch (action.type) {
        case 'like':
          return current.map(p =>
            p.id === action.id
              ? { ...p, likes: p.likes + 1, liked: true }
              : p,
          );
        case 'comment': {
          const target = current.find(p => p.id === action.postId);
          const patched = { ...target, comments: [...target.comments, action.comment] };
          return current.map(p => (p.id === action.postId ? patched : p));
        }
        default:
          return current;
      }
    },
  );

  function like(postId) {
    startTransition(async () => {
      addOptimistic({ type: 'like', id: postId });       // 1. 先乐观展示 +1
      const res = await fetch(`/api/posts/${postId}/like`, { method: 'POST' });
      if (!res.ok) throw new Error('点赞失败');           // 2. 失败自动回滚
      setPosts(prev => prev.map(p => (p.id === postId ? { ...p, likes: p.likes + 1, liked: true } : p)));
    }).catch(() => alert('点赞失败，已恢复'));
  }

  function comment(postId) {
    const text = inputRef.current.value;
    if (!text.trim()) return;
    startTransition(async () => {
      addOptimistic({ type: 'comment', postId, comment: { id: Date.now(), text } });
      await fetch(`/api/posts/${postId}/comments`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });
      setPosts(prev => prev.map(p =>
        p.id === postId
          ? { ...p, comments: [...p.comments, { id: Date.now(), text }] }
          : p,
      ));
      inputRef.current.value = '';
    }).catch(() => alert('评论发送失败'));
  }

  return (
    <div>
      {optimisticPosts.map(post => (
        <article key={post.id}>
          <button onClick={() => like(post.id)} disabled={post.liked}>
            {post.liked ? '已赞' : '赞'} {post.likes}
          </button>
          <ul>
            {post.comments.map(c => <li key={c.id}>{c.text}</li>)}
          </ul>
          <input ref={inputRef} placeholder="写评论..." onKeyDown={e => e.key === 'Enter' && comment(post.id)} />
        </article>
      ))}
    </div>
  );
}
```
