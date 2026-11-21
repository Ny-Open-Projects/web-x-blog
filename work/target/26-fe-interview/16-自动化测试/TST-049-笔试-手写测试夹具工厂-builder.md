---
title: [TST-049] 笔试：手写测试夹具工厂（builder 模式 + 默认值覆盖）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-049：笔试：手写测试夹具工厂（builder 模式 + 默认值覆盖）
**答**：
- 需求：写 `makeUser(overrides)` / `makeOrder(overrides)` 夹具工厂：合理默认值 + 浅覆盖 + 深层路径覆盖（'profile.city'）；多对象间保持引用一致性（订单里的 user.id 与 user 对象一致）。
- 设计：默认值集中定义（deep clone 防污染）；覆盖用 flat key 解析（a.b.c 路径写入）；提供 `.build()` 收尾或直接返回对象。
- 边界：override 为函数时支持「基于默认值加工」（函数式覆盖）；同一工厂多次调用产出独立对象（无共享引用）。

```javascript
function makeDefaults() {
  return {
    id: 'u-1', name: '张三', vip: false,
    profile: { city: '杭州', tags: ['fe'] },
  };
}

function applyPath(obj, path, value) {
  const keys = path.split('.');
  let cur = obj;
  for (let i = 0; i < keys.length - 1; i++) cur = cur[keys[i]] ??= {};
  cur[keys.at(-1)] = value;
}

function makeUser(overrides = {}) {
  const base = structuredClone(makeDefaults());   // 独立对象，防用例间串数据
  for (const [k, v] of Object.entries(overrides)) {
    if (typeof v === 'function') v(base);         // 函数式覆盖：makeUser({ vip: (u) => { u.vip = true } })
    else if (k.includes('.')) applyPath(base, k, v);
    else base[k] = v;
  }
  return base;
}

function makeOrder(userOverrides = {}, orderOverrides = {}) {
  const user = makeUser(userOverrides);
  return structuredClone({
    id: 'o-100', userId: user.id, amount: 649,
    user,                                        // 引用一致性：order.user.id === order.userId
    ...orderOverrides,
  });
}

// ---- 用法 ----
const vipOrder = makeOrder({ vip: true }, { amount: 0 });
expect(vipOrder.user.vip).toBe(true);
expect(vipOrder.userId).toBe(vipOrder.user.id);

const hangzhou = makeUser({ 'profile.city': '深圳' });
expect(hangzhou.profile.city).toBe('深圳');
expect(hangzhou.profile.tags).toEqual(['fe']);   // 未覆盖字段保留默认
```
**评分点**：
- 每次调用产出独立深拷贝（共享默认值对象是用例污染的经典来源）。
- 支持点路径深覆盖与函数式覆盖。
- 关联对象引用一致性（userId 与 user.id）。
- 说明价值：新增字段只改默认值，所有用例自动获得，测试数据维护成本收敛到一处。
