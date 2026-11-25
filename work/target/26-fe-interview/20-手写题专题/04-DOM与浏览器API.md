---
title: 04 DOM 与浏览器 API · 手写题专题
date: 2026-11-24
categories: [前端手写]
tags: [前端面试, 笔试题, HW, DOM]
type: 笔试题
---

# 04 DOM 与浏览器 API

> 这一块的题有个共同点：**代码本身不长，坑全在浏览器语义里**。事件为什么没触发、图片为什么不加载、埋点为什么少报一半——面试官问的从来不是 API 拼写，而是你有没有真正在浏览器里调过。

## 能力分层

| 层级 | 题目 | 面试要求 |
|---|---|---|
| L1 必会 | 事件委托 / 原生 ajax / cookie 读写 / URL 参数解析 | 不看文档默写，知道五步流程 |
| L2 进阶 | 图片懒加载（含降级）/ rAF 缓动 / IntersectionObserver 曝光 | 会写降级路径，能说清阈值语义 |
| L3 深水 | 曝光批量上报（时长 + 去重 + sendBeacon）/ IndexedDB Promise 化 / Pointer Events 拖拽 | 能讲清生命周期与错误恢复 |

L1 的判定标准很实在：给你一个白板，能不能在 8 分钟里写出「能真的发出请求」的 `ajax`，而不是伪代码。

## 本专题原卡全景

| 编号 | 题目 | 层级 | 关键考点 |
|---|---|---|---|
| [HW-022](../06-算法与手写/HW-022-手写事件委托.md) | 手写事件委托 | L1 | 冒泡 + closest + contains 校验 |
| [HW-031](../06-算法与手写/HW-031-手写图片懒加载.md) | 手写图片懒加载 | L2 | IO + scroll 降级 + rootMargin |
| [HW-032](../06-算法与手写/HW-032-手写原生-ajax-XMLHttpRequest.md) | 手写原生 ajax | L1 | 五步流程、status 判断、onerror 边界 |
| [HW-033](../06-算法与手写/HW-033-手写-JSON-深比较.md) | 手写 JSON 深比较 | L1 | 同引用短路、key 数量剪枝、NaN |
| [HW-034](../06-算法与手写/HW-034-手写-URL-参数解析.md) | 手写 URL 参数解析 | L1 | 剔除 hash、第一个 = 分割、解码 |
| [HW-035](../06-算法与手写/HW-035-手写-cookie-读写.md) | 手写 cookie 读写 | L1 | 单条写、encode、max-age 删除 |
| [HW-036](../06-算法与手写/HW-036-手写-requestAnimationFrame.md) | 手写 rAF 动画（缓动） | L2 | 时间驱动进度、缓动函数、cancel |
| [HW-057](../06-算法与手写/HW-057-手写-IntersectionObserver.md) | 手写 IntersectionObserver 曝光统计 | L2 | threshold、单次去重、批量上报 |
| [HW-096](../06-算法与手写/HW-096-手写-IntersectionObserver-曝光埋点.md) | 手写曝光埋点 | L3 | 时长结算、WeakSet 去重、sendBeacon |
| [HW-107](../06-算法与手写/HW-107-手写-IndexedDB-轻量封装.md) | 手写 IndexedDB 轻量封装 | L3 | 事务 complete 语义、游标分页、版本迁移 |
| [HW-156](../06-算法与手写/HW-156-手写-基于-Pointer-Events-的通用拖拽.md) | 手写 Pointer Events 拖拽 | L3 | setPointerCapture、阈值、touch-action |
| [HW-175](../06-算法与手写/HW-175-手写-基于-URL-API-的深层解析.md) | 手写 URL 深层解析 | L2 | 相对路径、数组参数、hash 路由冲突 |

## 精讲（6 题）

### 精讲 1 · [HW-022] 事件委托

**为什么考这个**：它是「性能优化」里最容易被问、也最容易写错的一个。写对的关键不在 `addEventListener`，而在三个校验：`closest` 找到的是不是真命中、命中的元素还在不在容器内、`this` 指向谁。

**标准实现**：

```javascript
function delegate(root, selector, type, handler, { capture = false } = {}) {
  if (!root || typeof root.addEventListener !== 'function') {
    throw new TypeError('root must be an EventTarget');
  }
  const listener = (event) => {
    const origin = event.target;
    if (!origin || origin.nodeType !== 1) return;      // 文本节点没有 closest
    const matched = origin.closest(selector);          // 从触发点向上找，支持任意选择器
    if (!matched || !root.contains(matched)) return;   // 命中点必须仍在容器内
    handler.call(matched, event, matched);             // this → 命中的子元素
  };
  root.addEventListener(type, listener, capture);
  return () => root.removeEventListener(type, listener, capture); // 返回卸载函数
}

// 用法
const off = delegate(document.querySelector('#list'), 'li.item', 'click', function (e) {
  console.log(this.dataset.id);   // this 是被点的 li
});
```

