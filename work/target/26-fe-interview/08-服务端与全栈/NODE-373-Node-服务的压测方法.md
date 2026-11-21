---
title: [NODE-373] Node 服务的压测方法与容量验证如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-373：Node 服务的压测方法与容量验证
**答**:
- 压测目标分级：容量探测（最大 QPS 与瓶颈点）、回归（版本升级后同流量性能对比）、场景验证（大促流量模型 NODE-446 的服务端版）。
- 流量模型：按真实日志回放（Gatling/k6 回放生产流量分布，比均匀打流真实）；阶梯加压（每级稳态 5 分钟，找拐点：P99 陡增即容量边界）。
- 铺垫与隔离：压测数据打标隔离（影子表/影子队列，不污染生产数据）、压测流量标识透传（监控可区分）、下游容量协同（压 BFF 会放大到下游——下游配额同步申请）。
- 瓶颈定位顺序：先外部（DB 连接池/Redis/下游限流）再内部（事件循环/内存/CPU，NODE-349/350）；常见 Node 瓶颈：JSON 大对象、单进程 CPU 饱和、连接池不足。
- 产出：容量报告（单实例 QPS、瓶颈项、扩容公式），写进容量预案；压测脚本版本化随流量模型演进。
```javascript
// k6 阶梯压测脚本
import http from 'k6/http';
export const options = {
  stages: [
    { duration: '2m', target: 200 },   // 阶梯到 200 VU
    { duration: '5m', target: 200 },   // 稳态观察
    { duration: '2m', target: 400 },   // 加压找拐点
    { duration: '5m', target: 400 },
  ],
  tags: { loadTest: 'true' }           // 流量标识透传（隔离）
};
export default () => http.get(`${__ENV.BASE}/api/goods?page=1`);
```
