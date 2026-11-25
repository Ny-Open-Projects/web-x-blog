---
title: [NODE-479] Node 服务的故障注入 SDK（内建韧性测试钩子）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-479：故障注入 SDK
**答**:
- 内建 vs 外部注入：外部工具（网络层 tc/proxy）能注入网络故障，但业务内故障（特定条件的 bug 场景）需要应用内钩子。内建 SDK：请求层/依赖层/定时任务层的注入点统一。
- 注入点设计：HTTP 客户端（按 URL 规则注入延迟/错误/慢响应）、DB/Redis 客户端（查询注入）、消息消费（注入处理失败）、定时器（注入跳过/重复触发）；注入条件声明（路径匹配 + 概率 + 持续时间）。
- 安全边界：注入仅在演练标识流量生效（灰度标签 NODE-370/请求头 x-chaos——只影响测试流量，不影响真实用户）、注入操作审计（谁注入的）、一键全局关闭（panic 开关 NODE-373）。
- 验收集成：每个降级声明（NODE-390）自动关联一条注入用例（"声明了 Redis 降级 → 必须有 Redis 故障注入用例通过"——降级声明与演练自动配对）。
- 观测：注入触发的降级事件验证记录（演练报告自动生成：注入了什么/降级是否生效/恢复耗时）。
```javascript
// 统一注入点（HTTP 客户端层）
function injectableFetch(url, init) {
  const rule = chaos.match(url, currentGrayTag());               // 仅演练流量生效
  if (rule?.delay) await delay(rule.delay);
  if (rule && Math.random() < rule.errRate) throw new InjectedError(rule.name);
  return fetch(url, init);
}
// 降级声明 ↔ 注入用例配对校验（CI）：
// degradeRegistry.redis 必须有 chaosCase('redis-down') 且最近 30d 内演练通过
```
