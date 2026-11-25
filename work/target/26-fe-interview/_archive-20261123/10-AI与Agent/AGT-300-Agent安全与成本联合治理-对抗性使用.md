---
title: [AGT-300] 对抗性使用与滥用防护——恶意用户怎么薅坏你的 Agent？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-300：恶意用户滥用 Agent（刷成本/套数据/绕限制）怎么防护？

**答**:
- 滥用形态与对策：成本攻击（故意诱导长任务/循环→单用户配额+任务成本熔断 AGT-277+异常模式检测）、数据套取（诱导 Agent 复述系统提示/吐出训练语料/翻越 ACL→系统提示防提取+行级权限+输出 DLP 扫描 AGT-285）、绕过限制（多账号/自动化脚本→设备指纹+行为风控+速率限制）。
- 风控信号：请求模式异常（高频相似请求/典型的注入试探序列）、成本异常（单用户成本分布突变）、内容异常（高频触发拦截）——风控引擎按信号评分，高危限流/封禁/人审。
- 分层处置：软限制（降速/加验证码）→ 硬限制（配额锁）→ 账号处置（封禁+申诉通道）——处置可申诉，误杀有出口；黑产对抗是持久战，规则持续更新。
- 平衡体验：风控误伤率要监控（正常用户被限的比例），新用户冷启动宽松+成熟账号严格——安全与增长平衡。

```javascript
async function abuseGuard(user, req) {
  const score = await riskEngine.score({
    rate: user.ratePattern,          // 请求模式
    cost: user.costPercentile,       // 成本分布
    content: await detectProbe(req), // 注入试探特征
  });
  if (score > 0.9) return hardLimit(user);      // 配额锁
  if (score > 0.7) return throttle(user) || captcha();
  return normal(user);                           // 全量审计留痕
}
// 误伤率监控 + 申诉通道；规则滚动更新。
```
