---
title: [DP-166] copy-paste 改造为模式的时机如何判断？"三次法则"怎么用？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-166：copy-paste 改造为模式的时机如何判断？"三次法则"怎么用？（高频）
**答**：
- 三次法则：第一次写直接写；第二次容忍复制（相似可能是巧合）；第三次抽象（重复被证实是模式）。
- 更准的判据是"变化方向"而非重复次数：两段代码如果总是一起改（修改耦合），重复一次就该合并；如果各自演化，重复十次也别硬抽（DP-163）。
- 落地检查表：重复的是"形状"还是"语义"？改这段代码时要同步改那几段吗？抽象后的入参是不是越来越像配置对象（坏信号）？

```javascript
// 第一次 & 第二次：允许重复（各自演化方向未知）
// order 页
const total1 = items.reduce((s, i) => s + i.price * i.qty, 0);
render(`合计 ¥${total1}`);
// cart 页（复制的同款，暂时容忍）
const total2 = items.reduce((s, i) => s + i.price * i.qty, 0);
render(`合计 ¥${total2}`);
// 第三次出现 + 需求变化同步打到两处（满减规则上线两页都要改）→ 抽象时机到了
```

```javascript
// 第三次：抽取，但只抽"语义一致且一起变化"的部分
const calcTotal = (items, promotions = []) => {                // 变化点（促销）作为参数进抽象
  const subtotal = items.reduce((s, i) => s + i.price * i.qty, 0);
  return promotions.reduce((p, rule) => rule(p), subtotal);    // 变化方向一致：满减/折扣都作用于金额
};
const fullCut = (p) => (p >= 300 ? p - 40 : p);
const percentOff = (rate) => (p) => p * rate;
// 三页共用一处实现；下次满减规则变更只改这里
calcTotal(orderItems, [fullCut, percentOff(0.9)]);
calcTotal(cartItems, [fullCut]);
// 反例警戒：若两处 reduce 未来一个算金额一个算件数（语义分叉），则不抽，保持各自实现
```

---

## 二十一、综合与体系
