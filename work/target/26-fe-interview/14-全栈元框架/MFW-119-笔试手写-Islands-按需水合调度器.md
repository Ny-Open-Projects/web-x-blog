---
title: [MFW-119] 笔试：手写一个 Islands 按需水合调度器
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-119：笔试：手写一个 Islands 按需水合调度器
**答**：Astro 输出的静态 HTML 里，每个岛有占位标记。实现调度器 `mountIslands()`：① 扫描 `[data-island]` 元素；② 按 `data-hydrate` 值调度：`load` 立即、`idle` 空闲后、`visible` 进入视口、`media` 匹配媒体查询；③ 水合 = 动态 import 该岛的模块并调用其 render；④ 同一岛只水合一次。

```ts
interface IslandHost {
  hydrate: 'load' | 'idle' | 'visible' | 'media';
  media?: string;
  componentPath: string; // 动态 import 目标
}

type Renderer = (el: HTMLElement) => void | Promise<void>;
const hydrated = new WeakSet<HTMLElement>();

function hydrateIsland(el: HTMLElement, island: IslandHost, render: Renderer): void {
  if (hydrated.has(el)) return; // 幂等：只水合一次
  hydrated.add(el);
  import(/* @vite-ignore */ island.componentPath)
    .then((mod) => render.call(mod, el))
    .catch((err) => console.error(`[island] 加载失败 ${island.componentPath}`, err));
}

function schedule(el: HTMLElement, island: IslandHost): void {
  const fakeRender: Renderer = (root) => {
    // 真实框架 renderer 在这里注入；示意：标记已激活
    root.setAttribute('data-hydrated', 'true');
  };

  switch (island.hydrate) {
    case 'load':
      hydrateIsland(el, island, fakeRender);
      break;
    case 'idle':
      (window as any).requestIdleCallback?.(() => hydrateIsland(el, island, fakeRender))
        ?? setTimeout(() => hydrateIsland(el, island, fakeRender), 200); // Safari 兜底
      break;
    case 'media':
      if (island.media && matchMedia(island.media).matches) hydrateIsland(el, island, fakeRender);
      else island.media && matchMedia(island.media).addEventListener?.('change', (e) => {
        if (e.matches) hydrateIsland(el, island, fakeRender);
      });
      break;
    case 'visible': {
      const io = new IntersectionObserver((entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            hydrateIsland(el, island, fakeRender);
            io.disconnect(); // 进入过视口就不再观察
          }
        }
      }, { rootMargin: '200px' }); // 提前 200px 预水合，减少滚动白屏
      io.observe(el);
      break;
    }
  }
}

export function mountIslands(): void {
  document.querySelectorAll<HTMLElement>('[data-island]').forEach((el) => {
    const island: IslandHost = {
      hydrate: (el.dataset.hydrate as IslandHost['hydrate']) ?? 'load',
      media: el.dataset.media,
      componentPath: el.dataset.component!,
    };
    schedule(el, island);
  });
}

// Astro 静态 HTML 里的标记形如：
// <div data-island data-hydrate="visible" data-component="/islands/CartButton.js"></div>
```

**评分点**：
1. 四种策略全覆盖且用对的 API（requestIdleCallback、IntersectionObserver、matchMedia）。
2. 幂等保护（WeakSet/断开 observer），避免重复水合。
3. visible 有 rootMargin 预加载意识（或等价提前量说明）。
4. idle 在不支持 requestIdleCallback 的浏览器有 setTimeout 兜底。
5. 动态 import 用运行时路径并处理加载失败（catch 不让单个岛拖垮页面）。
