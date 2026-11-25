---
title: [FRP-393] 笔试：手写 islands 渲染器（静态 HTML + 交互岛水合）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, SSR]
type: 笔试题
---

## FRP-393：笔试：手写 islands 渲染器

**答**：实现 islands 客户端运行时：① HTML 中的 `<astro-island component="counter.react" props="{...}">` 占位符——运行时按需水合；② 水合策略三档：load（立即）、visible（IO 进入视口）、idle（空闲）——按 island 声明；③ 组件加载（registry.load）+ props 解析（JSON → 内核）+ mount（React/Vue 各自挂载）；④ 水合互斥（同 island 不重复）；⑤ 失败降级（island 加载失败保留静态 HTML + 错误标记）。写出实现。

```javascript
export function hydrateIslands(registry) {
  const islands = document.querySelectorAll('astro-island[data-hydrate]');
  islands.forEach((el) => {
    const strategy = el.dataset.hydrate;              // load | visible | idle
    const run = () => doHydrate(el, registry);
    if (strategy === 'load') run();
    else if (strategy === 'idle') requestIdleCallback?.(run, { timeout: 3000 }) ?? setTimeout(run, 2000);
    else if (strategy === 'visible') {
      const io = new IntersectionObserver((es) => {
        if (es[0].isIntersecting) { io.disconnect(); run(); }
      }, { rootMargin: '200px' });
      io.observe(el);
    }
  });
}
let hydrated = new Set();
async function doHydrate(el, registry) {
  if (hydrated.has(el)) return;                       // 互斥
  hydrated.add(el);
  try {
    const comp = await registry.load(el.dataset.component, el.dataset.framework);
    const props = JSON.parse(el.getAttribute('props') || '{}');
    const inner = document.createElement('div');
    el.appendChild(inner);
    // 各框架挂载(统一 unmount 句柄协议)
    const dispose = el.dataset.framework === 'react' ? mountReact(inner, comp, props) : mountVue(inner, comp, props);
    el._dispose = dispose;
  } catch (e) {
    el.dataset.error = '1';                           // 保留静态 HTML + 标记
    console.warn('[island] hydrate fail', el.dataset.component, e);
  }
}
```

**评分点**：
- 三档水合策略的触发时机（load/visible/idle + IO rootMargin）
- props 从 HTML attribute 反序列化
- 水合互斥 + 失败保留静态内容（渐进增强底线）
- 统一 unmount 句柄协议（与 FRP-371 契约一致）

## 变体与延伸（补充）

**变体与延伸**：

1. props 从 attribute 反序列化有什么安全风险？ → JSON 里若含 `</script>` 或未转义字符可导致 XSS；服务端必须做 HTML 转义，客户端 parse 后还要白名单校验，不能直接 innerHTML。
2. 两种水合策略同时命中同一 island 怎么办？ → hydrated 集合要分"声明中/已完成"两态，先占位再标记完成；否则 visible 与 idle 同时触发会二次 mount，事件被重复绑定。
3. island 水合失败后用户还能用吗？ → 不能交互，只剩静态 HTML；正确做法是保留原生可用的链接与表单行为（渐进增强），并把 dataset.error 上报给监控聚合。
