---
title: [ARC-335] 笔试题：实现组件库的 Drawer 方向与嵌套？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-335：笔试题：实现组件库的 Drawer 方向与嵌套？
**答**：实现 Drawer：1) 四方向（right/left/top/bottom）定位与尺寸（width/height 按方向应用）；2) RTL 下 left/right 语义自动翻转；3) 嵌套 Drawer（z-index 递增，遮罩不叠加变黑）；4) 打开时 body 滚动锁定（多层嵌套只解锁最外层关闭时）。
**评分点**：
- 方向→CSS 映射正确（right: right:0; width；top: top:0; height）。
- RTL 翻转用 dir 上下文而不是物理属性。
- 嵌套：z-index 基于层级计数器，遮罩透明度固定不叠加（每层 mask 独立但 background 相同会变黑 → 用 stacking 或共享 mask 计数）。
- 滚动锁计数器正确（开 +1 关 -1，归零才解锁）。
```tsx
let drawerCount = 0;
let scrollLock = 0;
function Drawer({ open, placement = 'right', width = 378, dir = 'ltr', onClose, children }) {
  useEffect(() => {
    if (open) {
      drawerCount++;
      if (++scrollLock === 1) document.body.style.overflow = 'hidden';  // 4) 计数锁
      return () => {
        if (--scrollLock === 0) document.body.style.overflow = '';
        drawerCount--;
      };
    }
  }, [open]);
  if (!open) return null;
  const flip = dir === 'rtl' ? (placement === 'right' ? 'left' : placement === 'left' ? 'right' : placement) : placement; // 2) RTL
  const style = {                                                        // 1) 方向映射
    position: 'fixed', zIndex: 1000 + drawerCount,                       // 3) 层级递增
    [flip]: 0,
    ...(placement === 'top' || placement === 'bottom' ? { height: width } : { width }),
    background: '#fff',
  } as React.CSSProperties;
  const maskStyle = { position: 'fixed', inset: 0, zIndex: 999 + drawerCount,
    background: drawerCount > 1 ? 'transparent' : 'rgba(0,0,0,.45)' };   // 3) 内层不叠黑
  return <>
    <div style={maskStyle} onClick={onClose}/>
    <div role="dialog" style={style}>{children}</div>
  </>;
}
```
