---
title: [MFW-345→MFW-345] API Sunset 执行器（弃用到删除的自动化）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## MFW→345：Sunset 执行器

**答**:
- 生命周期自动化：deprecated 声明（{ route, sunsetAt, successor }) → 运行时三动作（响应自动附 Sunset 头+替代 Link / 按 caller 白名单延迟个人为期限 / 到期切 410+文档跳转）——人只做决策，执行器做纪律
- 流量驱动延期：sunsetAt 前 7 天仍有关键调用方（内部一二级服务/大客户）→ 自动提案延期（附调用方清单——数据决策不拍脑袋）；外部僵尸流量（爬虫/弃用客户端）不构成延期理由
- 观测闭环：弃用路由调用量周曲线（应单调下降——不降说明通知渠道失效，升级触达）
- 删除日动作：路由删 + 契约测试移除 + 文档归档（留 410 说明页一年——外链用户体验兜底）

```javascript
function sunsetGate(route, { now = Date.now(), callers }) {
  if (now < dateOf(rule.sunsetAt)) return attachSunsetHeaders()          // 附头+计调用方
  const critical = callers.onPlan?.filter((c) => c.tier >= 2 && c.seen7d)
  if (critical.length) return autoProposeExtend({ by: critical })        // 数据驱动延期
  return gone410WithDoc()                                                // 到期：410+跳转
}
// 周曲线不降 → 升级触达（owner 直邮+群 @）
```
