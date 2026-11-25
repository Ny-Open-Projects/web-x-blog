---
title: [DP-336] 笔试题：手写表单 Schema 渲染器？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-336：笔试题：手写表单 Schema 渲染器？
**答**：实现 SchemaForm：1) schema 字段 → 组件映射（text/number/select/date）；2) 联动（visibleWhen）；3) 校验错误展示；4) 提交前全量校验。
**评分点**：
- 组件映射注册表（可扩展）。
- 联动求值只算受影响字段。
- 错误信息字段级绑定。
- 提交校验聚合。
```tsx
const widgets = {
  text: ({ value, onChange, error }) => <div><Input value={value} onChange={onChange}/>{error}</div>,
  number: ({ value, onChange, error }) => <div><InputNumber value={value} onChange={onChange}/>{error}</div>,
  select: ({ value, onChange, options, error }) => <div><Select value={value} onChange={onChange} options={options}/>{error}</div>,
  date: ({ value, onChange, error }) => <div><DatePicker value={value} onChange={onChange}/>{error}</div>,
};
function SchemaForm({ schema, values, setValues, onSubmit }) {
  const [errors, setErrors] = useState({});
  const visible = (f) => !f.visibleWhen || f.visibleWhen(values);       // 2) 联动
  const validateField = async (f) => {
    const err = await f.validate?.(values[f.name], values);
    setErrors(e => ({ ...e, [f.name]: err ?? undefined }));
    return err;
  };
  const submit = async (e) => {                                         // 4)
    e.preventDefault();
    const errs = await Promise.all(schema.filter(visible).map(validateField));
    if (errs.every(x => !x)) onSubmit(values);
  };
  return <form onSubmit={submit}>
    {schema.filter(visible).map(f => {                                  // 1) 注册表渲染
      const W = widgets[f.type];
      return <W key={f.name} {...f} value={values[f.name]} error={errors[f.name]}
        onChange={v => setValues(s => ({ ...s, [f.name]: v }))}/>;
    })}
    <button type="submit">提交</button>
  </form>;
}
```
