---
title: [R19-421] 笔试：手写 useSyncExternalStore 简版
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 状态管理]
type: 笔试题
---

## R19-421：笔试：手写 useSyncExternalStore

**答**：实现 useSyncExternalStore 核心语义：① subscribe 建立订阅（effect 中）；② getSnapshot 读取——每次渲染检查快照是否变化（不等则强制重渲染）；③ 快照稳定性校验：同一次渲染内两次 getSnapshot 不等则警告（不稳定快照导致死循环的防护）；④ unsubscribe 在 cleanup。写出实现（简化版，用 useRef + useEffect）。

```javascript
function useSyncExternalStoreShim(subscribe, getSnapshot) {
  const [, force] = useReducer((c) => c + 1, 0);
  const lastRef = useRef(getSnapshot());

  // 渲染期一致性检查: 快照必须稳定
  const snap = getSnapshot();
  if (!Object.is(snap, lastRef.current)) {
    lastRef.current = snap;                         // 快照变了 → 强制重渲染
    force();
  }

  useEffect(() => {
    const check = () => {
      const next = getSnapshot();
      if (!Object.is(next, lastRef.current)) {
        lastRef.current = next;
        force();                                    // 外部变更 → 重渲染
      }
    };
    check();
    const unsub = subscribe(check);
    return unsub;                                   // cleanup 必须返回 unsubscribe
  }, [subscribe, getSnapshot]);

  return lastRef.current;
}
// 关键约束: getSnapshot 必须返回缓存引用(不能每次新建对象)
// 否则 Object.is 永不相等 → 无限重渲染
```

**评分点**：
- 渲染期快照一致性检查（防撕裂的核心）
- 订阅回调中比较 → force 重渲染
- cleanup 返回 unsubscribe
- getSnapshot 引用稳定性的约束说明（死循环防护）
