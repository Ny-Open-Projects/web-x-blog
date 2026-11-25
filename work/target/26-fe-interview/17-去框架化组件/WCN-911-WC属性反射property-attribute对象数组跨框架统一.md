---
title: [WCN-911] WC 属性反射协议：React 传 property、Vue 传 attribute，对象/数组怎么统一
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-911：WC 属性反射协议：React 传 property、Vue 传 attribute，对象/数组怎么统一

**答**：
- 结论先行：HTML attribute 只能是字符串，复杂值（对象/数组/函数）必须走 DOM property；跨框架差异的根源就是「React 对自定义元素倾向设 property、Vue 模板倾向写 attribute」。
- 统一策略：组件协议层声明每个 prop 的类型（string 走 attribute，object/function 走 property），适配层负责 `el.setAttribute` 或 `el.prop = value` 的路由（大促商品卡 props 常是 SKU 对象）。
- 布尔值坑：`disabled` 这种只要出现即为真的 attribute，框架传 `disabled={false}` 时不能 setAttribute('disabled','false')，要移除属性或设 property=false。
- 反射（reflection）：property 变化是否回写 attribute 要显式约定，避免「property 是权威、attribute 是快照」的双源冲突；建议单向：property 为源，attribute 仅初始化。
- 追问钩子：面试官问「函数回调 prop 怎么跨框架传」——答：函数只能走 property，且要注意 this 绑定与框架事件系统差异，通常改用 CustomEvent 派发更稳。

```javascript
// 属性适配：按类型路由到 attribute / property
function applyProp(el, key, value, spec) {
  const type = spec[key] || 'string';
  if (type === 'object' || type === 'function') {
    el[key] = value;                    // 复杂值走 property
  } else if (type === 'boolean') {
    value ? el.setAttribute(key, '') : el.removeAttribute(key);
  } else {
    el.setAttribute(key, String(value)); // 字符串走 attribute
  }
}
const card = document.createElement('product-card');
applyProp(card, 'sku', { id: 1, price: 99 }, { sku: 'object' });
applyProp(card, 'disabled', false, { disabled: 'boolean' });
console.log(card.sku, card.hasAttribute('disabled')); // {id:1,price:99} false
```
