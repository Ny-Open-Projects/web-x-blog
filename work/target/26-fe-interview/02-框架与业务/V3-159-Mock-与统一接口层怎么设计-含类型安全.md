---
title: [V3-159] Mock 与统一接口层怎么设计（含类型安全）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-159：Mock 与统一接口层怎么设计（含类型安全）？
**答**：
- 分层：request 基座（axios/fetch 封装：拦截器、token、错误码归一）→ api 模块（按领域组织，泛型标注返回类型）→ 组件只调 api 函数。
- 类型安全：后端 OpenAPI 用 openapi-typescript 生成类型，api 层 `request<GetUserResp>(...)`，接口签名变化编译期暴露。
- Mock 两级：本地开发用 vite-plugin-mock（拦截网络层，前端独立开发）；联调期用环境变量切换真实网关。
- 统一约定：响应结构 `{ code, data, message }` 在拦截器里拆包，业务码集中映射错误提示，组件层只拿纯 data。

```typescript
// src/services/request.ts —— 基座 + 类型安全 + mock 切换
import axios from "axios";

const http = axios.create({
  baseURL: import.meta.env.VITE_API_BASE, // .env.development 可指向 mock 服务
  timeout: 10000,
});

http.interceptors.request.use((config) => {
  config.headers.Authorization = `Bearer ${localStorage.getItem("token")}`;
  return config;
});

// 响应拆包：业务码归一，组件只拿 data
http.interceptors.response.use(
  (resp) => {
    const { code, data, message } = resp.data;
    if (code !== 0) {
      const errorMap: Record<number, string> = {
        401: "登录已过期，请重新登录",
        403: "没有操作权限",
        500: "服务开小差了",
      };
      return Promise.reject(new Error(errorMap[code] ?? message));
    }
    return data; // 直接返回 data
  },
  (err) => Promise.reject(new Error(err.response?.data?.message ?? "网络异常"))
);

// 泛型 request：T 由调用方（或 OpenAPI 生成）指定
export function request<T>(config: Parameters<typeof http.request>[0]): Promise<T> {
  return http.request(config) as Promise<T>;
}

// src/services/user.ts —— 领域 api 模块
export interface User {
  id: number;
  name: string;
  role: "admin" | "user";
}
export type GetUserResp = User;

export const userApi = {
  getUser: (id: number) => request<GetUserResp>({ url: `/users/${id}` }),
  updateUser: (id: number, body: Partial<User>) =>
    request<User>({ url: `/users/${id}`, method: "put", data: body }),
};

// vite.config.ts 里的 mock 配置（伪代码）：
// plugins: [viteMockServe({ mockPath: "mock", localEnabled: true })]
// mock/user.ts: export default [{ url: "/api/users/:id", body: { code: 0, data: { id: 1, name: "wang", role: "admin" } } }]
```
