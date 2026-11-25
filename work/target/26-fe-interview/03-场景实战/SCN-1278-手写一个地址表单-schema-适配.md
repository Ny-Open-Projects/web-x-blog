---
title: [SCN-1278] 手写一个地址表单 schema 适配器（按国家渲染）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## SCN-1278：手写一个地址表单 schema 适配器（按国家渲染）

**答**：
- 需求：implement AddressForm(country)。fields() 返回字段顺序列表（含 label i18n key 与校验规则）；validate(values) 校验（邮编正则/必填）；normalize(values) 输出标准化地址（ISO 国家码）。
- 边界：未知国家回退 US schema；postal 可选国家（如香港）处理；values 多余字段忽略。
- 评分点：schema 适配；邮编正则；未知回退；ISO 归一

```javascript
class AddressForm {
  constructor(country = 'US') {
    this.s = SCHEMAS[country] ?? SCHEMAS.US; this.country = country;
  }
  fields() {
    return this.s.fields.map(f => ({ name: f,
      label: `addr.${this.country}.${f}`, required: true }));
  }
  validate(values) {
    const errors = {};
    for (const f of this.s.fields) {
      const v = values[f];
      if (!v) errors[f] = 'required';
      else if (f === this.s.postalField && !this.s.zip.test(v))
        errors[f] = 'invalid-zip';
    }
    return { errors, valid: !Object.keys(errors).length };
  }
  normalize(values) {
    return { country: this.country,
      ...Object.fromEntries(this.s.fields.map(f => [f, values[f] ?? ''])) };
  }
}
const SCHEMAS = {
  JP: { fields: ['postal', 'prefecture', 'city', 'street'], postalField: 'postal', zip: /^\d{7}$/ },
  US: { fields: ['street', 'city', 'state', 'zip'], postalField: 'zip', zip: /^\d{5}(-\d{4})?$/ },
};
```

## 补充：评分点与变体

**评分点**：

- `SCHEMAS[country] ?? SCHEMAS.US` 回退生效，且 `this.country` 保留原始入参，输出国家码不会错写成 US。
- 邮编正则按国家区分（JP 七位纯数字 / US 五位或五位加四位），且只在 `f === this.s.postalField` 时才取 `this.s.zip`（US 的邮编字段叫 `zip`，不能写死 `'postal'`）。
- `if (!v) errors[f] = 'required'` 会误伤合法值 0，评分点要求说明可选字段（如香港无邮编）怎么放行而不是硬报 required。
- `normalize` 只输出 schema 声明字段并补空串，多余字段被丢弃，键顺序与 `fields()` 一致。

**变体与延伸**：

1. 同一国家不同地区邮编规则不同怎么办 → schema 增加 `regions` 二级映射，按 `values.state` 选对应正则。
2. 字段顺序改由后端配置下发怎么办 → 把 `SCHEMAS` 换成运行时注入的 config，`fields()` 只做 label 拼装。
3. 校验要支持异步（地址真实性核验）怎么办 → `validate` 返回 Promise，并区分同步格式错误与异步核验失败两类错误码。
