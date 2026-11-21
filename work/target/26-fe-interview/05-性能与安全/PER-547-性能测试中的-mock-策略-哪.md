---
title: [PER-547] 性能测试中的 mock 策略：哪些东西要 mock 掉、哪些必须保留真实链路？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-547：性能测试中的 mock 策略：哪些东西要 mock 掉、哪些必须保留真实链路？

**答**：
- mock 掉的是**随机性与外部依赖**：A/B 分流（锁分支）、广告与个性化（固定快照）、第三方统计脚本（防污染外部系统）、支付/短信等外部副作用（打标进影子通道）。
- 必须保留真实的是**被测链路本身**：CDN 真实下载（体积与 HTTP 行为是性能本体）、真实图片/字体资源、主接口的真实响应体积与结构（mock 响应太小会让压测结论严重失真）。
- 灰色地带是后端服务：全链路压测要真实（打标），单前端性能测试要 mock（后端波动会污染前端指标），按测试目的选。
- 原则一句话：mock 的唯一合法理由是"消除与被测对象无关的噪声"，任何为了省事而 mock 被测链路的行为都是造假。

```javascript

const mockPolicy = {
  mock: {
    abSdk: 'force control 分支',         // 消除分流随机性
    ads: '固定快照 + 尺寸占位',           // 消除内容随机性但保留体积
    analytics: '不发出（stub 上报）',     // 防污染外部系统
    payment: '影子通道',                  // 副作用隔离
  },
  keepReal: {
    cdnAssets: true,   // 真实下载是性能本体
    apiPayload: true,  // 响应体积必须真实，否则 LCP 结论失真
    webfont: true,
  },
  rule: 'mock 只允许消除与被测对象无关的噪声',
};
console.log(mockPolicy.rule);
```
