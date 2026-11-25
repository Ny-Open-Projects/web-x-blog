---
title: [JS-166] 手写 fetch 封装完整版？超时、重试、拦截器、取消如何整合？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-166：手写 fetch 封装完整版？超时、重试、拦截器、取消如何整合？

**答**：
- 超时：AbortController + setTimeout 主动 abort；外部传入的 signal 也要桥接进来，两路取消合并成一个信号。
- 重试：只对网络错误与 5xx 重试，4xx 属于确定性失败；用指数退避避免打崩服务。
- 拦截器：请求拦截器逐层加工配置（注入 token/traceId），响应拦截器统一剥壳、错误归一。
- 超时 abort 会抛 TimeoutError 命名异常，要与用户取消区分开，方便上层提示。

```javascript
class HttpError extends Error {
  constructor(status, body) { super(`HTTP ${status}`); this.status = status; this.body = body; }
}

class HttpClient {
  constructor({ baseURL = '', timeout = 10000, retry = 0 } = {}) {
    this.baseURL = baseURL;
    this.timeout = timeout;
    this.retry = retry;
    this.reqPipe = [];               // 请求拦截器
    this.resPipe = [];               // 响应拦截器
  }
  useRequest(fn)  { this.reqPipe.push(fn); return this; }
  useResponse(fn) { this.resPipe.push(fn); return this; }

  async request(url, { method = 'GET', body, headers = {}, signal } = {}) {
    // 1. 请求拦截器：逐层加工配置
    let config = { url: this.baseURL + url, method, body, headers };
    for (const fn of this.reqPipe) config = await fn(config);

    // 2. 超时与外部取消合并为同一个 AbortController
    const ac = new AbortController();
    const timer = setTimeout(
      () => ac.abort(new DOMException('请求超时', 'TimeoutError')),
      this.timeout
    );
    if (signal) signal.addEventListener('abort', () => ac.abort(signal.reason), { once: true });

    // 3. 指数退避重试：仅网络错误与 5xx
    for (let attempt = 0; ; attempt++) {
      try {
        const res = await fetch(config.url, {
          method: config.method,
          body: config.body ? JSON.stringify(config.body) : undefined,
          headers: { 'Content-Type': 'application/json', ...config.headers },
          signal: ac.signal,
        });
        clearTimeout(timer);
        const data = res.headers.get('content-type')?.includes('json')
          ? await res.json() : await res.text();
        if (!res.ok) {
          if (res.status >= 500 && attempt < this.retry) {
            await new Promise((r) => setTimeout(r, 2 ** attempt * 300));
            continue;                             // 5xx 退避后重试
          }
          throw new HttpError(res.status, data);  // 4xx 直接失败
        }
        // 4. 响应拦截器：剥壳与错误归一
        let out = data;
        for (const fn of this.resPipe) out = await fn(out, res);
        return out;
      } catch (e) {
        clearTimeout(timer);
        if (e instanceof HttpError) throw e;
        if (attempt < this.retry) {
          await new Promise((r) => setTimeout(r, 2 ** attempt * 300));
          continue;                               // 网络错误重试
        }
        throw e;
      }
    }
  }
}

// 用法
const getToken = () => localStorage.getItem('token') || '';
const http = new HttpClient({ baseURL: 'https://api.example.com', timeout: 5000, retry: 2 })
  .useRequest(async (c) => ({
    ...c,
    headers: { ...c.headers, Authorization: `Bearer ${getToken()}`, 'X-Trace-Id': crypto.randomUUID() },
  }))
  .useResponse(async (data) => {
    if (data?.code !== 0) throw new Error(data?.msg || '业务错误');
    return data.data;                             // 统一剥壳
  });
// const user = await http.request('/user/1', { signal: 页面离开的 signal });
```
