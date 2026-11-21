---
title: [NODE-066] 如何压测与估算 QPS 容量（autocannon/wrk）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-066：如何压测与估算 QPS 容量（autocannon/wrk）？
**答**：
- 工具：`autocannon`（Node 写的，易集成脚本）、`wrk`（C 写的高性能压测，Lua 脚本定制请求）。压测必须**在等价环境**（同配置机器/容器限额）进行，压测端与服务端分开部署。
- 看什么指标：QPS（吞吐）、P99 延迟（比平均值重要）、错误率（non-2xx）、压测时的事件循环延迟与内存曲线。**容量 = 目标峰值 QPS × 安全系数 / 单实例实测 QPS**，再除以单实例极限留 30~50% 余量。
- 方法论：先单接口压出基线 → 找瓶颈（CPU/下游/锁）→ 优化 → 复压 → 用小流量灰度验证真实流量模型。

```bash
# autocannon：100 并发持续 30s，输出 QPS 与延迟分布
npx autocannon -c 100 -d 30 -p 10 http://localhost:3000/api/products/42 \
  --headers "authorization: Bearer $TOKEN" \
  --json > result.json
# 输出关注：requests/avg（QPS）、latency p99、non2xx
```

```bash
# wrk：4 线程 200 连接 30s，Lua 脚本带 body
wrk -t4 -c200 -d30s -s post.lua --latency http://localhost:3000/api/orders
```

```lua
-- post.lua
wrk.method = "POST"
wrk.headers["content-type"] = "application/json"
wrk.body   = '{"sku":"A001","count":1}'
wrk.headers["authorization"] = "Bearer test-token"

response = function(status, headers, body)
  if status ~= 200 then
    io.write("bad status: " .. status .. "\n")  -- 错误采样
  end
end
```

```javascript
// 容量估算：由压测结果推导实例数
const measured = { qpsPerInstance: 1800, p99Ms: 45, errorRate: 0 };
const target = {
  peakQps: 30000,          // 大促预估峰值（由历史流量 × 增长系数推得）
  safetyFactor: 0.6,       // 只用 60% 极限容量，留突发余量
};
const needInstances = Math.ceil(
  target.peakQps / (measured.qpsPerInstance * target.safetyFactor),
); // ≈ 28 个实例，再按可用区打散部署
console.log(`建议实例数: ${needInstances}`);

// 压测脚本化：CI 中做基线对比，防止性能回退
// node bench.js --baseline bench-last.json --threshold 0.9
```
