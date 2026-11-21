---
title: [NODE-570] Node 服务的 Push 通道（APNs/FCM/厂商）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-570：Push 通道服务
**答**:
- 通道矩阵：iOS APNs、Android FCM + 各厂商通道（小米/华为/OPPO——国内到达率依赖厂商通道）——设备 token 登记（多通道注册：App 上报各通道 token）、通道选择（按设备品牌路由——优先厂商通道）。
- 发送链路：消息构建（平台 payload 协议：标题/正文/深链/角标——统一协议 adapter 转换各平台格式 NODE-552 同构）、批量发送（分批限速——厂商 QPS 限制）、失败处理（token 失效清理：410/BadDeviceToken → 删除订阅——设备换机清理）、重发与去重。
- 到达与效果：到达回执（厂商回执/端上报送达——到达率统计）、打开追踪（点击深链——推送转化数据）、角标管理（服务端角标数同步——ARC-523 未读联动）。
- 合规：推送频控与用户偏好（NODE-568 统一去重合并——Push 不绕过）、静默推送（后台数据同步——低频使用）。
- 对账：发送量 vs 厂商回执对账、token 有效性巡检（定期清理僵尸 token——通道质量）。
```javascript
async function push(deviceTokens, msg) {
  for (const t of deviceTokens) {
    const ch = channelFor(t);                                    // 按品牌路由
    const r = await ch.send(transform(msg, ch)).catch(e => {
      if (ch.isTokenDead(e)) return tokens.remove(t);            // 失效清理
      return retryQueue.add({ t, msg });
    });
    trackDelivery(msg.id, t, r);
  }
}
```
