---
title: [WEB-462] 图片裂图的排查 SOP
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-462：图片裂图的排查 SOP

**答**：
- 按概率排序排查：① URL 是否失效/拼错（看 Network 面板状态码）② 防盗链（Referer 校验，403，策略刚收紧是高发）③ 格式兼容（老设备不支持 webp/avif）④ HTTPS 混合内容（http 图片被拦）⑤ 证书/域名问题
- 防盗链典型症状：开发机能看、线上 403，或嵌在第三方页里 403——对照 Referer-Policy 改动历史
- 兜底工程：`onerror` 里降级——换备用域名 → 换格式（webp→jpg）→ 占位图，并上报原始 URL 供统计
- 组件层：骨架/占位样式避免裂图标出现；列表滚动场景用 IntersectionObserver 加载而非直接 src
- 监控闭环：对 top 图片域名做拨测（定时 HEAD 请求），CDN 配置变更早于用户报障发现

```javascript
function imgFallback(img) {
  img.onerror = async () => {
    const step = img.dataset.step || '0';
    if (step === '0') { img.dataset.step = '1'; img.src = img.src.replace('cdn.a.com', 'cdn.b.com'); }
    else if (step === '1') { img.dataset.step = '2'; img.src = '/static/placeholder.png'; }
    report({ broken: img.dataset.origin, step });
  };
}
```