**必须覆盖的边界**：

- `event.target` 可能是文本节点或注释节点，`nodeType !== 1` 要先挡掉，否则 `closest` 不存在直接报错。
- 必须做 `root.contains(matched)` 校验：元素被 `remove()` 后仍可能触发冒泡，或在 Shadow DOM / portal 场景下 `closest` 找到容器外的同名节点。
- 返回卸载函数，否则组件销毁后监听器泄漏（这是最常见的线上问题）。
- `handler` 用 `call(matched)` 而不是直接调用，否则 `this` 是 `undefined`（严格模式）而不是命中的元素。
- 不冒泡的事件（`focus`/`blur`/`mouseenter`）不能委托，要用 `focusin`/`focusout`/`mouseover` 替代。
- 捕获阶段委托（`capture: true`）时，事件还没到目标，语义与冒泡不同，要显式说明。

**追问链**：

1. 委托一定更快吗？→ 事件多、元素频繁增删时更快（一个监听器 vs N 个）；单个静态按钮反而多一次冒泡查找，没必要。
2. `closest` 和手写 `while (node !== root)` 的区别？→ `closest` 支持完整选择器语法且已优化；手写版要自己处理 `parentNode` 到 `document` 的边界。
3. React 17 之前的事件委托在哪？→ 委托在 `document`；17 之后改到根容器，好处是多实例 React 树不互相干扰、与原生 `stopPropagation` 的交互更可预测。
4. 怎么委托「点击空白关闭弹窗」？→ 在 `document` 上监听，判断 `!panel.contains(e.target) && !trigger.contains(e.target)`，注意触发按钮自身要排除，否则先关后开。

### 精讲 2 · [HW-031] 图片懒加载

**为什么考这个**：它是「渐进增强」的典型题。会写 `IntersectionObserver` 只是及格，能写出 `scroll` 降级、能解释 `rootMargin` 的单位与方向、能处理首屏，才是真的上线过。

**标准实现**：

```javascript
function lazyLoadImages({ selector = 'img[data-src]', rootMargin = '200px', onError } = {}) {
  const load = (img) => {
    const src = img.dataset.src;
    if (!src) return;
    delete img.dataset.src;                 // 先摘标记，防止重复触发
    img.addEventListener('error', () => onError?.(img), { once: true });
    img.src = src;                          // 真正开始下载
  };

  if (typeof IntersectionObserver === 'undefined') {
    // —— 降级：scroll + rAF 节流 + rect 判定 ——
    const imgs = [...document.querySelectorAll(selector)];
    let ticking = false;
    const check = () => {
      ticking = false;
      const vh = window.innerHeight || document.documentElement.clientHeight;
      for (let i = imgs.length - 1; i >= 0; i--) {
        if (imgs[i].getBoundingClientRect().top < vh + 200) {  // 提前 200px
          load(imgs[i]);
          imgs.splice(i, 1);                // 加载过就出队
        }
      }
    };
    const onScroll = () => {
      if (ticking) return;                  // 一帧只算一次
      ticking = true;
      requestAnimationFrame(check);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    check();                                // 首屏在视口内的必须立刻查
    return () => window.removeEventListener('scroll', onScroll);
  }

  const io = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      load(entry.target);
      io.unobserve(entry.target);           // 一次性：加载后不再观察
    }
  }, { rootMargin });

  document.querySelectorAll(selector).forEach(img => io.observe(img));
  return () => io.disconnect();
}
```

**必须覆盖的边界**：

- 首屏图片：IO 首次回调会触发，但降级版必须在绑定后立刻 `check()` 一次，否则首屏空白。
- `rootMargin: '200px'` 是「向外扩张 200px」，提前加载；负值则是「缩进」，用于「必须完全进入才加载」。
- 加载后必须 `unobserve` 或从队列移除，否则滚动时反复命中。
- `delete img.dataset.src` 比 `removeAttribute` 更快，且能防止重复加载。
- 图片加载失败要有 `error` 兜底（占位图 / 重试），否则用户看到破图。
- 懒加载 + `srcset`/`sizes` 时，要设置 `srcset` 而不是 `src`，否则响应式失效。
- 首屏 LCP 图**不要**懒加载——会直接拖慢 LCP 指标。

**追问链**：

