---
title: [R19-081] 表单状态和全局状态（store）的边界怎么划？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-081：表单状态和全局状态（store）的边界怎么划？
**答**：
- 判定核心是生命周期与消费范围：表单草稿的生命周期 = 本次填表过程，消费范围 = 本表单，就留在本地。
- 只有两个信号才升级进 store：提交后才成为全局事实（如用户资料）、或跨页面/跨组件消费（如购物车）。
- 反模式：每个 keystroke 都同步进 Zustand——全局订阅者疯狂重渲染，且中途离开页面会污染全局。
- 标准姿势：本地持有 draft，提交动作成功的那一刻才写入全局。

```jsx
// 表单状态 vs 全局状态：判定原则——生命周期与消费范围
import { useState } from 'react';
import { useUserStore } from './store';

function ProfileForm({ user }) {
  const updateUser = useUserStore(s => s.updateUser);  // 全局：跨页面消费、提交后才生效

  // 表单草稿只属于本表单生命周期 → useState 本地持有
  const [draft, setDraft] = useState(() => ({
    nickname: user.nickname,
    email: user.email,
  }));

  const submit = async (e) => {
    e.preventDefault();
    await updateUser(draft);            // 提交那一刻才写入全局 store
    // 校验失败、中途离开都不会污染全局状态
  };

  return (
    <form onSubmit={submit}>
      <input value={draft.nickname} onChange={e => setDraft({ ...draft, nickname: e.target.value })} />
      <button>保存</button>
    </form>
  );
}
// 反例：把每个 keystroke 都同步进 Zustand → 全局订阅者疯狂重渲染
```
