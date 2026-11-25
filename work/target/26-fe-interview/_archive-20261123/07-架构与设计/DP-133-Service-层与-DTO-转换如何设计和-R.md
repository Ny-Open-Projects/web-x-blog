---
title: [DP-133] Service 层与 DTO 转换如何设计？和 Repository 怎么分工？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-133：Service 层与 DTO 转换如何设计？和 Repository 怎么分工？（高频）
**答**：
- 分层：组件 → Service（业务编排、组合多个仓库、事务语义）→ Repository（数据存取）→ HTTP；DTO 是传输层形状，与领域模型解耦。
- DTO 转换收益：后端字段变更（snake_case、冗余字段、脏数据）被隔离在 fromDTO/toDTO，领域模型始终干净稳定。
- Service 示例：下单 = 校验库存仓库 + 创建订单仓库 + 扣优惠券仓库，一个业务动作编排三个仓库，组件只调一个方法。

```javascript
// DTO ↔ 领域模型：字段映射与清洗集中一处
class User {
  constructor({ id, name, vipLevel }) { Object.assign(this, { id, name, vip: vipLevel >= 3 }); }
  static fromDTO(dto) {                                       // 传输形状 → 领域模型
    return new User({ id: dto.user_id, name: dto.nickname?.trim() || '匿名用户', vipLevel: dto.vip_level ?? 0 });
  }
  toDTO() { return { user_id: this.id, nickname: this.name, vip_level: this.vip ? 5 : 0 }; }
}
// Repository：纯存取（见 DP-132）
class OrderRepository { constructor(http) { this.http = http; } create(payload) { return this.http.post('/orders', payload); } }
class CouponRepository { constructor(http) { this.http = http; } use(id) { return this.http.post(`/coupons/${id}/use`); } }
class StockRepository { constructor(http) { this.http = http; } lock(skus) { return this.http.post('/stock/lock', skus); } }
// Service：业务编排层，组件只面对它
class CheckoutService {
  constructor(orderRepo, couponRepo, stockRepo) { Object.assign(this, { orderRepo, couponRepo, stockRepo }); }
  async checkout(cart, couponId) {
    await this.stockRepo.lock(cart.skus);                     // 步骤1 锁库存
    if (couponId) await this.couponRepo.use(couponId);        // 步骤2 核销优惠券
    const order = await this.orderRepo.create({               // 步骤3 建单
      skus: cart.skus, couponId, amount: cart.total,
    });
    return order;
  }
}
const checkout = new CheckoutService(orderRepo, couponRepo, stockRepo);
await checkout.checkout(cart, 'C1001');                        // 组件一行调用，不关心编排细节
```
