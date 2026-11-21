---
title: [R19-190] 如何设计一个埋点 SDK 的 React 插件（自动埋点）？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-190：如何设计一个埋点 SDK 的 React 插件（自动埋点）？
**答**：
- 双模式：**自动埋点**（data-track 属性声明式埋点：曝光/点击全局代理）、**手动埋点**（track(eventName, props) 命令式 API）；React 侧提供 `<Track>` 组件与 usePageView hook。
- 曝光实现：IntersectionObserver 全局单例，目标元素入视口超阈值即上报，带去重（同 id 只报一次）与停留时长。
- 点击实现：document 级事件代理捕获 click，沿 DOM 向上找 `[data-track]`，取属性组装事件——组件零侵入。
- 工程要点：sendBeacon 兜底页面卸载上报、批量队列 + 定时 flush、SPA 路由变化自动 pageview、采样率与灰度开关。

```tsx
// track-sdk.tsx —— 埋点 SDK React 插件
import { useEffect, useRef, type ReactNode } from 'react';

// 1. SDK 核心：队列 + 批量上报 + sendBeacon
const queue: any[] = [];
let flushTimer: number | undefined;

function flush() {
  if (!queue.length) return;
  const batch = queue.splice(0);          // 原子取出
  navigator.sendBeacon?.('/api/track', JSON.stringify(batch))
    ?? fetch('/api/track', { method: 'POST', body: JSON.stringify(batch), keepalive: true });
}

function track(event: string, props: Record<string, unknown> = {}) {
  queue.push({ event, props, ts: Date.now(), path: location.pathname });
  clearTimeout(flushTimer);
  flushTimer = window.setTimeout(flush, 3000);      // 批量 + 防抖
}
// 页面卸载兜底：剩余队列立即发出
window.addEventListener('pagehide', flush);

// 2. React 插件：全局安装自动埋点
export function installTrackProbe() {
  // 2a. 点击代理：事件委托，组件零侵入
  document.addEventListener('click', e => {
    const el = (e.target as HTMLElement).closest('[data-track]');
    if (!el) return;
    track(el.dataset.track!, {
      module: el.dataset.trackModule,
      text: el.textContent?.slice(0, 20),
    });
  }, { capture: true });

  // 2b. 曝光代理：全局单例 IO
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (en.isIntersecting) {
        const el = en.target as HTMLElement;
        track('expose', { module: el.dataset.trackModule, id: el.dataset.track });
        io.unobserve(el);               // 曝光只报一次
      }
    });
  }, { threshold: 0.5 });

  // MutationObserver 兜底 SPA 动态节点
  const mo = new MutationObserver(() => {
    document.querySelectorAll('[data-track-expose]:not([data-exposed])').forEach(el => {
      el.setAttribute('data-exposed', '1');
      io.observe(el);
    });
  });
  mo.observe(document.body, { childList: true, subtree: true });
}

// 3. 路由 pageview：React Router 侧一行接入
export function usePageView() {
  const firstRef = useRef(true);
  useEffect(() => {
    track(firstRef.current ? 'page_view_first' : 'page_view', {
      referrer: document.referrer,
    });
    firstRef.current = false;
  }, [location.pathname]);
}

// 4. 声明式组件：<Track action="buy_click"> 包装埋点
export function Track({ action, module, children }: {
  action: string; module: string; children: ReactNode;
}) {
  return (
    <div data-track={action} data-track-module={module} data-track-expose="1">
      {children}
    </div>
  );
}

// 5. 手动埋点导出
export const analytics = { track };
// 业务代码：analytics.track('order_submit', { amount: 99 })
```
