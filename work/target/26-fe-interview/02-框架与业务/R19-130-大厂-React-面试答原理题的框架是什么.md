---
title: [R19-130] 大厂 React 面试答原理题的框架是什么？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-130：大厂 React 面试答原理题的框架是什么？
**答**：
- 四段式：概念（一句话定性）-> 实现（机制到源码级）-> 场景（什么业务用它）-> 权衡（代价与不适用的场合）。
- 概念要能一句话说清"它解决什么问题"；实现至少到 API 语义与内部状态流转层。
- 场景给真实业务例子；权衡体现 senior 视角——没有银弹，只有取舍。
- 以 useOptimistic 为例完整演示四段式。

```jsx
// 答题框架示例：概念 -> 实现 -> 场景 -> 权衡
// 以 useOptimistic 为例：

// 1. 概念（一句话定性）
// 乐观更新：变更发起时就先展示预期结果，请求失败由 React 自动回滚。

// 2. 实现（机制层）
// useOptimistic 内部维护一个叠加层，读取时用传入的 reducer 把 pending action
// 叠加到当前 state 上；transition 结束后叠加层自动清空，回到真实值。
import { startTransition, useOptimistic } from 'react';

function LikeButton({ likes, onLike }) {
  const [optimisticLikes, addOptimistic] = useOptimistic(
    likes,
    (current, amount) => current + amount,
  );
  return (
    <button
      onClick={() =>
        startTransition(async () => {
          addOptimistic(1);              // 先渲染 +1
          await onLike();                // 失败时 React 自动回滚到真实 likes
        })
      }
    >
      {optimisticLikes}
    </button>
  );
}

// 3. 场景：点赞、购物车、消息发送等高频低风险写操作
// 4. 权衡：体验好但乐观值可能与最终值不一致；高风险操作（支付）不适合乐观
```

## 第十九章 源码级简化实现（R19-131 ~ R19-137）

本章用手写极简实现回答"它是怎么工作的"，是原理题的落地形态。

## 追问（补充）

**追问**：

1. 面试官追问「你说的实现在源码哪个位置」，怎么接？→ 说到模块与调用顺序，而不是背文件名：比如 render 阶段从 `beginWork` 进到 `updateFunctionComponent`，hook 在 `renderWithHooks` 里按链表顺序读取，能讲清先后就够，细节不确定就明说不确定。
2. 权衡那一段怎么讲才不像套话？→ 给出触发条件和量级：例如"列表超过一万行时 memo 失效，因为父级每次都新建回调 props，我们的做法是把回调提到模块级或用 useCallback 固定引用"。
3. 完全不会这道题时怎么答？→ 先界定概念边界、说出最接近的已知机制，再给出可验证的路径（查 RFC、看源码入口、写最小复现），不要为了显得懂而编造内部字段名。
