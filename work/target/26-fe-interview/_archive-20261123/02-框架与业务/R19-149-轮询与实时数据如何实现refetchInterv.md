---
title: [R19-149] 轮询与实时数据如何实现？refetchInterval 如何配合页面可视性优化？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-149：轮询与实时数据如何实现？refetchInterval 如何配合页面可视性优化？
**答**：
- TanStack Query 原生支持 `refetchInterval`：固定间隔、函数形式（按数据决定下次间隔）两种；轮询期间数据仍是缓存读，UI 无闪断。
- 必配 `refetchIntervalInBackground: false`：页面切到后台暂停轮询，回前台（`focusManager`）自动恢复并立即刷一次。
- 频率自适应：数据变化越快轮询越勤（函数式 interval 返回值），出错时退避拉长间隔。
- 更高实时性再升级为 SSE/WebSocket：服务端推送 -> `invalidateQueries`，轮询作为降级兜底。

```tsx
// use-live-dashboard.ts —— 可视性感知的自适应轮询
import { useQuery } from '@tanstack/react-query';
import { useEffect } from 'react';

export function useLiveDashboard() {
  const q = useQuery({
    queryKey: ['dashboard', 'live'],
    queryFn: async () => {
      const res = await fetch('/api/dashboard/live');
      if (!res.ok) throw new Error('fetch failed');
      return res.json();
    },
    refetchInterval: (query) => {
      const data = query.state.data as { pendingAlarms: number } | undefined;
      // 自适应：有告警 5 秒一轮，平常 30 秒一轮
      if (data && data.pendingAlarms > 0) return 5_000;
      return 30_000;
    },
    refetchIntervalInBackground: false, // 页面隐藏时暂停，省请求省电
    staleTime: 0,
  });
  return q;
}

// 手写兜底版（不依赖 Query）：visibilitychange + 自适应间隔
export function usePolling(fn: () => void, getInterval: () => number) {
  useEffect(() => {
    let timer: number | undefined;
    let stopped = false;

    function tick() {
      if (stopped || document.hidden) return; // 隐藏时跳过执行
      fn();
      timer = window.setTimeout(tick, getInterval()); // 间隔可随数据变化
    }
    function onVisible() {
      if (!document.hidden) { fn(); restart(); } // 回前台立即刷 + 重排定时器
    }
    function restart() {
      clearTimeout(timer);
      timer = window.setTimeout(tick, getInterval());
    }

    tick();
    document.addEventListener('visibilitychange', onVisible);
    return () => {
      stopped = true;
      clearTimeout(timer);
      document.removeEventListener('visibilitychange', onVisible);
    };
  }, [fn, getInterval]);
}
```
