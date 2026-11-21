---
title: [ARC-328] 笔试题：实现组件库的 Spin 与 Suspense 组合降级？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-328：笔试题：实现组件库的 Spin 与 Suspense 组合降级？
**题目**：实现 `Spin` 组件与延迟 loading 组合：1) loading 显示 Spin，超过 300ms 才显示（防闪烁）；2) 支持包裹模式（children 遮罩）与独立模式；3) delay 期间请求完成则不显示任何 loading；4) 全局单例 Spin（全屏 loading）支持嵌套计数。
**评分点**：
- 延迟显示逻辑正确（setTimeout + 卸载清理，delay 内完成不闪 loading）。
- 包裹模式遮罩层实现（相对定位 + 遮罩 + 居中 spin）。
- 全局单例嵌套计数正确（N 个请求并发 → show N 次 hide 1 次 → 计数归 0 才隐藏）。
- 清理完整（unmount 清定时器与计数）。
```tsx
function Spin({ spinning, delay = 300, children, fullscreen }) {
  const [show, setShow] = useState(false);
  useEffect(() => {
    if (!spinning) { setShow(false); return; }
    const t = setTimeout(() => setShow(true), delay);      // 1) 防闪烁
    return () => clearTimeout(t);                          // 3) delay 内完成即清理
  }, [spinning, delay]);
  if (fullscreen) return show ? createPortal(<div className="spin-global"><Icon/></div>, document.body) : null;
  if (!children) return show ? <span className="spin"><Icon/></span> : null;
  return (
    <div className="spin-wrap" style={{ position: 'relative' }}>
      {children}
      {show && <div className="spin-mask" style={{ position: 'absolute', inset: 0,
        display: 'grid', placeItems: 'center', background: 'rgba(255,255,255,.6)' }}><Icon/></div>}  // 2) 遮罩
    </div>
  );
}
// 4) 全局嵌套计数
const full = (() => { let n = 0; let setters;
  return { show() { n++; setters?.(true); }, hide() { if (--n <= 0) { n = 0; setters?.(false); } },
    bind(s) { setters = s; } };
})();
export const FullSpin = { show: full.show, hide: full.hide };
```
