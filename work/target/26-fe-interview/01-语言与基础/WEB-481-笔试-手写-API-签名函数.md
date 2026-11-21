---
title: [WEB-481] 笔试：手写 API 签名函数
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 笔试题, 安全]
type: 笔试题
---

## WEB-481：笔试：手写 API 签名函数

**题目**：实现 `signRequest(params, secret)`：参数按 key 字典序排序，拼接成 `k1=v1&k2=v2`，追加 `timestamp` 与 `nonce`，对整体做 HMAC-SHA256，返回带签名的完整参数对象。要求：数组与嵌套对象先 JSON.stringify、空值参与签名、签名在 timestamp 生成之后计算。

**答**：
```javascript
async function signRequest(params, secret) {
  const timestamp = Date.now();
  const nonce = crypto.randomUUID();
  const norm = { ...params, timestamp, nonce };
  for (const k in norm) {
    if (norm[k] === undefined) delete norm[k];
    else if (typeof norm[k] === 'object') norm[k] = JSON.stringify(norm[k]);
  }
  const base = Object.keys(norm).sort()
    .map(k => `${k}=${encodeURIComponent(String(norm[k]))}`)
    .join('&');
  const key = await crypto.subtle.importKey('raw', new TextEncoder().encode(secret),
    { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const mac = await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(base));
  const sign = btoa(String.fromCharCode(...new Uint8Array(mac)));
  return { ...params, timestamp, nonce, sign };
}

// 用法
signRequest({ b: 2, a: { x: 1 }, empty: '' }, 's3cret').then(console.log);
```

**评分点**：
- 排序前先做值规范化（对象 JSON 化、undefined 剔除），顺序错了服务端必验不过
- timestamp/nonce 必须参与签名，否则可被拆改
- encodeURIComponent 只编码值；HMAC 用 WebCrypto 异步实现
- 知道纯前端签名的局限（secret 暴露），能主动提服务端代签
