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
