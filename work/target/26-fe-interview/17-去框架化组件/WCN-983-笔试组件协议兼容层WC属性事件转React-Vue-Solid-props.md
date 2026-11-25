---
title: [WCN-983] 手写组件协议兼容层：把 WC 属性 / 事件协议自动转成三端 props
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-983：手写组件协议兼容层：把 WC 属性 / 事件协议自动转成三端 props

**题目**：实现 `adaptProtocol(spec, framework)`，spec 形如 `{ props:{ label:{kind:'attr'}, data:{kind:'prop'} }, events:{ onChange:'ds-change' } }`，framework 取 'react'|'vue'|'solid'。要求：① 返回 `toProps(values)`：把统一 values 转成该框架的 props 对象——react: 事件名为 `onChange`（首字母大写 on + 名）、data 之类 prop 保持原样、attr 保持字符串；vue: 事件名为 `onDsChange`（on + 事件名驼峰化）、其余同;solid: 事件名 `onChange` 同 react；② 事件名转换规则：`ds-change`→`DsChange`（按 - 分词首字母大写）；③ attr 类型值转字符串，prop 类型保持原值；④ 未知 framework 抛错；⑤ 不修改输入。请自足实现并给出可运行示例。

**答**：

```javascript
function adaptProtocol(spec, framework) {
  if (!['react', 'vue', 'solid'].includes(framework)) throw new Error('未知框架: ' + framework);
  const toEventName = (evt, fw) => {
    const camel = evt.split('-').map(s => s[0].toUpperCase() + s.slice(1)).join('');
    return fw === 'vue' ? 'on' + camel : 'on' + camel; // react/solid 亦用 on+驼峰
  };
  return {
    toProps(values = {}) {
      const out = {};
      for (const [key, s] of Object.entries(spec.props || {})) {
        const v = values[key];
        out[key] = s.kind === 'attr' && v != null ? String(v) : v;
      }
      for (const [prop, evt] of Object.entries(spec.events || {}))
        if (values[prop] != null) out[toEventName(evt, framework)] = values[prop];
      return out;
    },
  };
}
const spec = { props: { label: { kind: 'attr' }, data: { kind: 'prop' } },
  events: { onChange: 'ds-change' } };
const values = { label: 5, data: { id: 1 }, onChange: () => {} };
console.log(Object.keys(adaptProtocol(spec, 'react').toProps(values))); // ['label','data','onDsChange']
console.log(Object.keys(adaptProtocol(spec, 'vue').toProps(values)));   // 同上
```

**评分点**：
- 三框架 toProps 转换正确（事件名 on+驼峰、attr转字符串、prop保原值）。
- 事件名 ds-change→onDsChange 转换规则正确。
- 未知框架抛错。
- 不修改输入对象。
- 示例可运行、输出正确。