1. IO 和 scroll 的本质差别？→ IO 由浏览器合成线程计算，不占主线程、不需要读布局；scroll 方案每帧 `getBoundingClientRect` 会强制同步布局（layout thrashing）。
2. 为什么用 `rAF` 节流而不是 `setTimeout`？→ rAF 与渲染帧对齐，页面不可见时自动暂停，不会在后台空转。
3. `rootMargin` 能写百分比吗？→ 能，但百分比是相对 root 的尺寸，容易误算，工程上优先用 px。
4. 图片进入视口但用户快速划过，要不要加载？→ 可以用「停留时长」或 `requestIdleCallback` 延迟加载，省流量。

### 精讲 3 · [HW-032] 原生 ajax（XMLHttpRequest）

**为什么考这个**：现在人人用 `fetch`/`axios`，但只要问到「`onerror` 会捕获 404 吗」「`open` 会发请求吗」，立刻能筛出谁真的写过 XHR。这两个点几乎每年都有人答错。

**标准实现**：

```javascript
function ajax({ url, method = 'GET', data = null, headers = {}, timeout = 10000, responseType = 'json' } = {}) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    const hasBody = !/^(GET|HEAD)$/i.test(method);
    let finalUrl = url;

    if (!hasBody && data) {                                  // GET 参数拼 query
      const qs = new URLSearchParams(data).toString();
      finalUrl += (url.includes('?') ? '&' : '?') + qs;
    }

    xhr.open(method.toUpperCase(), finalUrl, true);          // ① 只配置，不发请求
    xhr.timeout = timeout;
    xhr.responseType = responseType;                         // 'json' 自动解析
    for (const [k, v] of Object.entries(headers)) xhr.setRequestHeader(k, v); // ② open 之后、send 之前

    xhr.onload = () => {                                     // ③ readyState === 4 时触发
      if ((xhr.status >= 200 && xhr.status < 300) || xhr.status === 304) {
        resolve(xhr.response);
      } else {
        reject(Object.assign(new Error(`HTTP ${xhr.status}`), { status: xhr.status }));
      }
    };
    xhr.onerror = () => reject(new Error('Network Error'));  // 只捕获网络层错误
    xhr.ontimeout = () => reject(new Error(`Timeout after ${timeout}ms`));
    xhr.onabort = () => reject(new DOMException('Aborted', 'AbortError'));

    if (hasBody && data != null) {
      if (!headers['Content-Type']) xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.send(JSON.stringify(data));                        // ④ 真正发出
    } else {
      xhr.send(null);
    }
  });
}
```

**必须覆盖的边界**：

- `open()` 不发请求，只是配置；不调 `send()` 永远不会发。
- `setRequestHeader` 必须在 `open` 之后、`send` 之前，否则抛 `InvalidStateError`。
- `onerror` 只处理网络层失败（断网、DNS、CORS 预检失败），**4xx/5xx 会走 `onload`**，必须在 `onload` 里判断 `status`。
- 304 要算成功（走缓存），不要漏。
- 超时用 `xhr.timeout`，比外面套 `setTimeout` 更准（后者不能真正中止请求）。
- `responseType = 'json'` 时 `xhr.response` 已是对象，再 `JSON.parse` 会报错；空响应体（204）解析会失败，要兜底。

**追问链**：

1. `fetch` 为什么不会因 4xx 而 reject？→ 规范设计：`fetch` 只在网络层失败时 reject，HTTP 错误码属于「成功的响应」，必须自己 `if (!res.ok) throw`。
2. `fetch` 怎么加超时？→ `AbortController` + `AbortSignal.timeout(ms)`；注意 abort 后要区分「用户取消」与「超时」。
3. XHR 能传进度吗？→ `xhr.upload.onprogress`（上传）和 `xhr.onprogress`（下载），`fetch` 只能读 `response.body` 的流。
4. 为什么 `Content-Type: application/json` 会触发预检？→ 它不属于 CORS 简单请求的三种类型（`text/plain`、`multipart/form-data`、`application/x-www-form-urlencoded`），需要 `OPTIONS` 预检。

### 精讲 4 · [HW-036] requestAnimationFrame 动画（缓动）

**为什么考这个**：这题是「你懂不懂帧」的试金石。用帧数累加进度是最常见的错误——120Hz 屏上动画会快一倍，掉帧时会变慢。正确做法永远是「按时间戳算进度」。

**标准实现**：

