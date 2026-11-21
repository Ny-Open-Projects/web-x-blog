---
title: [PER-216] 首页挂了七八个三方 SDK（统计/客服/广告/AB），互相抢主线程拖垮 INP，怎么治理？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-216：首页挂了七八个三方 SDK（统计/客服/广告/AB），互相抢主线程拖垮 INP，怎么治理？

**答**：
- 先量化：用 LoAF/RUM 按 invoker 归因，拿到"三方脚本阻塞时长排行榜"，用数据推动业务方下线/替换，而不是拍脑袋。
- 加载治理：非关键 SDK 延迟到空闲或首次交互后再加载（idle 加载 + 预热）；统一由自研加载器接管，禁止各方自行 `document.write` / 阻塞 script；能合网关的合网关（一次 TLS、一次解析）。
- 运行时治理：facade 模式替换重 SDK（地图/视频先渲染静态封面，点击才加载真 SDK）；Worker 化——把 SDK 的计算挪进 Web Worker（Partytown 思路隔离到 worker 线程）；设置权限与超时兜底（加载失败不影响主流程）。
- 制度治理：新三方接入走性能评审（体积、是否同步加载、是否写主线程）；CI 里加三方脚本体积与请求数卡口；定期审计下线僵尸 SDK。

```javascript
// 统一三方加载器：空闲时预连接 + 首次交互/空闲后真正加载 + 失败熔断
function loadThirdParty({ src, trigger = 'idle', timeout = 8000 }) {
  const link = document.createElement('link');
  link.rel = 'preconnect'; link.href = new URL(src).origin; document.head.append(link);
  return new Promise((resolve, reject) => {
    const load = () => {
      const s = document.createElement('script');
      s.src = src; s.async = true;
      s.onload = resolve; s.onerror = () => reject(new Error(`SDK 失败: ${src}`));
      document.head.append(s);
    };
    const t = setTimeout(() => reject(new Error('加载超时，熔断')), timeout);
    const start = () => { clearTimeout(t); load(); };
    if (trigger === 'idle') (window.requestIdleCallback || setTimeout)(start, { timeout: 2000 });
    else addEventListener(trigger, start, { once: true });   // 如 'pointerdown' 预热
  });
}
```
