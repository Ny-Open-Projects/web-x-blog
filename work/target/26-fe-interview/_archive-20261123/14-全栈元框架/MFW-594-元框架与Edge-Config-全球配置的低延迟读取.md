---
title: [MFW-594] Edge Config：全球配置的低延迟读取
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-594：Edge Config 全球配置读取

**答**:
- Edge Config 的定位：全球复制的只读 KV（读 <1ms——数据在边缘节点驻留）vs 中心 Redis（RTT 100ms+）——「读极多写极少」的全局配置（feature flags/实验配置/路由表/灰度百分比 RBL-888）。
- 读路径：middleware/edge 函数直接读（同步级别的延迟——每个请求都读也不会慢）；「每请求读 EC」的可行性 = 延迟 <1ms（中心 DB 每请求读 = 100ms+ 不可行）。
- 写路径：管理后台 → 写 API → 全球传播（秒级最终一致——写入后各边缘节点陆续生效）；「配置变更的传播延迟」是设计输入（灰度百分比改了 10s 生效——可接受；密钥轮换要求即时——不适合 EC）。
- 与 Data Cache 的分工：EC = 「控制面数据」（决定渲染路径的配置）；Data Cache = 「业务数据」（渲染内容）——控制面与数据面分离（RBL-926 缓存分层的配置维度）。
- 追问钩子：为什么 feature flags 适合 Edge Config 而不适合 Data Cache？——flags 的读取频率 = 每请求（每个请求都要判定开关）；Data Cache 读 = 每请求 fetch 成本（KV 查询）；EC 读是内存级（isolate 驻留副本——零网络）——「读取频率 × 延迟敏感度」决定存储选型：每请求 × <1ms 要求 = EC；偶尔读 = Data Cache/DB——控制面数据的「读模式」与业务数据完全不同。

```typescript
// middleware 里读 EC（每请求 <1ms）
import { get } from '@vercel/edge-config';
export async function middleware(req) {
  const grayPct = await get('checkoutGrayPct') ?? 0;     // 全球边缘驻留
  const bucket = hash(userId(req)) % 100;
  if (bucket < grayPct) return NextResponse.rewrite(new URL('/checkout-b', req.url));
}
// EC 写路径（管理后台 → API → 全球传播）
await updateEdgeConfig({ checkoutGrayPct: 10 });         // 秒级传播到全球节点
// 控制面 vs 数据面
// EC: { flags, experiments, routingTable, rateLimits }   ← 控制面：决定「怎么渲染」
// Data Cache: { products, users, orders }                ← 数据面：渲染「什么内容」
// fallback 链：EC 不可用 → 环境变量默认（fail-open RBL-679）
const flags = await get('flags').catch(() => DEFAULT_FLAGS);
```
