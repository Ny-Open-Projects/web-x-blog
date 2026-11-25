---
title: [FRP-160] 用 key 重置组件状态的所有用法与底层原理是什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-160：用 key 重置组件状态的所有用法与底层原理是什么？

**答**：
- 原理：reconcile 阶段比较同位置子元素的 **key**，key 不同 → 视为不同组件 → 旧组件 unmount（state/hooks/DOM 全部丢弃）→ 新组件从零 mount——"重置"因此是彻底的、同步的。
- 用法一：数据源切换重置，`<Profile key={userId} />` 换人即重置；用法二：表单重置 `<Form key={draftId} />`；用法三：路由级刷新 `key={location.pathname}`。
- 用法四：错误恢复 `<Boundary key={retryCount} />`，重试次数变化作为 key 强制重建边界内子树。
- 对比手动重置（useEffect 里清 state）：key 重置在 commit 内一次完成，**无中间态闪现**、无 effect 时序问题、清理函数自动执行。

```javascript
// 简化实现，帮助理解 key 触发的"销毁重建"
function reconcileChildren(parent, newChildren) {
  for (const child of newChildren) {
    const old = parent.children.find(c => c.key === child.key); // 同 key 才复用
    if (old && sameType(old, child)) {
      // 复用：fiber 保留（state 保留），走更新路径
      reconcile(old, child);
    } else {
      if (old) unmount(old);     // 旧 key 的实例：完整卸载（state 丢弃、cleanup 执行）
      mount(child);              // 新 key：从零 mount（useState 初始值重新生效）
    }
  }
}

// —— 用法速查 ——
// 1. 数据源切换
<UserProfile key={userId} />            // userId 变 -> 整个组件重建，包括内部缓存
// 2. 草稿表单
<DraftEditor key={draftId} />           // 新建草稿 -> 表单回到初始值
// 3. 路由级刷新（保留组件但强制重置状态）
<Routes key={location.pathname} />      // 每次导航都重建页面组件
// 4. 错误恢复
<ErrorBoundary key={attempt} onRetry={() => setAttempt(a => a + 1)} />

// —— 对比手动重置方案 ——
function EditorManual({ draftId }) {
  const [title, setTitle] = useState('');
  useEffect(() => { setTitle(draft.initial); }, [draftId]); // 问题：先渲染旧值再清，闪现
  // ...
}
function EditorByKey({ draftId }) {
  return <DraftEditorInner key={draftId} />;  // commit 内完成：无中间帧、cleanup 自动跑
}
// 注意代价：key 重置 = 全新 mount，子树所有 effect 重新执行、DOM 重建；
// 大子树高频切换时要用惰性初始化/受控恢复代替。
```

## 二十四、状态库与数据流原理对比

## 追问（补充）

**追问**：

1. key 变化时旧子树的 effect 清理和新子树的 effect 谁先执行？ → 同一个 commit 内先对旧树全部执行 cleanup（子先父后），再 mount 新树、按顺序跑 effect；因为都在 commit 内完成，用户看不到中间帧，这也是它优于手动 reset 的关键。
2. 什么情况下不该用 key 重置？ → 子树很大且需要保留 DOM、滚动位置、焦点时不该用，因为 key 重置等于全量重建 DOM、重跑所有 effect；这种场景应用 ref 暴露的 reset 方法只清数据。
3. 同一位置 key 相同但组件类型变了，state 会保留吗？ → 不会。复用条件是 key 相同**且** type 相同，type 不同一律 unmount 再 mount，这就是条件渲染里三元切换两个组件会丢 state 的源码原因。
