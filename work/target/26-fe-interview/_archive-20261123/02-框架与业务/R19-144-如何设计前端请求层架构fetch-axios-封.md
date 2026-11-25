---
title: [R19-144] 如何设计前端请求层架构？fetch/axios 封装、拦截器与请求取消怎么落地？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-144：如何设计前端请求层架构？fetch/axios 封装、拦截器与请求取消怎么落地？
**答**：
- 分层：`http`（裸请求+拦截器）-> `api`（领域化函数，参数类型化）-> `hooks`（缓存/状态由 TanStack Query 接管），组件永远不直接 fetch。
- 拦截器只做横切关注点：注入 token、traceId、统一错误码翻译、401 刷新重放；**不做业务逻辑**。
- 取消三处都要接：路由切换取消未完成请求、搜索防抖取消上一次、组件卸载取消；axios 用 signal，封装层统一收口。
- 错误要有统一形状（code/message/data），业务代码只判断 data；错误上报在拦截器一次性埋好。

```typescript
// http.ts —— 请求层架构：封装 + 拦截器 + 取消
type ApiError = { code: number; message: string };

const BASE = '/api';
const pending = new Map<string, AbortController>(); // 在途请求登记表

function key(url: string, init?: RequestInit) {
  return `${init?.method ?? 'GET'} ${url}`;
}

async function request<T>(url: string, init: RequestInit = {}): Promise<T> {
  const k = key(url, init);
  // 去重：同 method+url 的在途 GET 直接复用，避免抖动重复请求
  if ((init.method ?? 'GET') === 'GET' && pending.has(k)) {
    return pending.get(k)!.signal.aborted
      ? Promise.reject(new Error('aborted'))
      : Promise.reject(new Error('duplicate'));
  }

  const controller = new AbortController();
  pending.set(k, controller);

  const res = await fetch(BASE + url, {
    ...init,
    signal: controller.signal,
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${localStorage.getItem('token') ?? ''}`, // 横切：注入凭证
      'X-Trace-Id': crypto.randomUUID(),                              // 横切：链路追踪
      ...init.headers,
    },
  }).finally(() => pending.delete(k));

  if (res.status === 401) {
    // 横切：统一处理会话过期（跳登录或刷新 token 重放）
    window.dispatchEvent(new Event('auth:expired'));
    throw { code: 401, message: 'unauthorized' } as ApiError;
  }
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw { code: res.status, message: body.message ?? 'request failed' } as ApiError;
  }
  const json = await res.json();
  return json.data as T; // 统一信封：业务只拿 data
}

export const http = {
  get: <T>(url: string) => request<T>(url),
  post: <T>(url: string, body: unknown) =>
    request<T>(url, { method: 'POST', body: JSON.stringify(body) }),
  cancelAll: () => pending.forEach(c => c.abort()), // 路由切换时统一取消
};

// api/user.ts —— 领域层：类型化 + 可单测
export const userApi = {
  list: (q: string) => http.get<{ id: number; name: string }[]>(`/users?q=${q}`),
  create: (name: string) => http.post<{ id: number }>('/users', { name }),
};
```
