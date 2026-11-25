---
title: [WCN-920] 手写统一组件协议描述符（contract）：输入/输出/主题/生命周期的 schema 校验器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-920：手写统一组件协议描述符（contract）：输入/输出/主题/生命周期的 schema 校验器

**题目**：实现 `createContractValidator(contract)`，contract 形如 `{ name, props: { label: { type:'string', required:true }, size: { type:'enum', values:['s','m','l'] }, data: { type:'object' } }, events: ['ds-change'], themeTokens: ['--ds-primary'] }`。要求：① `validateProps(props)` 返回 `{ ok, errors:[...] }`，校验 required、类型（string/number/boolean/object/enum）、enum 取值；② `validateEvents(emitted)` 检查派发的事件是否在声明列表，返回未知事件告警；③ `assertTheme(tokens)` 返回缺失的 themeTokens；④ 错误信息包含 prop 名与期望/实际；⑤ 全部方法对非对象输入健壮（不抛异常，返回错误）。请自足实现并给出可运行示例。

**答**：

```javascript
function createContractValidator(contract) {
  const typeOk = (v, t) => ({
    string: x => typeof x === 'string', number: x => typeof x === 'number',
    boolean: x => typeof x === 'boolean', object: x => x !== null && typeof x === 'object',
    enum: () => true,
  }[t] || (() => true))(v);
  return {
    validateProps(props) {
      const errors = [];
      const p = (props && typeof props === 'object') ? props : {};
      if (!props || typeof props !== 'object') errors.push('props 非对象');
      for (const [key, spec] of Object.entries(contract.props || {})) {
        const v = p[key];
        if (spec.required && v === undefined) { errors.push(`${key}: required 缺失`); continue; }
        if (v !== undefined && !typeOk(v, spec.type)) errors.push(`${key}: 期望 ${spec.type}，实际 ${typeof v}`);
        if (spec.type === 'enum' && v !== undefined && !spec.values.includes(v))
          errors.push(`${key}: 应为 ${spec.values.join('/')}，实际 ${v}`);
      }
      return { ok: errors.length === 0, errors };
    },
    validateEvents(emitted = []) {
      const allowed = new Set(contract.events || []);
      return (Array.isArray(emitted) ? emitted : [])
        .filter(e => !allowed.has(e)).map(e => `未知事件: ${e}`);
    },
    assertTheme(tokens = {}) {
      return (contract.themeTokens || []).filter(t => !(t in tokens));
    },
  };
}
const v = createContractValidator({
  name: 'ds-button',
  props: { label: { type: 'string', required: true }, size: { type: 'enum', values: ['s','m','l'] } },
  events: ['ds-change'], themeTokens: ['--ds-primary'],
});
console.log(v.validateProps({ label: 'OK', size: 'xl' })); // size 错误
console.log(v.validateEvents(['ds-change', 'ds-bogus'])); // 未知事件
console.log(v.assertTheme({})); // 缺失 --ds-primary
```

**评分点**：
- validateProps 覆盖 required/类型/enum 三类校验，错误信息含 prop 名与期望实际。
- validateEvents 检出未声明事件并给出告警。
- assertTheme 返回缺失 token 列表。
- 全部方法对非对象输入健壮，不抛异常。
- 返回结构符合约定、示例可运行且输出正确。
