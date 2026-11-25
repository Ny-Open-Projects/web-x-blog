---
title: [ARC-328] 笔试题：实现组件库的 Spin 与 Suspense 组合降级？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-328：笔试题：实现组件库的 Spin 与 Suspense 组合降级？
**答**：实现 `Spin` 组件与延迟 loading 组合：1) loading 显示 Spin，超过 300ms 才显示（防闪烁）；2) 支持包裹模式（children 遮罩）与独立模式；3) delay 期间请求完成则不显示任何 loading；4) 全局单例 Spin（全屏 loading）支持嵌套计数。
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

## 变体与延伸（补充）

**变体与延伸**：

1. 多个并发请求的延迟计时怎么算？→ 用全局挂起计数，从 0 变 1 时开始计时，归零才隐藏，避免每个请求各起一个定时器，计数与定时器都要在卸载时干净释放。
2. SSR 下全屏遮罩怎么处理？→ 只在客户端挂载后 portal 渲染，服务端输出占位，避免 hydration 不匹配，首屏本就该加载时直接渲染，不再走延迟逻辑。
3. 无障碍上要注意什么？→ 容器加 aria-busy，遮罩用 role=status 并带加载文本，reduced-motion 下减少动画，读屏播报只在开始与结束各一次。
