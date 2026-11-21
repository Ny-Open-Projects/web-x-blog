---
title: [JS-173] 代码分层与依赖方向如何设计？领域逻辑与 UI 分离怎么做？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-173：代码分层与依赖方向如何设计？领域逻辑与 UI 分离怎么做？

**答**：
- 四层结构：UI 层 → 应用层 → 领域层 → 基础设施，依赖只能自上而下单向流动。
- 领域层是纯函数：只做业务规则计算，不碰 DOM/网络/框架，因此可以脱离浏览器单测。
- 应用层编排：组合领域逻辑与基础设施调用，不写业务规则，也不关心 UI。
- UI 层只做展示与事件转发：按钮回调里出现 `reduce` 算金额就是分层被击穿的信号。
- 好处：规则集中可复用（Web/小程序/App 共用领域层）、逻辑可单测、换框架不重写业务。

```javascript
// 依赖方向：UI → 应用 → 领域 → 基础设施（箭头只能向下）

// 1. 领域层：纯函数，零环境依赖，可直接单测
const orderDomain = {
  calcTotal(items) {
    return items.reduce((s, i) => s + i.price * i.qty, 0);
  },
  canCheckout(items) {
    return items.length > 0 && items.every((i) => i.stock > 0);
  },
};

// 2. 应用层：编排领域逻辑 + 基础设施
const orderService = {
  async checkout(items) {
    if (!orderDomain.canCheckout(items)) throw new Error('存在无库存商品');
    const total = orderDomain.calcTotal(items);
    return api.post('/orders', { items, total });   // 依赖基础设施 api
  },
};

// 3. UI 层：只做转发与展示
checkoutBtn.onclick = async () => {
  try {
    await orderService.checkout(state.items);
    showToast('下单成功');
  } catch (e) {
    showToast(e.message);
  }
};

// 反例（分层被击穿）：按钮回调里直接写业务规则
// checkoutBtn.onclick = () => { let t = 0; items.forEach(i => t += i.price * i.qty); ... }
// 规则散落后：无法单测、多端重复实现、改优惠逻辑要全局搜代码
```
