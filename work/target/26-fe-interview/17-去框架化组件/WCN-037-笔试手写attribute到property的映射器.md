---
title: [WCN-037] 笔试：手写 attribute → property 类型化映射器（boolean/number/string/object）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Web Components]
type: 笔试题
---

## WCN-037：笔试：手写 attribute → property 类型化映射器

**题目**：实现 `createProps(spec)` 帮助 WC 组件做 attribute 声明式配置：spec 形如 `{ disabled: 'boolean', max: 'number', label: 'string', data: 'json' }`。要求：① 生成 observedAttributes 数组；② 提供把 attribute 值转为类型化 property 的 `parse(name, raw)`：boolean 空串为 true、缺省为 false；number NaN 回落默认；json 解析失败回落默认并 warn 一次；③ 提供 `reflect(el, name, value)` 反向写回（boolean 用存在性、json 序列化）；④ 单元测试口径：`<x-item disabled max="10" data='{"a":1}'>`。

**答**：

```javascript
export function createProps(spec) {
  const observed = Object.keys(spec);
  const defaults = { boolean: false, number: 0, string: '', json: null };
  const warned = new Set();

  function parse(name, raw) {
    const type = spec[name];
    if (raw === null) return defaults[type];       // attribute 不存在
    switch (type) {
      case 'boolean': return raw !== 'false';       // '' / 任意值 → true
      case 'number': {
        const n = Number(raw);
        return Number.isNaN(n) ? defaults.number : n;
      }
      case 'string': return raw;
      case 'json': {
        try { return JSON.parse(raw); }
        catch {
          if (!warned.has(name)) { warned.add(name); console.warn(`invalid json attr: ${name}`); }
          return defaults.json;
        }
      }
    }
  }

  function reflect(el, name, value) {
    const type = spec[name];
    switch (type) {
      case 'boolean':
        value ? el.setAttribute(name, '') : el.removeAttribute(name);
        break;
      case 'json':
        value === null || value === undefined
          ? el.removeAttribute(name)
          : el.setAttribute(name, JSON.stringify(value));
        break;
      default:
        el.setAttribute(name, String(value));
    }
  }
  return { observed, parse, reflect };
}

// 用法：class XItem extends HTMLElement {
//   static #props = createProps({ disabled: 'boolean', max: 'number', data: 'json' });
//   static get observedAttributes() { return XItem.#props.observed; }
//   attributeChangedCallback(n, o, v) { if (o !== v) this[n] = XItem.#props.parse(n, v); }
// }
// <x-item disabled max="10" data='{"a":1}'> → { disabled:true, max:10, data:{a:1} }
```

**评分点**：
- boolean 语义正确：存在即为 true、`'false'` 特判为 false、缺失为 false。
- number 的 NaN 回落与 json 的 try/catch + 单次 warn（防日志风暴）。
- reflect 与 parse 互为逆运算，boolean 用存在性而不是 `"true"/"false"` 混写。
- observedAttributes 从 spec 派生，配置单一来源。
