---
title: [MFW-165] SSR 服务过载时的降级策略有哪些？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-165：SSR 服务过载时的降级策略有哪些？
**答**：
- 降级阶梯（从轻到重）：① 缩短缓存 TTL/扩大缓存面（把更多页面推给 CDN）；② 关闭非关键取数（评论/推荐延后或客户端补齐）；③ **切静态壳**——预渲染的骨架 HTML + 客户端 CSR 补数据；④ 整页切 CSR（SPA 降级模式）；⑤ 最坏返回统一错误页但保持可重试。
- 触发信号：CPU/内存水位、渲染队列积压（p95 渲染时间超阈值）、下游依赖熔断。判定要「连续 N 个窗口」防抖，避免抖动降级。
- 实现要点：降级开关集中在中间件层统一决策（边缘/网关比应用层更可控）；降级页要有重试引导；恢复要渐进（先灰度放量 10% 检查指标再全量）。
- 压测验证：降级路径必须平时演练（混沌工程），否则故障时降级代码本身是没被测过的新代码。

```ts
// middleware.ts —— 过载检测与降级开关
import { NextRequest, NextResponse } from 'next/server';

const WINDOW = 10_000;
let renderTimes: number[] = [];

export function middleware(req: NextRequest) {
  const degraded = isOverloaded();

  if (degraded && !isPersonalized(req)) {
    // 降级：返回预渲染静态壳，客户端自行 CSR 拉数据
    const res = NextResponse.rewrite(new URL('/static-shell' + req.nextUrl.pathname, req.url));
    res.headers.set('x-degraded', '1');
    res.headers.set('Cache-Control', 'public, max-age=30'); // 短缓存吸收洪峰
    return res;
  }
  return NextResponse.next();
}

function isOverloaded(): boolean {
  const now = Date.now();
  renderTimes = renderTimes.filter((t) => now - t < WINDOW);
  const slow = renderTimes.length > 0
    && renderTimes.filter((t) => t > 800).length / renderTimes.length > 0.5; // 50% 渲染超 800ms
  return slow;
}

// 渲染计时埋点（业务代码里）
export function trackRender(ms: number): void { renderTimes.push(ms); }
```
