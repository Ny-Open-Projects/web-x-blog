---
title: [MFW-614] SSR 的时间与时区：TZ 感知渲染的陷阱
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-614：SSR 时间与时区渲染

**答**:
- SSR 的时区陷阱：1) server 时区 ≠ client 时区（SSR 渲染 UTC+8、用户 UTC-5——同 timestamp 显示不同日期「跨日界」）；2) 水合 mismatch（SSR 的「3 分钟前」与 client 计算不同——时间流逝 RBL-914 时间类）；3) 构建期固化时间（RBL-890 反模式——SSG 页面的 new Date() = 构建时间戳）。
- 正确姿势：1) **timestamp 为源、格式化在 client**（或 server 显式传 tz）；2) 相对时间：server 传 timestamp + client Intl.RelativeTimeFormat（水合后更新——或接受 SSR 与 client 的差异 suppress + 更新）；3) SSR 格式化用「用户的 tz」需要 session/geo 信息（IP→tz 的近似）——「用户 tz 的来源」：cookie 显式 > geo IP 近似 > UTC 兜底。
- 追问钩子：为什么「SSR 的时间显示」的 mismatch 比「其他 mismatch」更难彻底消除？——时间是持续流逝的（SSR 时刻的「3 分钟前」到水合时刻就是「4 分钟前」——即使用户与 server 同 tz 也 mismatch）；彻底解 = 「suppress + client 更新」或「绝对时间显示」（不显示相对时间）；「时间的流动性」决定策略：显示精度要求低（分钟级）→ suppress 可接受；精确 → server 只传 timestamp + client 渲染——时间渲染是「流式 + 流逝」的双重时序问题（RBL-520 流式的叠加）。

```tsx
// 反模式：SSR 直接 new Date() 相对时间
// <span>{relativeTime(item.createdAt)}</span>  ← SSR「3分钟前」vs client「4分钟前」→ mismatch
// 方案 A：suppress + client 更新（分钟精度场景）
export default function Time({ ts }: { ts: number }) {
  return <span suppressHydrationWarning>{format(ts)}</span>;   // SSR 可能略异，client 校正
}
// 方案 B：绝对时间（精确场景）
<span>{new Intl.DateTimeFormat(locale, { timeZone: tz, dateStyle: 'medium' }).format(ts)}</span>
// server 显式 tz：session/geo 注入
export async function getTZ() {
  const c = await cookies();
  return c.get('tz')?.value ?? geoToTZ(headers().get('x-vercel-ip-city')) ?? 'UTC';
}
// TZ 矩阵测试（CI）
// TZ=America/New_York pnpm test -- filter=date
// TZ=Asia/Tokyo pnpm test -- filter=date
```
