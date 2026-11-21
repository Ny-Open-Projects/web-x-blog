---
title: [OPS-014] CDN 整体挂了怎么办？多 CDN 容灾和内联兜底页怎么做？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-014：CDN 整体挂了怎么办？多 CDN 容灾和内联兜底页怎么做？
**答**：
- 多 CDN 容灾：页面从主 CDN 加载 JS/CSS 失败时，自动切换到备用 CDN 域名重试；构建时把资源地址做成可替换的运行时清单。
- 极端兜底：index.html 内联一个极简"服务降级页"（或内联关键逻辑），外链资源全部失败时展示可用的静态内容+重试按钮，而不是白屏。
- 域名层面：CDN 域名配置多 CNAME 或由 DNS 服务做健康检查切换（DNSPod/GSLB），客户端脚本再兜一层。
- 切换动作要上报监控，区分"CDN 故障"和"应用故障"，方便事后向 CDN 厂商追责/复盘。

```javascript
// loader.js：多 CDN 容灾加载器 + 全挂时内联兜底
const CDN_HOSTS = [
  'https://cdn.example.com',      // 主 CDN
  'https://cdn-b.example.com',    // 备 CDN
  'https://cdn.example-cdn.net',  // 第三方兜底
];

function loadScript(src) {
  return new Promise((resolve, reject) => {
    const s = document.createElement('script');
    s.src = src; s.onload = resolve;
    s.onerror = () => { s.remove(); reject(new Error('load fail ' + src)); };
    document.head.appendChild(s);
  });
}

async function bootstrap(entryPath) {
  for (const host of CDN_HOSTS) {
    try {
      await loadScript(`${host}/${entryPath}`);
      reportMetric('cdn_bootstrap', { host, ok: 1 });
      return; // 命中即用，并把本次可用 CDN 记住供后续资源使用
    } catch (e) { /* 换下一个 */ }
  }
  // 所有 CDN 都挂：显示 index.html 里内联的降级内容
  document.getElementById('fallback-page').style.display = 'block';
  reportMetric('cdn_bootstrap', { ok: 0 }); // 打点也走 beacon 兜底
  setTimeout(() => location.reload(), 30000); // 30s 后自动重试
}

bootstrap('__ENTRY_JS__');
```
