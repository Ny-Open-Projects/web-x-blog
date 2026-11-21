---
title: [WCN-484] 笔试：实现元素脚本加载的多 CDN 降级链（SRI + 超时切换）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-484：笔试：实现元素脚本加载的多 CDN 降级链（SRI + 超时切换）。
**题目**：`loadWithFallback(urls, {sri, timeout})`：依次尝试，单源超时/校验失败切下一个；全部失败 reject；成功返回 eval 结果（script 标签加载）。

```javascript
function loadScript(url, sri, timeout = 5000) {
  return new Promise((res, rej) => {
    const s = document.createElement('script');
    s.src = url; if (sri) s.integrity = sri; s.crossOrigin = 'anonymous';
    const t = setTimeout(() => rej(new Error('timeout')), timeout);
    s.onload = () => { clearTimeout(t); res(); };
    s.onerror = () => { clearTimeout(t); rej(new Error('load-fail')); };
    document.head.append(s);
  });
}
async function loadWithFallback(urls, sris) {
  const tried = [];
  for (let i = 0; i < urls.length; i++) {
    try { await loadScript(urls[i], sris?.[i]); return { url: urls[i], tried }; }
    catch (e) { tried.push({ url: urls[i], err: e.message }); }
  }
  throw new Error(`全部 CDN 失败：${JSON.stringify(tried)}`);
}

```

**评分点**：
- 超时控制（单源 5s）。
- SRI 校验失败也切换（完整性优先）。
- fallback 链记录（诊断上报）。
- 全失败 reject（页面静态内容仍可用——DSD 兜底说明）。
