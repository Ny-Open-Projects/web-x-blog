---
title: [AGT-312] 电商导购 Agent——实时商品理解与营销合规怎么兼顾？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-312：电商导购/比价 Agent 的实时数据与营销合规怎么设计？

**答**:
- 实时数据接入：价格/库存/优惠实时查询走工具（不进 prompt 缓存——价格秒变），Agent 只负责理解需求与组织话术——时效数据永远工具直查（AGT-268 时效幻觉治理）。
- 导购逻辑：需求澄清（预算/场景/偏好）→ 候选召回（推荐系统出候选，Agent 不自选商品——避免幻觉商品）→ 对比呈现（结构化对比卡，规格/价格/评价摘要）→ 引导决策不误导。
- 营销合规：禁用绝对化用语（"最便宜/第一"词表拦截）、价格承诺谨慎（"当前价"非"保证最低价"）、不诋毁竞品——营销话术合规词表+输出扫描。
- 转化归因：Agent 会话的转化率/客单价与普通导购对照（AGT-259 A/B），推荐列表的曝光点击数据回流推荐系统——导购 Agent 是推荐系统的对话式前端。

```javascript
async function shoppingAgent(req) {
  const pref = await clarify(req);              // 预算/场景澄清
  const cands = await recommender(pref);        // 推荐系统出候选
  const live = await Promise.all(cands.map(p =>
    priceTool(p.id)));                          // 实时价格工具查
  const card = compare(live, { ban: MARKETING_BANLIST });
  return scan(card);                            // 合规扫描
}
// 商品只能来自推荐系统（防幻觉商品），
// 价格只来自实时工具。
```
