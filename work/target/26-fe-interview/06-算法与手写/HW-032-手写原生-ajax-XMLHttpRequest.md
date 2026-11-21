---
title: [HW-032] 手写原生 ajax（XMLHttpRequest）
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-032：手写原生 ajax（XMLHttpRequest）

**答**：
- 评分点：五步流程说清——`new XMLHttpRequest()` → `open(method, url)`（open 不发请求只是配置）→ `setRequestHeader`（必须在 open 之后、send 之前）→ `onreadystatechange` 监听 `readyState === 4` → `send(body)`；status 判断用 `>= 200 && < 300 || === 304`；onerror 只捕获网络层错误，HTTP 4xx/5xx 不会触发 onerror（高频坑）；GET/POST 序列化：对象转 query 或 JSON body；整体包成 Promise 返回。

```javascript
// ===== 5 分钟速写版 =====
function ajax({ url, method = 'GET', data = null }) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open(method, url, true); // true = 异步
    if (method.toUpperCase() === 'POST') {
      xhr.setRequestHeader('Content-Type', 'application/json');
    }
    xhr.onreadystatechange = () => {
      if (xhr.readyState === 4) { // 4 = DONE
        if ((xhr.status >= 200 && xhr.status < 300) || xhr.status === 304) {
          resolve(JSON.parse(xhr.responseText));
        } else {
          reject(new Error(`HTTP ${xhr.status}`));
        }
      }
    };
    xhr.onerror = () => reject(new Error('network error'));
    xhr.send(method === 'GET' ? null : JSON.stringify(data));
  });
}

// ===== 标准完整版（含边界处理）=====
function ajaxPro({ url, method = 'GET', data = null, headers = {}, timeout = 10000 }) {
  return new Promise((resolve, reject) => {
    if (!url) return reject(new TypeError('url is required'));
    const xhr = new XMLHttpRequest();
    xhr.open(method.toUpperCase(), url, true);
    Object.entries(headers).forEach(([k, v]) => xhr.setRequestHeader(k, v));
    xhr.timeout = timeout; // 原生超时支持
    xhr.onreadystatechange = () => {
      if (xhr.readyState !== 4) return;
      // 0 常见于请求被取消 / 跨域被拦截
      if (xhr.status === 0) return reject(new Error('request aborted or blocked by CORS'));
      if ((xhr.status >= 200 && xhr.status < 300) || xhr.status === 304) {
        try {
          resolve(xhr.responseText ? JSON.parse(xhr.responseText) : null); // 空 body 容错
        } catch {
          resolve(xhr.responseText); // 非 JSON 按文本返回
        }
      } else {
        reject(Object.assign(new Error(`HTTP ${xhr.status} ${xhr.statusText}`), { status: xhr.status }));
      }
    };
    xhr.onerror = () => reject(new Error('network error')); // 断网 / DNS 失败才触发
    xhr.ontimeout = () => reject(new Error(`timeout after ${timeout}ms`));
    if (method.toUpperCase() === 'GET' || data === null) {
      xhr.send();
    } else if (data instanceof FormData) {
      xhr.send(data); // FormData 不能手动设置 Content-Type（浏览器会带 boundary）
    } else {
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.send(JSON.stringify(data));
    }
  });
}
// 追问：readyState 五个值的含义 0 未初始化 / 1 已 open / 2 已收到响应头 / 3 解析中 / 4 完成。
```

---