```javascript
const easings = {
  linear: t => t,
  easeOutCubic: t => 1 - Math.pow(1 - t, 3),
  easeInOutQuad: t => (t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2),
};

function animate({ from = 0, to = 1, duration = 300, easing = easings.easeOutCubic, onUpdate, onDone } = {}) {
  if (duration <= 0) { onUpdate?.(to); onDone?.(); return () => {}; }

  let rafId = null;
  let startTime = null;
  let cancelled = false;

  const step = (now) => {
    if (cancelled) return;
    if (startTime === null) startTime = now;                  // 首帧定起点
    const p = Math.min((now - startTime) / duration, 1);      // 时间驱动，与帧率无关
    onUpdate?.(from + (to - from) * easing(p), p);
    if (p < 1) rafId = requestAnimationFrame(step);
    else onDone?.();
  };

  rafId = requestAnimationFrame(step);
  return () => {                                              // 返回 cancel
    cancelled = true;
    if (rafId !== null) cancelAnimationFrame(rafId);
  };
}

// animate({ from: 0, to: 300, duration: 400, onUpdate: v => (box.style.transform = `translateX(${v}px)`) });
```

**必须覆盖的边界**：

- 进度必须用时间戳算，不能用帧计数；`Math.min(..., 1)` 防止最后一帧超过 100%。
- `startTime` 要在**第一次回调**里取 `now`，不能在外面取 `performance.now()`，否则首帧会跳。
- 必须返回 cancel，并在 cancel 后阻止后续回调（`cancelled` 标志），否则动画停不下来。
- `duration <= 0` 要立即跳到终值并触发 `onDone`，否则永远不结束。
- 缓动函数的输入域是 `[0,1]`，输出也应在 `[0,1]`，否则会过冲（如 `easeOutBack`）。
- 页面切到后台时 rAF 自动暂停，回来时会「跳帧」——用时间戳算进度天然能对齐，不会补播。

**追问链**：

1. rAF 和 `setInterval(fn, 16)` 的差别？→ rAF 与屏幕刷新同步、后台自动暂停、不会连续堆积回调；`setInterval` 在掉帧时会排队，恢复后连续触发。
2. 为什么动画用 `transform` 不用 `left`？→ `transform` 走合成层，不触发布局与重绘；`left` 每帧触发 layout。
3. 怎么做到「暂停 / 继续」？→ 记录已播放的 `elapsed`，暂停时 cancel 并累加，恢复时把 `startTime` 设为 `now - elapsed`。
4. 多个元素同时动画怎么优化？→ 一个 rAF 循环驱动所有元素（集中调度），而不是每个元素各起一个 rAF。

### 精讲 5 · [HW-096] 曝光埋点：时长、去重与批量上报

**为什么考这个**：这是「业务理解 + 浏览器 API」的结合题。能写出「进入视口就上报」是初级；能说出「要停留 ≥ 1s 才算有效曝光」「页面隐藏时要结算」「用 `sendBeacon` 防止丢数据」才是真正做过数据的人。

**标准实现**：

```javascript
class ExposureTracker {
  constructor({ threshold = 0.5, minDuration = 0, report, batchSize = 10, flushInterval = 1000 } = {}) {
    Object.assign(this, { threshold, minDuration, report, batchSize, flushInterval });
    this.visibleSince = new Map();          // el -> 进入视口的时间
    this.reported = new WeakSet();          // 已上报：单次曝光去重
    this.queue = [];
    this.timer = null;
    this.io = new IntersectionObserver(this.handle.bind(this), { threshold: [0, threshold] });
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState !== 'hidden') return;
      for (const el of [...this.visibleSince.keys()]) this.settle(el); // 先把停留时长结掉
      this.flush(true);                                                // 再用 beacon 兜底
    });
  }
  handle(entries) {
    for (const { target, intersectionRatio } of entries) {
      if (intersectionRatio >= this.threshold) {                       // 可见面积达标
        if (!this.visibleSince.has(target)) this.visibleSince.set(target, performance.now());
      } else {
        this.settle(target);                                           // 离开视口
      }
    }
  }
  settle(el) {
    const start = this.visibleSince.get(el);
    if (start == null) return;
    this.visibleSince.delete(el);
    if (this.reported.has(el)) return;      // 已经报过，不重复
    const duration = performance.now() - start;
    if (duration < this.minDuration) return; // 停留太短：不算有效曝光
    this.reported.add(el);
    this.queue.push({ id: el.dataset.track, duration: Math.round(duration), ts: Date.now() });
    if (this.queue.length >= this.batchSize) this.flush();
    else this.schedule();
  }
  schedule() {
    if (this.timer) return;
    this.timer = setTimeout(() => this.flush(), this.flushInterval);
  }
  flush(useBeacon = false) {
    if (this.timer) { clearTimeout(this.timer); this.timer = null; }
    if (!this.queue.length) return;
    const batch = this.queue.splice(0);     // 先取出再发，失败可回填
    if (useBeacon && navigator.sendBeacon) {
      navigator.sendBeacon('/api/exposure', new Blob([JSON.stringify(batch)], { type: 'application/json' }));
    } else {
      this.report?.(batch);
    }
  }
  observe(selector) {
    document.querySelectorAll(selector).forEach(el => this.io.observe(el));
  }
}
```

