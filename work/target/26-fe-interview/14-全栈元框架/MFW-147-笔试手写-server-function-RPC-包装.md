---
title: [MFW-147] 笔试：手写一个 server function RPC 包装器
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-147：笔试：手写一个 server function RPC 包装器
**题目**：实现 `createServerFn(options)` 简化版：① 返回可调用函数，客户端调用时 POST 到 `/api/_rpc/{fnId}`；② 服务端根据 fnId 从注册表找到 handler 执行，入参先过 validator；③ 结果统一 `{ data }` 或 `{ error: { message, code } }` 结构；④ 仅服务端函数（isServer）直接本地调用不走网络；⑤ 未注册的 fnId 返回 404 结构化错误。

```ts
// shared/rpc.ts —— 客户端与服务端共用
type Handler<I, O> = (input: I) => Promise<O> | O;
type Validator<I> = (input: unknown) => I;

const registry = new Map<string, { handler: Handler<unknown, unknown>; validator: Validator<unknown> }>();

export function createServerFn<I, O>(opts: {
  fnId: string;
  method?: 'GET' | 'POST';
  validator?: Validator<I>;
  handler: Handler<I, O>;
  isServer?: boolean; // 编译期注入：该模块在服务端 bundle 中为 true
}) {
  const validator = opts.validator ?? ((x: unknown) => x as I);

  // 注册（服务端 bundle 才注册）
  if (opts.isServer) {
    registry.set(opts.fnId, { handler: opts.handler as Handler<unknown, unknown>, validator: validator as Validator<unknown> });
  }

  async function call(input: I): Promise<O> {
    if (opts.isServer) {
      // 服务端进程内直调：不绕网络
      return opts.handler(validator(input));
    }
    // 客户端：RPC
    const res = await fetch(`/api/_rpc/${opts.fnId}`, {
      method: opts.method ?? 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ input }),
    });
    const body = await res.json();
    if (!res.ok || body.error) {
      throw new RpcError(body.error?.message ?? 'RPC failed', body.error?.code ?? res.status);
    }
    return body.data as O;
  }

  return Object.assign(call, { fnId: opts.fnId });
}

export class RpcError extends Error {
  constructor(message: string, public code: string | number) { super(message); }
}

// 服务端入口：/api/_rpc/[fnId]
export async function rpcEndpoint(fnId: string, body: unknown) {
  const fn = registry.get(fnId);
  if (!fn) {
    return { status: 404, body: { error: { message: `unknown fn ${fnId}`, code: 404 } } };
  }
  try {
    const data = await fn.handler(fn.validator(body)); // validator 先行
    return { status: 200, body: { data } };
  } catch (e) {
    return {
      status: 500,
      body: { error: { message: e instanceof Error ? e.message : 'internal', code: 'RPC_HANDLER' } },
    };
  }
}
```

**评分点**：
1. 注册表 + fnId 路由的设计（框架生成端点的本质），未注册返回 404 结构化错误。
2. validator 在服务端端点处执行——入参校验不信任客户端。
3. isServer 分支：进程内直调 vs 网络 RPC，能说清编译期双 bundle 抽取原理。
4. 错误统一封装为 RpcError（不把服务端堆栈带给客户端）。
5. GET/POST 语义区分（GET 可缓存、POST 必须）。
