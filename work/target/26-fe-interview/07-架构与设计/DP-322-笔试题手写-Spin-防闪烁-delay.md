---
title: [DP-322] 笔试题：手写 Spin 防闪烁（delay + 全局嵌套计数）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-322：笔试题：手写 Spin 防闪烁（delay + 全局嵌套计数）？
**答**：实现 Spin：1) delay 300ms 防闪烁（请求快完成不闪 loading）；2) delay 内完成则完全不显示；3) 全局 Spin 嵌套计数（N 个并发请求共享一个全屏 loading）；4) 组件卸载清理。
**评分点**：
- 延迟显示逻辑正确（setTimeout + cleanup）。
- 计数归零才隐藏。
- 卸载清理定时器与计数。
- 全局 Spin 单例挂载（portal）。
```tsx
let globalCount = 0;
let setGlobal;
function GlobalSpinHost() {                       // 3) 计数
  const [on, setOn] = useState(false);
  setGlobal = setOn;
  return on ? createPortal(<div className="spin-global"><Spinner/></div>, document.body) : null;
}
function useGlobalSpin(spinning, delay = 300) {
  const timer = useRef();
  useEffect(() => {
    if (!spinning) return;
    const t = setTimeout(() => { globalCount++; setGlobal?.(true); }, delay);   // 1)
    return () => { clearTimeout(t);              // 2) delay 内完成不显示
      if (globalCount > 0 && --globalCount === 0) setGlobal?.(false); };        // 3) 归零隐藏
  }, [spinning, delay]);
}
// 用：<GlobalSpinHost/> 挂根；组件里 useGlobalSpin(isLoading)
```