**必须覆盖的边界**：

- `threshold` 是数组时，回调里必须自己判断 `intersectionRatio`，不能只依赖 `isIntersecting`（布尔值不区分比例）。
- 去重分两层：`visibleSince` 防止重复进入，`reported` 保证同一元素只上报一次。
- 页面隐藏时浏览器可能直接杀进程，`fetch` 会被中断，必须用 `navigator.sendBeacon`（或 `fetch` + `keepalive: true`）。
- `flush` 前先 `splice` 取出队列，请求失败时才能回填重试；直接清空会丢数据。
- `minDuration` 过滤「快速划过」的无效曝光，否则数据会被刷量污染。
- 元素从 DOM 移除时最好主动 `unobserve` 并 `settle`，否则 IO 可能在移除瞬间给出一次 `ratio=0`。

**追问链**：

1. `isIntersecting` 和 `intersectionRatio >= 0.5` 有什么区别？→ 前者只要有任何交集就是 `true`，后者要求可见面积过半；曝光业务通常用比例。
2. 为什么 `sendBeacon` 不会丢？→ 它把请求交给浏览器在页面卸载后继续发送，且不阻塞卸载；限制是只能 POST、体积 ≤ 64KB。
3. 首屏曝光和滚动曝光要分开统计吗？→ 要，首屏曝光（`load` 后立即可见）与「用户主动滚动看到」在业务含义上不同，通常用不同的 `trackId` 前缀。
4. 曝光数据量太大怎么办？→ 采样（按 `userId` 哈希取模）、批量合并、失败的降级到 `localStorage` 下次补发。

### 精讲 6 · [HW-175] URL 深层解析：相对路径、数组语义与 hash 冲突

**为什么考这个**：`URLSearchParams` 人人会用，但「相对路径怎么正确解析」「`?tag=a&tag=b` 和 `?tags=a,b` 怎么统一」「hash 路由下 `#` 还能不能当锚点」这三个问题，能立刻看出你有没有做过真实的路由/分享链接业务。

**标准实现**：

```javascript
function parseURL(input, base) {
  const fallbackBase = base ?? (typeof location !== 'undefined' ? location.href : undefined);
  const u = new URL(input, fallbackBase);        // 相对路径自动解析，非法值抛 TypeError

  const params = {};
  for (const key of new Set(u.searchParams.keys())) {
    const all = u.searchParams.getAll(key);
    if (all.length > 1) params[key] = all;                                    // ?tag=a&tag=b
    else params[key] = all[0].includes(',') ? all[0].split(',') : all[0];     // ?tags=a,b
  }

  const isHashRouter = u.hash.startsWith('#/');   // #/xxx 是路由，不是业务锚点
  return {
    href: u.href,
    origin: u.origin,
    path: u.pathname,
    query: u.search,
    params,
    hash: isHashRouter ? null : decodeURIComponent(u.hash.slice(1)),
    resolve: (rel) => new URL(rel, u).href,       // 相对路径 → 绝对
    withParams(patch) {
      const next = new URL(u.href);
      for (const [k, v] of Object.entries(patch)) {
        next.searchParams.delete(k);
        if (v === null || v === undefined) continue;              // 传 null 即删除
        for (const item of [].concat(v)) next.searchParams.append(k, item);
      }
      return next.href;
    },
  };
}

// parseURL('../detail?id=1', 'https://ex.com/list/page').resolve('./x') → 'https://ex.com/list/x'
```

**必须覆盖的边界**：

- 相对路径必须交给 `new URL(input, base)`，手写 `../` 的合并逻辑会踩 `//`、`.`、`..` 溢出根路径等一堆坑。
- `base` 在 Node/SSR 环境没有 `location`，必须显式传入，否则构造器抛错。
- 同键多次出现是数组语义，单值逗号也是数组语义，要统一成数组，否则下游 `params.tag.includes` 会炸。
- hash 路由（`#/user/1`）占用 `#`，业务锚点（`#section`）不可用，解析时必须区分并返回 `null`。
- 中文：整条 URL 用 `encodeURI`，参数值用 `encodeURIComponent`；`URLSearchParams` 会自动处理，不要重复编码（双重编码是高频 bug）。
- `withParams` 修改后要保证顺序稳定，便于做「分享链接去重」和缓存 key。

