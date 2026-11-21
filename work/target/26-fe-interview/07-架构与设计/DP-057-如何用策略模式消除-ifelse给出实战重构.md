---
title: [DP-057] 如何用策略模式消除 if-else？给出实战重构。
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-057：如何用策略模式消除 if-else？给出实战重构。
**答**：
- 可消除的 if-else 特征：分支彼此独立、每支都在做"一类算法/一类处理"、分支集合会持续增长。
- 重构三步：提炼每支为策略函数 → 建立 `key -> 策略` 映射 → 调用处改为查表 + 兜底（默认策略）。
- 不要矫枉过正：两三个分支、语义就是"分类讨论"时，if-else 反而更清晰；映射表的 key 必须是稳定枚举值。
- 进阶：Map 注册表支持运行时注册（插件化），符合 OCP。

```javascript
// 重构前：权限判断的 if-else 泥潭
function calcPrice(origin, user) {
  if (user.level === 'vip1') return origin * 0.95;
  else if (user.level === 'vip2') return origin * 0.9;
  else if (user.level === 'svip') return origin * 0.8;
  else if (user.level === 'employee') return origin * 0.5;
  else return origin;
}
// 每加一个等级都要改函数体，且折扣逻辑散落在分支里

// 重构后：策略表 + 兜底
const priceStrategies = {
  vip1: (p) => p * 0.95,
  vip2: (p) => p * 0.9,
  svip: (p) => p * 0.8,
  employee: (p) => p * 0.5,
  default: (p) => p, // 兜底策略：未知等级走原价
};
const calcPriceV2 = (origin, user) => (priceStrategies[user.level] || priceStrategies.default)(origin);
console.log(calcPriceV2(100, { level: 'svip' }));     // 80
console.log(calcPriceV2(100, { level: 'unknown' }));  // 100 —— 新等级不再炸掉

// 运行时可注册：插件化扩展（OCP）
const strategyRegistry = new Map(Object.entries(priceStrategies));
function registerStrategy(level, fn) { strategyRegistry.set(level, fn); }
registerStrategy('annual', (p) => p * 0.7); // 新增等级零修改
const calcPriceV3 = (origin, user) => strategyRegistry.get(user.level)?.(origin) ?? origin;
console.log(calcPriceV3(100, { level: 'annual' })); // 70
```
