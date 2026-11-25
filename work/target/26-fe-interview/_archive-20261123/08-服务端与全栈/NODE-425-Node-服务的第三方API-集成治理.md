---
title: [NODE-425] Node 服务的第三方 API 集成治理（适配器/超时/降级）如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-425：第三方 API 集成治理
**答**:
- 适配器层隔离：第三方 SDK/HTTP 调用收口在 adapter 包（统一接口签名），第三方变更只改 adapter；业务不直接 import 第三方包（防腐层思想，ARC-145）。
- 可靠性配置化：每第三方声明超时/重试/熔断/降级（外部服务必挂心态——预算化超时 NODE-377、降级数据/异步补偿队列）、限流遵守（对方的 rate limit 是硬约束——客户端限流器提前控制，避免 429 浪费）。
- 一致性处理：第三方数据与本方数据的冲突裁决（以谁为准的规则显式化）、字段映射版本（第三方 schema 变更的兼容层）。
- 成本与配额：调用量计量（按第三方分账 NODE-479 思想）、配额耗尽预警、缓存第三方结果（减少调用）。
- 监控与演练：第三方错误率/延迟单独看板、第三方故障演练（NODE-408 验证降级真实生效）、SLA 记录（对方的承诺与实际对比——谈判与备份选型依据）。
```javascript
// 第三方适配器（防腐层）
class SmsAdapter {
  constructor(client) { this.client = client; }                  // 可替换实现
  async send(phone, tplId, params) {
    return withPolicy('sms', { timeout: 2000, retries: 2, breaker: true },
      () => this.client.send({ to: phone, template: tplId, params }));
  }
}
// 降级：sms 挂 → 入队补偿队列延后重发（验证码类不接受降级，显式报错）
```