**追问链**：

1. `new URL('//cdn.com/a.js', 'https://ex.com')` 得到什么？→ `https://cdn.com/a.js`，协议相对 URL 会继承 base 的协议。
2. `searchParams.set` 和 `append` 的区别？→ `set` 覆盖同名键（只留一个），`append` 追加（变数组）；批量改写时必须先 `delete` 否则会残留旧值。
3. hash 路由和 history 路由怎么选？→ hash 不需要服务端配置、兼容老浏览器，但 URL 丑且 SEO 差；history 需要服务端 fallback 到 `index.html`，URL 干净、可做 SSR。
4. 分享链接里怎么带数组？→ 优先 `?tag=a&tag=b`（标准、可被 `getAll` 读取）；逗号分隔更短，但值本身含逗号时会歧义，必须约定转义。

## 其余 6 题速查

### [HW-033] JSON 深比较

```javascript
function deepEqual(a, b) {
  if (Object.is(a, b)) return true;                       // 同引用 / NaN === NaN
  if (typeof a !== 'object' || typeof b !== 'object' || a === null || b === null) return false;
  if (Array.isArray(a) !== Array.isArray(b)) return false;
  const ka = Object.keys(a), kb = Object.keys(b);
  if (ka.length !== kb.length) return false;              // 数量不同直接剪枝
  return ka.every(k => Object.hasOwn(b, k) && deepEqual(a[k], b[k]));
}
```

边界：只比较可枚举自有属性，`Symbol` 键与原型不参与（JSON 语义）；纯 JSON 数据无环，若可能成环要加 `WeakMap` 记录已比较的 `[a,b]` 对。复杂度 O(n)。追问「`JSON.stringify` 比较行不行」→ 键顺序敏感、环抛错、`undefined` 丢失，不可靠。

### [HW-034] URL 参数解析

```javascript
function parseQuery(url) {
  const qs = url.split('?')[1]?.split('#')[0] || '';   // 先剔除 hash
  const out = {};
  for (const pair of qs.split('&')) {
    if (!pair) continue;
    const idx = pair.indexOf('=');                     // 值里可能有 =（base64）
    const rawKey = idx === -1 ? pair : pair.slice(0, idx);
    const rawVal = idx === -1 ? '' : pair.slice(idx + 1);
    const key = decodeURIComponent(rawKey.replace(/\+/g, ' '));
    const val = decodeURIComponent(rawVal.replace(/\+/g, ' '));
    if (key in out) out[key] = [].concat(out[key], val); // 同名 key 合并数组
    else out[key] = val;
  }
  return out;
}
```

边界：`decodeURIComponent` 不处理 `+`（表单编码里 `+` 是空格），要手动 `replace`；没有 `=` 的参数（`?flag`）值为空串；重复 key 要么取最后一个、要么数组，必须明确约定。工程上优先 `new URL(url).searchParams`。

### [HW-035] cookie 读写

```javascript
const cookie = {
  set(name, value, { days, path = '/', domain, sameSite = 'Lax' } = {}) {
    let str = `${encodeURIComponent(name)}=${encodeURIComponent(value)}; path=${path}; SameSite=${sameSite}`;
    if (days != null) str += `; max-age=${Math.floor(days * 86400)}`;   // 秒，不是天
    if (domain) str += `; domain=${domain}`;
    if (location.protocol === 'https:') str += '; Secure';
    document.cookie = str;                            // 一次只能写一条
  },
  get(name) {
    const key = `${encodeURIComponent(name)}=`;
    const hit = document.cookie.split('; ').find(row => row.startsWith(key));
    return hit ? decodeURIComponent(hit.slice(key.length)) : null;
  },
  remove(name, opts = {}) {
    this.set(name, '', { ...opts, days: 0 });          // max-age=0 = 立即过期
  },
};
```

边界：`document.cookie` 是「全量字符串」，写入是追加不是覆盖，同名同 path/domain 才会覆盖；删除必须与写入的 `path`/`domain` 完全一致，否则删不掉；`HttpOnly` 的 cookie 前端读不到（安全设计）；`SameSite=None` 必须同时 `Secure`。

### [HW-057] IntersectionObserver 曝光统计（最小版）

```javascript
function trackExposure(selector, report, { threshold = 0.5, rootMargin = '0px' } = {}) {
  const io = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting || entry.intersectionRatio < threshold) continue;
      report(entry.target.dataset.trackId);
      io.unobserve(entry.target);                      // 单次曝光去重
    }
  }, { threshold: [threshold], rootMargin });
  document.querySelectorAll(selector).forEach(el => io.observe(el));
  return io;
}
```

