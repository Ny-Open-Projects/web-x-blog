---
title: [OPS-013] 什么是 Feature Flag 止血？前端降级开关怎么设计？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-013：什么是 Feature Flag 止血？前端降级开关怎么设计？
**答**：
- Feature Flag 是"不改代码、不发版本就能关闭某个功能"的运行时开关，是把 30 分钟的回滚变成 30 秒的止血的关键手段。
- 设计要点：开关读取要有本地缓存兜底（配置中心挂了要用最后一份已知配置）；默认值必须偏保守（拿不到配置时关闭高风险功能）。
- 开关粒度到功能级而非页面级，并且每次高风险发布 MR 里声明"本改动涉及哪些开关"，预案里写清关哪个。
- 开关是技术债，要定期清理长期为 true 的死开关，避免分支组合爆炸。

```javascript
// feature-flags.js：带本地缓存兜底的运行时开关
const FLAG_CACHE_KEY = 'app.flags.v1';
const FLAG_TTL = 5 * 60 * 1000; // 缓存 5 分钟
// 保守默认值：配置中心不可用时，高风险功能一律关闭
const SAFE_DEFAULTS = { newCheckout: false, aiAssistant: false, liveChat: true };

async function loadFlags() {
  try {
    const res = await fetch('https://config.example.com/flags/web.json', {
      cache: 'no-store',
      timeout: 3000,
    });
    if (!res.ok) throw new Error(`flag http ${res.status}`);
    const flags = await res.json();
    localStorage.setItem(
      FLAG_CACHE_KEY,
      JSON.stringify({ flags, ts: Date.now() })
    );
    return { ...SAFE_DEFAULTS, ...flags };
  } catch (e) {
    // 兜底：配置中心挂了用最后一份缓存；缓存也没有用安全默认值
    const cached = localStorage.getItem(FLAG_CACHE_KEY);
    if (cached) {
      const { flags, ts } = JSON.parse(cached);
      if (Date.now() - ts < FLAG_TTL * 12) return { ...SAFE_DEFAULTS, ...flags };
    }
    reportError('flag_center_down', e);
    return SAFE_DEFAULTS;
  }
}

export const flags = await loadFlags();
// 使用：flags.newCheckout ? <NewCheckout /> : <OldCheckout />
```
