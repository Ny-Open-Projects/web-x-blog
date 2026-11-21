---
title: [DP-276] 源码识别：第三方 SDK 加载器源码中的时序与竞态？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-276：源码识别：第三方 SDK 加载器源码中的时序与竞态？
**答**:
- 命令+单飞（核心）：loadScript(url) 的并发调用共享同一个 promise（loading promise 缓存）——N 个调用者只加载一次。
- 状态机：idle → loading → ready/failed，失败重试（退避）与超时兜底。
- 策略：加载策略（动态 script / import() / preload）、就绪判定策略（onload vs 轮询全局变量，防 SDK 未定义全局导出的坑）。
- 识别要点：能说出"SDK onload 后全局变量未必立刻可用（异步初始化）"的竞态与轮询/事件等待的解法。

```typescript
// 第三方 SDK 加载器（源码级简化）
const loading = new Map<string, Promise<void>>();
function loadScript(src: string, { timeout = 8000, globalKey } = {}) {
  if (loading.has(src)) return loading.get(src)!;          // 单飞
  const p = new Promise<void>((resolve, reject) => {
    const s = document.createElement('script');
    s.src = src; s.async = true;
    const timer = setTimeout(() => { s.remove(); reject(new TimeoutError(src)); }, timeout);
    s.onload = async () => {
      if (!globalKey) return clearTimeout(timer), resolve();
      // 就绪判定策略：SDK 异步初始化，轮询全局变量
      for (let i = 0; i < 100 && !(window as any)[globalKey]; i++) await sleep(50);
      clearTimeout(timer);
      (window as any)[globalKey] ? resolve() : reject(new Error(`SDK ${globalKey} not ready`));
    };
    s.onerror = () => { clearTimeout(timer); s.remove(); reject(new Error('load failed')); };
    document.head.appendChild(s);
  });
  loading.set(src, p);
  p.catch(() => loading.delete(src));       // 失败允许重试
  return p;
}
// 使用：await loadScript('https://accounts.google.com/gsi/client', { globalKey: 'google' })
```
