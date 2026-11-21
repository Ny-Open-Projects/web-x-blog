---
title: [HW-168] 手写 SPA 路由切换指标——navigationId 变化检测 + 软导航 LCP 近似 + 路由级看板数据
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：SPA 软导航指标（PER-253 工程化）：路由起点（pushState 包装）→ 软导航 LCP 近似（MutationObserver + 双 rAF 稳定判定，PER-136 模式）→ 路由级 INP 近似（切换后首次交互延迟）→ 按路由聚合上报（看板按 route 分组）。

```javascript
class SPAMetrics {
  #start = 0; #route = ''; #lcpObserved = false;
  constructor(report) {
    Object.assign(this, { report });
    for (const fn of ['pushState', 'replaceState']) {
      const orig = history[fn].bind(history);
      history[fn] = (...args) => { this.#onNav(args[2]); return orig(...args); };
    }
    addEventListener('popstate', () => this.#onNav(location.pathname));
  }
  #onNav(path) {
    this.#route = routeTemplate(path);                    // PER-234 模板化
    this.#start = performance.now();
    this.#lcpObserved = false;
    this.#watchContent();
  }
  #watchContent() {                                       // 软导航 LCP 近似：DOM 稳定 + 双 rAF
    let lastMut = this.#start, done = false;
    const mo = new MutationObserver(() => { lastMut = performance.now(); });
    mo.observe(document.body, { childList: true, subtree: true });
    (function check(self) {
      requestAnimationFrame(() => requestAnimationFrame(() => {
        if (performance.now() - lastMut > 300) {          // 300ms 无 DOM 变更：内容稳定
          mo.disconnect();
          if (!done) {
            done = true;
            self.report({ type: 'spa-lcp', route: self.#route,
                          value: Math.round(lastMut - self.#start) });
          }
        } else check(self);
      }));
    })(this);
  }
  firstInteractionDelay() {                               // 路由后首次交互延迟（可交互性近似）
    const start = this.#start;
    return new Promise((resolve) => {
      const t0 = performance.now();
      const handler = () => {
        resolve(Math.round(performance.now() - start));   // 首次点击：距路由起点（含加载等待）
        removeEventListener('click', handler, true);
      };
      addEventListener('click', handler, true);
    });
  }
}
// 看板：route × spa-lcp p75 —— SPA 内导航的"每页 LCP"终于可见（PER-253 口径补充）
```

**评分点**：
- pushState/popstate 双入口包装 + routeTemplate 归一。
- 软导航 LCP 近似（MutationObserver + 双 rAF 稳定）——本题核心。
- 首次交互延迟作为可交互性近似（含加载等待的真实体感）。
- 按路由聚合看板（与硬导航 CWV 分开，口径声明）。
