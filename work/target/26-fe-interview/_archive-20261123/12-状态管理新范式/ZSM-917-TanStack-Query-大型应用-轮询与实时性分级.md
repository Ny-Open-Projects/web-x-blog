---
title: [917] TanStack Query 的轮询/实时策略怎么分级
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 实时]
type: 面试题
---

## 917：TanStack Query 的轮询/实时策略怎么分级

**答**：
- 实时性三级：推送（WebSocket/SSE 变更 -> invalidate 对应 Key——最准）、条件轮询（refetchInterval 函数式——数据 live 才轮询）、静态（不轮询靠失效）——按数据「变化频率 x 业务敏感度」分级。
- 轮询礼仪：页面不可见暂停（refetchIntervalInBackground false）、轮询抖动（多客户端同步轮询打爆服务端——加随机抖动 ±20%）、指数轮询（连续空转 N 次自动降频）。
- 推送与轮询混合：核心数据推送 + 兜底轮询（推送断了低频轮询兜底，推送到达时 invalidate 即时更新）。
- 追问钩子：推送到达 invalidate 会不会引起请求风暴？——会，服务端要做失效合并窗口（batch invalidate 广播加随机延迟 0~2s 摊平）。

```ts
useQuery({
  queryKey: ['market', symbol],
  queryFn: fetchQuote,
  refetchInterval: q => {
    const live = q.state.data?.live;
    if (!live) return false;
    return 3000 + Math.random() * 600;          // 轮询抖动 ±20%
  },
  refetchIntervalInBackground: false,           // 后台暂停
});
```

