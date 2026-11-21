---
title: [TST-267] 边缘渲染（Deno Deploy/Cloudflare）的测试特殊性？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-267：边缘渲染（Deno Deploy/Cloudflare）的测试特殊性？
**答**：
- 运行时差异：边缘无完整 Node API（无 fs/部分 crypto 不同）——单测在目标运行时仿真下跑（miniflare）。
- 冷启动预算：边缘函数初始化时长断言（依赖精简验证）。
- 地理行为：不同 region 的路由/缓存行为用 header 模拟（cf-ipcountry）。
- 本地-边缘一致性：本地 dev 与部署后关键页面输出 diff 抽查。

```javascript
import { Miniflare } from 'miniflare';
const mf = new Miniflare({ script: edgeFn, bindings: mockBindings });
const res = await mf.dispatchFetch('https://x.test/goods/1');
expect(res.status).toBe(200);                        // 边缘运行时内验证
r
```
