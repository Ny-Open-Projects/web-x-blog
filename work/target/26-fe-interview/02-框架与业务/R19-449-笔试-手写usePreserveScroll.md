---
title: [R19-449] 笔试：手写 usePreserveScroll（列表滚动位置恢复）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## R19-449：笔试：手写 usePreserveScroll

**答**：实现 `usePreserveScroll(listKey)`：① 离开时保存 scrollTop（sessionStorage，key 含路由）；② 返回时数据渲染后恢复（双 rAF 等 DOM）；③ 恢复基于「锚点项」校准（数据更新后高度变化的补偿）；④ 列表虚拟化兼容（恢复后触发虚拟列表重算）；⑤ 失效时间（30 分钟过期不恢复）。写出实现。

```javascript
export function usePreserveScroll(listKey, containerRef, anchorId) {
  const saved = useRef(null);

  useEffect(() => {
    const raw = sessionStorage.getItem(`scroll:${listKey}`);
    if (raw) saved.current = JSON.parse(raw);
    sessionStorage.removeItem(`scroll:${listKey}`);
  }, [listKey]);

  // 保存: 卸载时
  useEffect(() => () => {
    const el = containerRef.current;
    if (el && anchorId?.current) sessionStorage.setItem(`scroll:${listKey}`, JSON.stringify({
      top: el.scrollTop,
      anchor: anchorId.current,                        // 首个可见项 id
      ts: Date.now(),
    }));
  }, [listKey]);

  // 恢复: 数据就绪后
  function restore(itemsLoaded) {
    const s = saved.current;
    if (!s || Date.now() - s.ts > 30 * 60_000) return false;
    requestAnimationFrame(() => requestAnimationFrame(() => {   // 等 DOM 渲染
      const el = containerRef.current;
      el.scrollTop = s.top;                            // 初步恢复
      const anchorEl = document.getElementById(`item-${s.anchor}`);
      if (anchorEl) el.scrollTop = s.top + (anchorEl.offsetTop - s.top);  // 锚点校准
      itemsLoaded?.();                                 // 通知虚拟列表重算
    }));
    return true;
  }
  return { restore };
}
// 用法: 列表页卸载自动保存, 返回时 restore()
```

**评分点**：
- 保存三元组（top/锚点项/时间戳）+ 过期判断
- 双 rAF 等渲染再恢复
- 锚点项校准（数据高度变化补偿）
- sessionStorage 单次消费（removeItem 防脏恢复）
