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

**追问**：

1. 表单草稿需要跨路由保留（比如分步表单）怎么办？→ 提到模块级 store 但单独开 draft 命名空间，并在离开流程时清理；或者用 sessionStorage 持久化，不要混进业务实体 store，否则别处会读到未提交的半成品。
2. 受控表单每个 keyStroke 都 setState，性能真的有问题吗？→ React 会批处理，主要成本是本组件重渲一遍；真正出问题的是大表单（几百个字段）用一个大 state 对象，应改 `useReducer` 或非受控 + ref，缩小渲染范围。
3. 提交成功后 draft 和 store 不一致怎么收敛？→ 以提交接口返回值为准重置 draft，或提交后重新拉取详情；走乐观更新时要保留回滚快照，失败时把 draft 恢复成提交前的值。
