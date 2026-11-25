---
title: [SCN-197] 营销活动页要用 Serverless（云函数）做 SSR，冷启动导致尾延迟飙高，如何应对？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-197：营销活动页要用 Serverless（云函数）做 SSR，冷启动导致尾延迟飙高，如何应对？
**答**：
- 冷启动的现实：Node 函数冷启动几百 ms 到秒级，无法根治只能"藏"：预热（定时触发器保活）、最小化依赖（bundle 瘦身比 runtime 优化更有效）、容器复用（模块顶层做连接池，handler 外的代码只在冷启动执行一次）。
- 用户体验兜底：SSR 超时（如 800ms）内没返回就先推静态骨架（HTML 流式输出 / CDN 兜底页），数据到了再 hydrate，用户永远先看到东西。
- 架构上分层：静态部分走 CDN（HTML 壳 + 资源），只有动态数据走函数，把函数的调用量与冷启动面都压到最小。
- 监控按"尾延迟"治理：P99 而不是平均值，冷启动占比单独打点，作为容量与预热的依据。

```javascript
// Serverless SSR：预热保活 + 流式输出 + CDN 兜底
// handler：冷启动开销移出 handler，模块顶层只执行一次（容器复用期共享）
import express from 'express';                         // 最小依赖：宁可手写路由也不引全家桶
const app = express();
app.get('/promo/:id', async (req, res) => renderPromo(req, res));

let dbPool;                                            // 连接池随容器复用
async function init() {
  dbPool ??= createPool({ min: 1, max: 4 });           // 顶层初始化，handler 内零建连
  await warmTemplateCache();                           // 模板预编译，避免首请求编译
}
const ready = init();                                  // 冷启动路径只走一次

export async function handler(req, res) {
  await ready;
  // 流式输出：骨架先走，数据到了再补，冷启动与查询延迟都被"藏"住
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.write(renderSkeletonHtml(req.params.id));        // 1. 骨架立即可见
  const data = await withTimeout(fetchPromoData(dbPool, req.params.id), 800);
  res.write(renderDynamicSection(data ?? null));       // 2. 动态区块（失败给客户端兜底标记）
  res.write('</body></html>');
  res.end();
}

function withTimeout(p, ms) {
  return Promise.race([p, new Promise((_, rej) => setTimeout(() => rej(new Error('SSR_TIMEOUT')), ms))]);
}
// SSR 超时时动态区块输出客户端兜底标记，前端接管为 CSR 拉取
function renderDynamicSection(data) {
  return data
    ? renderList(data)
    : `<div id="promo-root" data-csr-fallback="1"></div>`; // 客户端检测到标记则走 CSR 补拉
}

// 预热：定时触发器每 5 分钟打一次，保持容器存活（配合厂商并发预留更稳）
// serverless.yml 节选
//   functions:
//     ssr:
//       events:
//         - schedule: rate(5 minutes)   # 预热触发
//       provisionedConcurrency: 2       # 预留并发：热路径零冷启动
```
