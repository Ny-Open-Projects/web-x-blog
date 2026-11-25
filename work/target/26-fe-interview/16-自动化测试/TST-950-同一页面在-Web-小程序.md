---
title: [TST-950] 同一页面在 Web / 小程序 / App 内嵌三端，视觉基线如何统一治理又允许差异化容差？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-950：同一页面在 Web / 小程序 / App 内嵌三端，视觉基线如何统一治理又允许差异化容差？
**答**：
- 结论：用「一份语义基线 + 多端渲染配置」——共享同一套选择器与断言意图，各端维护自己的基线图片与容差，避免互相覆盖。
- 差异来源：三端字体、DPR、浏览器内核不同，像素必不一致，强行共用基线只会制造大量误报。
- 做法：基线按 (页面, 端, 视口) 三元组索引；公共断言逻辑复用，容差按端配置；跨端比对只看结构/几何而非像素。
- 追问钩子：小程序端把按钮圆角从 8px 改成 12px，Web 端没变，三端统一治理怎么做到「各端各自告警、互不干扰」？

```javascript
const baselines = new Map(); // key: `${page}@${platform}@${viewport}`
function key(page, platform, viewport) { return `${page}@${platform}@${viewport}`; }
const TOLERANCE = { web: 0.02, miniprogram: 0.05, app-webview: 0.08 };
async function checkVisual({ page, platform, viewport, screenshot }) {
  const k = key(page, platform, viewport);
  const base = baselines.get(k);
  if (!base) { baselines.set(k, screenshot); return { status: 'baseline-created', k }; }
  const diff = pixelDiff(base, screenshot);
  return {
    k,
    status: diff <= TOLERANCE[platform] ? 'pass' : 'fail',
    diff: +diff.toFixed(3), tolerance: TOLERANCE[platform],
  };
}
function pixelDiff() { return 0.03; }
console.log(checkVisual({ page: 'detail', platform: 'miniprogram', viewport: '390x844', screenshot: 'buf' }));
// { k:'detail@miniprogram@390x844', status:'pass', diff:0.03, tolerance:0.05 }
```