边界：`threshold` 传数组时回调只会在跨越阈值时触发，判断比例要自己写；一个 observer 实例观察所有元素（不要每个元素 new 一个）；`rootMargin` 用于提前曝光。要统计「停留时长」就看 [HW-096]。

### [HW-107] IndexedDB 轻量封装

```javascript
const req2p = req => new Promise((resolve, reject) => {
  req.onsuccess = () => resolve(req.result);
  req.onerror = () => reject(req.error);
});

class DB {
  constructor(name, version, upgrade) {
    this.ready = new Promise((resolve, reject) => {
      const req = indexedDB.open(name, version);
      req.onupgradeneeded = (e) => upgrade(req.result, e.oldVersion, e.newVersion);
      req.onsuccess = () => resolve(req.result);
      req.onerror = () => reject(req.error);
      req.onblocked = () => reject(new Error('upgrade blocked by other tabs'));
    });
  }
  async store(name, mode = 'readonly') {
    const db = await this.ready;
    return db.transaction(name, mode).objectStore(name);
  }
  async get(name, key) { return req2p((await this.store(name)).get(key)); }
  async put(name, value) {
    const os = await this.store(name, 'readwrite');
    await req2p(os.put(value));
    return value;                                     // put 成功需等事务 commit 才真正落盘
  }
  async page(name, { limit = 20, after = null, index = null } = {}) {
    const os = await this.store(name);
    const src = index ? os.index(index) : os;
    const range = after == null ? null : IDBKeyRange.lowerBound(after, true); // keyset 分页
    return new Promise((resolve, reject) => {
      const out = [];
      const req = src.openCursor(range);
      req.onsuccess = () => {
        const cursor = req.result;
        if (!cursor || out.length >= limit) return resolve(out);
        out.push(cursor.value);
        cursor.continue();
      };
      req.onerror = () => reject(req.error);
    });
  }
}
```

边界：`put` 的 promise 要在**事务 `oncomplete`** 时 resolve 才算真正写入（只等 request success 可能在回滚后误判成功）；`onupgradeneeded` 里不能 `await` 其它事务；游标分页用「上一页最后一个 key」做 `lowerBound(..., true)`，比 `offset` 快且不会因插入错位；多标签页同时升级会 `onblocked`，要提示用户关闭其它页。

### [HW-156] Pointer Events 通用拖拽

```javascript
function draggable(el, { onStart, onMove, onEnd, threshold = 5 } = {}) {
  el.style.touchAction = 'none';            // 手势归应用，避免拖拽时页面滚动
  let pid = null, start = null, last = null, dragging = false;

  const onDown = (e) => {
    if (pid !== null) return;               // 忽略多指的第二根
    pid = e.pointerId;
    start = last = { x: e.clientX, y: e.clientY };
    el.setPointerCapture(pid);              // 移出元素甚至移出窗口仍能收到 move
  };
  const onPointerMove = (e) => {
    if (e.pointerId !== pid || !start) return;
    const dx = e.clientX - start.x, dy = e.clientY - start.y;
    if (!dragging) {
      if (Math.hypot(dx, dy) < threshold) return;   // 阈值内仍算点击
      dragging = true;
      onStart?.({ x: start.x, y: start.y, event: e });
    }
    last = { x: e.clientX, y: e.clientY };
    onMove?.({ dx, dy, x: last.x, y: last.y, event: e });
  };
  const onUp = (e) => {
    if (e.pointerId !== pid) return;
    if (dragging) onEnd?.({ x: last.x, y: last.y, event: e });
    el.releasePointerCapture?.(pid);
    pid = null; start = null; dragging = false;
  };

  el.addEventListener('pointerdown', onDown);
  el.addEventListener('pointermove', onPointerMove);
  el.addEventListener('pointerup', onUp);
  el.addEventListener('pointercancel', onUp);   // 系统手势打断也要收尾

  return () => {
    el.removeEventListener('pointerdown', onDown);
    el.removeEventListener('pointermove', onPointerMove);
    el.removeEventListener('pointerup', onUp);
    el.removeEventListener('pointercancel', onUp);
  };
}
```

边界：`setPointerCapture` 是「拖出元素」仍然能跟踪的关键，否则鼠标一离开元素就丢事件；阈值区分「点击」与「拖拽」，触摸设备上尤其重要；`touch-action: none` 不加会导致移动端拖拽时页面跟着滚；`pointercancel` 必须处理，否则拖拽状态卡死。

## 浏览器 API 选型表

