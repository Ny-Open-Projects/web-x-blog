---
title: [DP-068] 中介者 vs 观察者 vs 外观 vs 职责链，一次辨析清楚。
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-068：中介者 vs 观察者 vs 外观 vs 职责链，一次辨析清楚。
**答**：
- 中介者：多对象**双向**通过中心协作，中心有业务编排逻辑——"协调者"。
- 观察者/发布订阅：**单向广播**通知，中心（若有）不做业务编排——"传声筒"。
- 外观：对子系统做**静态封装入口**，调用方向单一——"门面"；不涉及对象间通知。
- 职责链：请求沿**链**单向流动，节点依次加工可短路——"流水线"。

```javascript
// 四个模式处理同一需求的不同形态：用户提交表单后的多模块联动
// 1. 中介者：中心知道每个模块，双向编排
class FormMediator2 {
  submit(form) {
    const valid = this.validate.check(form);
    this.loading.set(valid);                 // 主动控制各模块
    if (valid) this.api.send(form).then((r) => this.toast.show('成功'));
  }
}
// 2. 发布订阅：单向广播，模块各取所需，互不认识
// bus.emit('form:submitted', form);
// loading/toast/api 各自 bus.on('form:submitted', ...) —— 中心没有业务逻辑
// 3. 外观：静态门面，调用方只看一个方法
class FormFacade {
  async submit(form) {
    const ok = await api.send(form);          // 内部编排细节对外隐藏
    if (ok) toast.show('成功');
    return ok;
  }
}
// 4. 职责链：处理步骤依次流转，节点可短路
const chain = compose([
  async (ctx, next) => { ctx.form = normalize(ctx.form); await next(); }, // 清洗
  async (ctx, next) => { if (!ctx.form.name) throw new Error('校验失败'); await next(); }, // 拦截
  async (ctx) => { ctx.result = await api.send(ctx.form); },              // 终点
]);
// chain({ form }) —— 请求像流水线一样被加工

// 快速判别：
// 有中心且编排逻辑 -> 中介者；只广播 -> 发布订阅；固定入口 -> 外观；顺序流动可短路 -> 职责链
console.log('判别完成');
```

## 十、函数式与前端的模式变体
