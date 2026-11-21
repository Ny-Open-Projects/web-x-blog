---
title: [PER-626] 手写一个 SRI 生成与校验工具：构建期给产物生成 integrity，运行时校验失败触发上报与降级决策
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-626：手写一个 SRI 生成与校验工具：构建期给产物生成 integrity，运行时校验失败触发上报与降级决策

**答**：
- 构建侧：读产物文件内容算 SHA-384，按 `<algorithm>-<base64>` 格式生成 integrity 值，写入资源清单；同时生成 HTML 标签属性。
- 运行侧：监听 script error 事件，按资源清单判断是 SRI 失败还是 404（用响应头/状态区分），上报并按资源等级决定是否降级。
- 要点：hash 算法用 SHA-384（比 256 强且是 W3C 推荐上限性价比）；降级决策要有资源分级清单（core: 不降级；analytics: 可降级）；降级动作本身带一次性标记防循环。
- 评分点：构建-运行两侧闭环与降级分级。

```javascript

const crypto = require('crypto'), fs = require('fs');
// ---- 构建期 ----
function genIntegrity(file) {
  const buf = fs.readFileSync(file);
  const hash = crypto.createHash('sha384').update(buf).digest('base64');
  return `sha384-${hash}`;
}
function buildManifest(dir) {
  const manifest = {};
  for (const f of fs.readdirSync(dir)) {
    if (/\.(js|css)$/.test(f)) manifest[f] = { path: f, integrity: genIntegrity(`${dir}/${f}`) };
  }
  fs.writeFileSync('asset-manifest.json', JSON.stringify(manifest, null, 2));
  return manifest;
}
// ---- 运行期 ----
const TIER = { analytics: 'degradable', chat: 'degradable', app: 'core' };
addEventListener('error', (e) => {
  const el = e.target;
  if (el?.tagName !== 'SCRIPT') return;
  const name = el.src.split('/').at(-1).split('?')[0];
  const tier = TIER[name.split('.')[0]] ?? 'core';
  navigator.sendBeacon('/collect/sri-fail', JSON.stringify({ src: el.src, tier }));
  if (tier === 'degradable' && !el.dataset.retried) {
    el.dataset.retried = '1';
    const s = document.createElement('script');
    s.src = el.src.replace(window.__CDN, window.__CDN_BACKUP);  // 备用域降级
    s.integrity = '';                                            // 放弃校验，仅非核心
    document.head.appendChild(s);
  }
}, true);
```