| 需求 | 首选 | 为什么 | 别用 |
|---|---|---|---|
| 元素是否可见 | `IntersectionObserver` | 合成线程计算，不阻塞主线程 | scroll + `getBoundingClientRect` 循环 |
| 元素尺寸变化 | `ResizeObserver` | 精确到元素，不受窗口 resize 限制 | `window.onresize` |
| DOM 结构变化 | `MutationObserver` | 微任务批量回调 | `Mutation Events`（已废弃） |
| 动画 | `requestAnimationFrame` | 与刷新率同步，后台暂停 | `setInterval(16)` |
| 网络请求 | `fetch` + `AbortController` | Promise、可取消、可读流 | XHR（除非要上传进度） |
| 卸载前上报 | `navigator.sendBeacon` | 浏览器保证送达、不阻塞卸载 | `fetch`（会被中断） |
| 本地大容量存储 | IndexedDB | 异步、容量大、支持索引 | `localStorage`（同步阻塞、5MB） |
| 统一鼠标/触摸 | Pointer Events | 一套事件覆盖三种输入 | 分别写 mouse + touch |
| 跨标签页通信 | `BroadcastChannel` | 同源广播、结构化数据 | `localStorage` 事件（性能差） |

## 常见扣分点

| 扣分点 | 后果 | 正确做法 |
|---|---|---|
| 委托用 `e.target` 直接当命中元素 | 点到子 span 就失效 | `closest(selector)` 后再校验 |
| 委托不校验 `contains` | 已移除节点/portal 误触发 | `root.contains(matched)` |
| 委托不返回卸载函数 | 组件切换后监听器泄漏 | 返回 `removeEventListener` 闭包 |
| 懒加载不查首屏 | 首屏图空白 | 绑定后立即 `check()` |
| 懒加载不 `unobserve` | 每次滚动重复加载 | 加载后 `unobserve` + 删 `data-src` |
| `onerror` 判断 HTTP 错误 | 404 永远不 reject | 在 `onload` 里判断 `status` |
| `setRequestHeader` 放在 `open` 前 | `InvalidStateError` | open → header → send |
| rAF 用帧数累加进度 | 高刷屏动画变快 | 用 `(now - start) / duration` |
| cancel 后不设标志 | 动画停不下来 | `cancelled` 标志 + `cancelAnimationFrame` |
| 曝光用 `isIntersecting` 判 50% | 露出 1px 就上报 | 判断 `intersectionRatio >= threshold` |
| 页面隐藏用 `fetch` 上报 | 请求被中断、数据丢失 | `sendBeacon` 或 `keepalive: true` |
| `flush` 直接清空队列 | 请求失败即丢数据 | 先 `splice` 取出，失败回填 |
| cookie 删除不带 path | 删不掉 | 与写入时 path/domain 完全一致 |
| `parseQuery` 用 `split('=')[1]` | base64 值被截断 | `indexOf('=')` 取第一段 |
| IndexedDB 只等 request success | 事务回滚仍报成功 | 等事务 `oncomplete` |
| 拖拽不设 `touch-action` | 移动端页面跟着滚 | `touch-action: none` |
| 拖拽不处理 `pointercancel` | 状态卡在 dragging | `pointercancel` 复用 `onUp` |

## 白板节奏（8 分钟）

1. **先确认环境**（30 秒）：浏览器还是 Node？要不要降级？容器是谁？——DOM 题最怕写着写着发现「这函数在 SSR 里跑不了」。
2. **写主干**（3 分钟）：绑定 → 判定 → 执行 → 清理。四段式结构先立起来。
3. **补边界**（3 分钟）：首屏、去重、错误、卸载、页面隐藏。
4. **说清取舍**（1.5 分钟）：为什么用 IO 不用 scroll、为什么用 `sendBeacon`、为什么用 `pointer` 不用 `mouse`。

## 自测清单

- [ ] 能不看文档写出「点父容器、拿到子元素 `this`」的委托，并说出 `contains` 为什么必要。
- [ ] 能解释 `onerror` 为什么捕获不到 404，以及 304 为什么要算成功。
- [ ] 能写出 rAF 缓动动画，并解释为什么不能用帧数算进度。
- [ ] 能说清 `threshold`、`intersectionRatio`、`isIntersecting` 三者的区别。
- [ ] 能说出 `sendBeacon` 的两个限制（只能 POST、64KB）。
- [ ] 能解释 `?tag=a&tag=b` 与 `?tags=a,b` 的取舍，以及双重编码的坑。
- [ ] 能说出 IndexedDB 为什么必须等事务 `oncomplete` 才算写入成功。
- [ ] 能解释 `setPointerCapture` 解决的是哪个具体问题（拖出元素丢事件）。

