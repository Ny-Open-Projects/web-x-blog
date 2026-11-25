---
title: [OPS-132] RUM 采样策略怎么设计？采样率过高/过低各有什么问题？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-132：RUM 采样策略怎么设计？采样率过高/过低各有什么问题？
**答**：
- 全量上报成本高、10% 以下采样又会让低频页面样本不足——按"会话级确定性采样"：同一会话所有事件同进同出，保证单用户数据完整。
- 错误类事件永不采样（低频高价值）；性能类按基础采样率；灰度期新版本采样率临时提高到 50% 加速收敛。
- 采样会引入偏差：报 p75/p95 必须注明样本量；样本不足的指标显示"insufficient"而不是抖动的数字。
- bot 与预渲染流量剔除，否则 LCP 分布被爬虫污染。
- 采样率做成远程配置：出事故时可临时调到 100% 抓现场，平时回归低采样。

```javascript
// RUM 采样：会话级确定性采样 + 错误全量 + 远程可调
const config = {
  baseSampleRate: 0.1,                       // 常规流量 10%
  // 会话 id 哈希决定采样：同一会话所有事件同进同出，用户级数据完整
  shouldSample(sessionId) {
    if (isBot()) return false;               // 爬虫/预渲染剔除，防指标污染
    if (isNewGrayVersion()) return 0.5;      // 新版本灰度期提高到 50%，加速收敛
    const hash = [...sessionId].reduce((a, c) => (a * 31 + c.charCodeAt(0)) >>> 0, 0);
    return hash % 100 < config.baseSampleRate * 100;
  },
  alwaysReport: ['js_error', 'resource_error', 'api_5xx'],   // 错误永不采样
};

// 采样率从远程配置读取：事故时可临时调 100% 抓现场，避免发版
// 报告规范：p75/p95 必须附带样本量；样本不足的指标标记 insufficient 而非裸数字
```
