---
title: [NODE-577] Node 服务的接口防爬（行为识别/分级响应）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-577：接口防爬
**答**:
- 爬虫识别：行为特征（访问序列规律性/频率曲线/无 JS 执行——与真人行为分布对比）、设备特征（无指纹/模拟器信号 ARC-575）、账号特征（批量注册/固定节奏）、网络特征（IDC IP 段/代理池）。
- 分级响应（NODE-458 谱系）：限速（隐形降速——返回慢而不是 403，防对方察觉调参）、投毒（部分返回假数据——增加爬取成本，业务合规评估）、验证码挑战（NODE-613）、封禁（IP/设备/账号——风控名单）。
- 实现位：网关层（频率/黑名单快速拦截）+ 应用层（行为序列风控——NODE-456 引擎）、数据层（敏感数据水印——泄露溯源 ARC-630）。
- 成本对抗：爬虫成本抬高策略（数据分页深度限制/字段裁剪/动态渲染依赖）——防爬是经济战不是技术战（抬高成本到不划算）。
- 观测：爬虫流量占比、分级处置统计、误伤率（正常用户被挑战——体验监测）。
```javascript
// 分级防爬决策
async function antiCrawl(ctx) {
  const score = await risk.assess(ctx, { signals: ['rate', 'behavior', 'device', 'ip'] });
  if (score > 0.9) return block(ctx);                            // 封禁
  if (score > 0.7) return challenge(ctx);                        // 验证码
  if (score > 0.5) return throttle(ctx, 0.3);                    // 隐形降速
}
```
