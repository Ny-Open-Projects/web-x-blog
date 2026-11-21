---
title: [OPS-065] Mock 平台与接口契约在工程里怎么落地？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-065：Mock 平台与接口契约在工程里怎么落地？
**答**：
- 契约先行：接口定义（OpenAPI/自定义 schema）是前后端的共同事实源，mock 数据、类型生成、联调验收都从契约出发。
- mock 平台提供：本地开发 mock、staging 挡板（后端未就绪时前端先开发）、异常场景注入（超时/500/弱网）。
- CI 中做契约测试：mock server 用真实契约，后端联调时 diff 真实响应与契约，不一致即阻断。
- 生产发布前置检查里加一条：涉及接口变更的 MR 必须附契约 diff 与双方确认。

```javascript
// mock/server.js：基于契约的 mock server（node 原生，无依赖）
import { createServer } from 'node:http';
import contract from './contract.json' with { type: 'json' };

// contract.json 片段：
// { "GET /api/items": { "delay": 100, "status": 200,
//     "schema": { "type": "object", "required": ["list", "total"],
//       "properties": { "list": { "type": "array" }, "total": { "type": "number" } } },
//     "body": { "list": [{"id": 1, "name": "商品A"}], "total": 42 } } }

const server = createServer(async (req, res) => {
  const key = `${req.method} ${req.url.split('?')[0]}`;
  const spec = contract[key];

  if (!spec) {
    res.writeHead(404, { 'Content-Type': 'application/json' });
    return res.end(JSON.stringify({ code: 'NOT_IN_CONTRACT', key }));
  }
  // 异常注入：?__mock=timeout/500 模拟故障场景
  const mode = new URL(req.url, 'http://x').searchParams.get('__mock');
  if (mode === 'timeout') return setTimeout(() => res.destroy(), 30_000);
  if (mode === '500') {
    res.writeHead(500, { 'Content-Type': 'application/json' });
    return res.end(JSON.stringify({ code: 'MOCK_500' }));
  }

  await new Promise(r => setTimeout(r, spec.delay ?? 0));
  res.writeHead(spec.status, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify(spec.body));
});

server.listen(4001, () => console.log('mock on :4001'));
```
