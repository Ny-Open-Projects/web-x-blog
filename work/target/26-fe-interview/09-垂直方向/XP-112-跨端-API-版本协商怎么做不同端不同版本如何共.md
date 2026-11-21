---
title: [XP-112] 跨端 API 版本协商怎么做？不同端不同版本如何共存？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-112：跨端 API 版本协商怎么做？不同端不同版本如何共存？
**答**：
- 问题本质：发版节奏不同（Web 实时、App 商店延迟、小程序审核）导致**多版本客户端长期并存**，服务端必须同时服务 N-3 个客户端版本。
- 协商机制：客户端上报 `clientVersion + platform + capabilitySet`（能力集而非版本号——按能力路由比按版本路由更稳），接口响应带 `minClientVersion` 与迁移提示；handshake 接口启动时一次拉取。
- 兼容策略：服务端按能力集裁剪响应字段（缺的能力不下发新字段，客户端也不解析）；schema 演进遵守"只加不删、加字段必可选"的宽容读取原则（tolerant reader）。
- 强制升级与软降级：破坏性变更前先双写过渡期；`minClientVersion` 触发强更弹窗（强更文案与节奏走 XP-137 发布体系），未到强更线的旧版本走功能开关降级。
- 测试保障：契约测试（Pact 类）覆盖所有在支持版本 × 平台组合；"最旧客户端回归"进发版 checklist——支持矩阵本身就是 XP-137 的发布门禁输入。

```typescript
// packages/core/handshake —— 启动协商：能力集驱动，而非裸版本号
export interface ClientHello {
  platform: Platform;
  clientVersion: string;              // semver
  capabilities: string[];             // 能力集：'v2.checkout' 'ai.assistant' 'offline.pkg'
}
export interface ServerHello {
  serverTime: string;                 // UTC 锚点（XP-108）
  supported: boolean;                 // false → 触发强更
  minClientVersion?: string;          // 强更线
  featureGates: Record<string, boolean | number>;   // 旧版降级开关（XP-067 下发）
  deprecatedIn?: string;              // 提示：下个版本将移除某能力，提示升级
}

export async function handshake(http: HttpClient, me: ClientHello): Promise<ServerHello> {
  const res = await http.post('/gateway/handshake', me);
  if (!res.supported && res.minClientVersion) forceUpdateFlow(res.minClientVersion);
  return res;                          // featureGates 写入运行时，接口层按能力裁剪消费
}
// 服务端兼容矩阵（示例）：
//   8.0  capabilities 不含 v2.checkout → /checkout 返回 v1 结构
//   8.2  含 v2.checkout               → 返回 v2 结构（宽容读取：多字段无害）
//   <7.9 supported=false             → 强更（发布门禁：强更覆盖率 <0.5% 才允许下线旧接口）
// 契约测试：Pact 覆盖 {在支持版本} × {ios,android,web} 组合，CI 阻断破坏性变更
```

---

## 十四、性能对比与调优（113-118）
