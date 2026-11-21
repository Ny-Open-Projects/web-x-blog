---
title: [PER-370] 性能开关（降级开关）的设计：服务端下发配置驱动前端性能降级，如何做到秒级生效？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-370：服务端下发的性能降级开关（关三方/降图片/关动画）如何做到秒级生效？

**答**：
- 配置通道三层（时效递增）：① 静态配置——HTML 里内联默认配置（兜底，离线可用）；② SW 缓存的配置接口——每次启动后台刷新（stale-while-revalidate，分钟级生效）；③ 实时通道——WebSocket/BroadcastChannel/轮询推送配置变更（秒级，用于紧急止血）。
- 开关设计：性能开关是"预置好的降级路径"——`{ disableThirdParty: false, imageQuality: 'high', disableAnimation: false }`，每个开关对应一段已写好的降级代码（不是临时改逻辑）；配置版本号 + hash 防止回滚错乱。
- 生效链路：SDK 收到配置 → 内存态立即生效（新请求走新配置）→ 持久化到 localStorage（下次启动保持）→ 广播到其他标签页（BroadcastChannel 同步）。
- 演练：降级开关必须季度演练（一键全量降级验证效果），否则紧急时刻才发现开关是坏的。

```javascript
// 配置驱动的降级
const defaults = { imageQuality: 'high', disableThirdParty: false };   // HTML 内联兜底
const conf = { ...defaults, ...JSON.parse(localStorage.getItem('perf-conf') || '{}') };

async function pollConf() {                            // SW/轮询刷新
  try {
    const r = await fetch('/api/perf-conf');
    const next = await r.json();
    if (next.rev !== conf.rev) { Object.assign(conf, next); localStorage.setItem('perf-conf', JSON.stringify(next));
      new BroadcastChannel('perf-conf').postMessage(next); applyConf(conf); }
  } catch { /* 离线用旧配置 */ }
}
new BroadcastChannel('perf-conf').onmessage = (e) => { Object.assign(conf, e.data); applyConf(conf); };
function applyConf(c) {                                 // 预置降级路径
  if (c.disableThirdParty) thirdPartyLoader.disableAll();       // 紧急止血：一键下线三方
  if (c.imageQuality === 'low') swapToPreviewImages();          // 弱网降级
  if (c.disableAnimation) document.documentElement.classList.add('no-anim');
}
// 秒级生效：实时通道改内存态 + 广播多标签页；开关必须演练过才算存在
```
