---
title: [PER-1017] 手写一个 third-party 脚本加载熔断器
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1017：手写一个 third-party 脚本加载熔断器

**答**：
- 需求：实现 loadThirdParty(src, opts) 返回 Promise。opts: { timeoutMs=3000, maxFail=3 }；用 script 标签动态加载；超时或错误计入失败计数，连续失败 >= maxFail 后进入熔断（后续调用直接 reject circuit-open，静默期 60s 后半开重试一次）；成功则重置计数并缓存 loaded 标记避免重复加载。
- 边界：并发调用共享同一 Promise（去重）；熔断期间不发起请求；报告上报失败与熔断事件。
- 评分点：并发去重；超时处理；熔断半开；事件上报

```javascript
function loadThirdParty(src, { timeoutMs = 3000, maxFail = 3, cooldown = 60_000 } = {}) {
  let fails = 0, openUntil = 0, inflight = null, loaded = false;
  return function load() {
    if (loaded) return Promise.resolve();
    const now = Date.now();
    if (fails >= maxFail && now < openUntil)
      return Promise.reject(new Error('circuit-open'));
    if (inflight) return inflight;
    inflight = new Promise((resolve, reject) => {
      const s = document.createElement('script');
      s.src = src;
      const timer = setTimeout(() => {
        s.remove(); fail(new Error('timeout'));
      }, timeoutMs);
      function fail(e) {
        fails++; report({ type: '3p-fail', src, fails });
        if (fails >= maxFail) { openUntil = Date.now() + cooldown;
          report({ type: '3p-circuit-open', src }); }
        inflight = null; reject(e);
      }
      s.onload = () => { clearTimeout(timer); loaded = true; inflight = null; resolve(); };
      s.onerror = () => { clearTimeout(timer); fail(new Error('load-error')); };
      document.head.appendChild(s);
    });
    return inflight;
  };
}
```
