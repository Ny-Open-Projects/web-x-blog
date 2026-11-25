---
title: [HW-185] 手写跨列表拖拽——dataTransfer 传 id + 拖入高亮判定 + 跨列表 splice 移动（含空列表落点）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-185：手写跨列表拖拽——dataTransfer 传 id + 拖入高亮判定 + 跨列表 splice 移动（含空列表落点）
**答**：任务看板跨列拖拽：dataTransfer.setData 传任务 id（跨列表数据载体）；dragover 的 dropEffect 与高亮判定（列表容器 dragover 必须 preventDefault 才允许 drop）；空列表的落点（容器级 drop 处理——无子元素可命中）；跨列表移动 = 源列 splice 移除 + 目标列 splice 插入（不可变更新 HW-099）。

```javascript
function enableKanban(listEl, onMove) {
  listEl.addEventListener('dragstart', (e) => {
    const item = e.target.closest('[data-task]');
    if (!item) return e.preventDefault();
    e.dataTransfer.setData('text/task', item.dataset.task);
    e.dataTransfer.effectAllowed = 'move';
    item.classList.add('dragging');
  });
  listEl.addEventListener('dragend', (e) => e.target.closest('.dragging')?.classList.remove('dragging'));
  listEl.addEventListener('dragover', (e) => {
    e.preventDefault();                                   // 必须：允许 drop
    e.dataTransfer.dropEffect = 'move';
    listEl.classList.add('drop-target');                  // 高亮：整列可放
  });
  listEl.addEventListener('dragleave', (e) => {
    if (!listEl.contains(e.relatedTarget)) listEl.classList.remove('drop-target');   // 子元素间移动不闪
  });
  listEl.addEventListener('drop', (e) => {
    e.preventDefault();
    listEl.classList.remove('drop-target');
    const taskId = e.dataTransfer.getData('text/task');
    if (!taskId) return;
    // 落点计算：目标元素半线判定（HW-106）；空列表：直接插头部
    const afterEl = [...listEl.querySelectorAll('[data-task]')].find((el) => {
      const r = el.getBoundingClientRect();
      return e.clientY < r.top + r.height / 2;
    });
    onMove(taskId, listEl.dataset.list, afterEl?.dataset.task ?? null);   // (id, toListId, beforeId)
  });
}
// onMove 内部做不可变数据更新：源列 remove + 目标列 insert（splice 双操作）
// 空列表：querySelectorAll 为空 → afterEl null → 插入头部
// dragleave 的 relatedTarget 判定：防止子元素间移动时高亮闪烁（只在真正离开列表时清除）
```

**评分点**：
- dataTransfer 传 id（跨列表数据载体）与 effectAllowed/dropEffect 配对。
- dragover 必须 preventDefault 才能触发 drop——本题高频考点。
- 空列表落点（容器级 drop + null beforeId 插头部）。
- dragleave relatedTarget 防闪烁。
