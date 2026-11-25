---
title: [R19-439] 笔试：手写 usePageTransition（路由切换 + transition + 进度）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 路由]
type: 笔试题
---

## R19-439：笔试：手写 usePageTransition

**答**：实现 `usePageTransition(navigate)`：① 导航包 transition（旧页保持）；② isPending 驱动顶部进度条（动画：0→80% 缓慢 → 完成跳 100%）；③ 连续导航重置进度（前一个未完成即重开）；④ 超时兜底（>8s 强制完成进度条 + 提示）；⑤ 页面数据预加载与导航的编排（hover 预取 + 点击导航）。写出实现。

```javascript
export function usePageTransition(navigate) {
  const [isPending, startTransition] = useTransition();
  const [progress, setProgress] = useState(0);
  const timerRef = useRef(null);
  const timeoutRef = useRef(null);

  useEffect(() => {
    if (!isPending) {                                  // 完成: 快速到 100% 再归零
      setProgress(100);
      const t = setTimeout(() => setProgress(0), 300);
      return () => clearTimeout(t);
    }
    // 进行中: 缓慢爬升到 80%(防卡死假进度)
    setProgress(10);
    clearInterval(timerRef.current);
    timerRef.current = setInterval(() => {
      setProgress((p) => Math.min(p + Math.random() * 10, 80));
    }, 200);
    timeoutRef.current = setTimeout(() => {            // 超时兜底
      clearInterval(timerRef.current);
      setProgress(100);
    }, 8000);
    return () => { clearInterval(timerRef.current); clearTimeout(timeoutRef.current); };
  }, [isPending]);

  const go = useCallback((to, prefetch) => {
    prefetch?.();                                      // 数据预取(同步发起)
    startTransition(() => navigate(to));               // 导航低优(旧页保持)
  }, [navigate]);

  return { go, isPending, progress };
}
// 进度条: <div style={{ width: `${progress}%` }} className="topbar-progress" />
```

**评分点**：
- transition 包导航（旧页保持 + pending）
- 假进度设计（爬升到 80% 防卡死 + 完成跳 100%）
- 超时兜底与连续导航重置
- 预取与导航的编排（hover 数据先到）
