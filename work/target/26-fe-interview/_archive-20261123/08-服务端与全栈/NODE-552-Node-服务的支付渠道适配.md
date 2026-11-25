---
title: [NODE-552] Node 服务的支付渠道适配（多渠道统一抽象）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-552：支付渠道适配
**答**:
- 渠道抽象：统一支付协议（下单/查询/退款/关单/对账——每渠道一个 adapter 实现：微信/支付宝/银联/国际渠道 NODE-425 防腐层），路由策略（按支付方式/金额/费率/可用性——渠道选择器配置化）。
- 协议差异收敛：渠道状态映射（各渠道状态 → 统一状态机：created/paying/success/failed/closed）、金额单位（各渠道分/元——adapter 内转换）、签名差异（各渠道签名算法封装——应用层只见统一凭证）。
- 回调统一：回调验签 → 幂等处理 → 统一事件（pay.succeeded 事件）——回调路由到 adapter 验签再进业务。
- 可靠性：渠道超时与重试策略独立（NODE-352）、渠道降级（主渠道故障 → 备用渠道——收银台渠道列表刷新）、对账文件（各渠道对账单格式 → 统一解析入对账引擎 ARC-382）。
- 演进：新渠道接入成本评估（adapter 模板 + 契约测试模板——接入标准化）、渠道质量监控（成功率/到账时效按渠道——路由权重数据）。
```javascript
class ChannelAdapter {                                            // 统一接口
  async create(payOrder) {} async query(payNo) {} async refund(r) {} async parseCallback(raw) {}
}
const routes = { wechat: WechatAdapter, alipay: AlipayAdapter };
// 统一状态映射：{ WX: { SUCCESS: 'success', CLOSED: 'closed' }, ... } → 统一状态机
```
