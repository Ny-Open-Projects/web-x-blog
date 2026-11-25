---
title: [MFW-516] 全栈类型安全：tRPC 管线与构建器的协作点
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-516：全栈类型安全：tRPC 管线与构建器协作

**答**:
- tRPC 的类型推导链：server router（procedure 定义）→ `AppRouter` 类型 → client 代理（调用点类型全推导）——无 codegen（类型是 TS 推理不是生成）——构建器的协作点：1) **monorepo 类型共享**（server/client 同仓引用 AppRouter 类型——project references 的编译图 RBL-701）；2) typecheck 任务的 strict 配置（skipLibCheck 的取舍——推理链要求全量检查）；3) 产物边界（类型不进 bundle——import type 的擦除保证 RBL-946）。
- 与 RSC 的分工：RSC 内直接调 server 函数（同进程无网络——不需要 tRPC 的 RPC 层）；tRPC 适用「独立 API 服务 + 多端消费」（RN/第三方）——「同进程直调、跨进程 RPC」的选型分界。
- 类型推导的性能坑：超大 router 的 TS 推理慢（IDE 卡顿）——router 拆分 + `infer` 深度控制；「类型推导时长」也要预算（与构建时长同级的开发体验指标）。
- 追问钩子：为什么 tRPC「无 codegen」反而是约束而非优势？——类型推导依赖「编译时可见的 router 源码」——跨仓（前后端分仓）时推导断链（必须 codegen/或 monorepo）；codegen 与推导的选型本质是「代码物理位置」：同仓推导、跨仓生成——类型共享方案由仓库拓扑决定，不是框架偏好。

```javascript
// router 单源
export const appRouter = router({
  user: router({
    byId: publicProcedure.input(z.string()).query(({ input }) => db.user.find(input)),
  }),
});
export type AppRouter = typeof appRouter;
// client 推导
const client = createTRPCClient<AppRouter>({ links: [httpBatchLink({ url: '/api/trpc' })] });
const user = await client.user.byId.query('u1');        // user: User 类型自动推导
// 构建 typecheck 任务的协作点
// tsconfig.json: "references": [{ "path": "./packages/server" }, { "path": "./apps/web" }]
// "strict": true; "skipLibCheck": false —— 推理链要求
// 产物边界：import type { AppRouter } —— 擦除保证类型不进 bundle
```
