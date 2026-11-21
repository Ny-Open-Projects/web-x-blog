---
title: [NODE-494] Node 服务的 BFF 多端协议适配（一后多端差异）如何组织？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-494：BFF 多端协议适配
**答**:
- 差异维度：字段裁剪（小程序带宽敏感 → 精简字段）、结构差异（App 需要预计算的展示字段/H5 现算）、交互差异（Web 分页/App 流式 cursor）。
- 组织方式演进：端专属接口（/h5/goods、/app/goods——清晰但重复多）→ 参数化（同一接口 + client 参数差分——收敛但参数爆炸）→ 端 profile（端声明 profile：字段集/结构模板——BFF 按profile 装配，推荐形态 ARC-414 组合）。
- profile 管理：profile 注册表（每端的字段裁剪/结构模板声明式配置）、默认 profile（未覆盖的端走默认全量——防新端漏配）、差异最小化原则（profile 差异要 justify——无理由的差异是维护负担）。
- 演进：端能力协商（ARC-556 客户端能力头）与 profile 融合（能力决定 profile 选择）；废弃 profile 清理（端版本渗透后 ARC-556）。
- 验证：多端协议一致性测试（同数据各 profile 输出的业务语义一致——字段可裁剪语义不可变）。
```javascript
// profile 装配
const profiles = {
  h5:  { fields: ['id', 'name', 'price', 'thumb'], page: 'cursor' },
  app: { fields: ['id', 'name', 'price', 'imgs', 'badges'], page: 'cursor', precompute: true }
};
function assemble(data, client) {
  const p = profiles[client.profile] ?? defaultProfile;
  return pick(data, p.fields, { page: p.page, precompute: p.precompute });
}
```
