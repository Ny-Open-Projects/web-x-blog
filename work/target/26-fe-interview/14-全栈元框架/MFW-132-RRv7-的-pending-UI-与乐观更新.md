---
title: [MFW-132] RRv7 里怎么做 pending UI 和乐观更新？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-132：RRv7 里怎么做 pending UI 和乐观更新？
**答**：
- pending UI 原料：`useNavigation()` 给出导航状态与提交的 formData（`navigation.formData`），可精确到「哪个表单在提交」；配合 `useFetcher` 处理局部提交。
- 乐观更新：`useOptimistic`（React 内置）或 RRv7 的 `useAsyncValue` + fetcher 手写——RRv7 文档推荐做法是「fetcher.formData 渲染乐观值 + useOptimistic 包装」。
- 关键区别：乐观值在 **fetcher 进行中**有效，action 失败时自动回落（重新渲染真实数据），无需手写回滚——RRv7 用「数据即真相」的模型替代了手动 rollback。
- 进阶：`useRevalidator` 手动刷新、`shouldRevalidate` 控制哪些 loader 在 mutation 后重跑。

```tsx
import { useFetcher, useNavigation, useOptimistic } from 'react-router';

function LikeButton({ post }: { post: { id: string; likes: number } }) {
  const fetcher = useFetcher();

  // 乐观值：提交期间显示 likes+1，完成后回真实值
  const [optimisticLikes, addOptimistic] = useOptimistic(
    post.likes,
    (cur: number, delta: number) => cur + delta,
  );

  function like() {
    startTransition(async () => {
      addOptimistic(1);
      await fetcher.submit(
        { postId: post.id },
        { method: 'post', action: `/posts/${post.id}/like` },
      );
    });
  }

  const submitting = fetcher.state !== 'idle';
  return (
    <button onClick={like} disabled={submitting}>
      {submitting ? optimisticLikes : post.likes} 赞
    </button>
  );
}

import { startTransition } from 'react';

// 全局 pending：顶部进度条
function TopBar() {
  const navigation = useNavigation();
  return <div className={navigation.state !== 'idle' ? 'bar active' : 'bar'} />;
}
```
