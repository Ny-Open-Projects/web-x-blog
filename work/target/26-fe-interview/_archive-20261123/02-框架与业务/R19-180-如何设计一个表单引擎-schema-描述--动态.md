---
title: [R19-180] 如何设计一个表单引擎（schema 描述 -> 动态渲染 -> 校验联动）？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-180：如何设计一个表单引擎（schema 描述 -> 动态渲染 -> 校验联动）？
**答**：
- 三段架构：**schema**（JSON 描述字段/布局/校验/联动）-> **引擎**（递归渲染器 + 字段注册表 + 联动表达式求值）-> **消费**（校验器可插拔：JSON Schema/zod/自定义 rules）。
- 渲染器核心是"字段注册表"：`type -> Component` 映射，新控件注册即用，引擎本身不感知具体控件。
- 联动语义收敛为三个正交维度：显隐（visible）、可写（disabled）、值计算（compute），全部接收 `(values, ctx)` 纯函数，避免 if-else 堆叠。
- 校验时机与错误展示统一在引擎层收口，业务只需声明 rules；性能上用 `useField` 级订阅防全表单重渲染。

```tsx
// form-engine.tsx —— schema 表单引擎
import { createContext, useContext, useMemo, useState, useCallback } from 'react';

// ---- 1. Schema 类型 ----
type FieldSchema = {
  name: string;
  label: string;
  type: 'input' | 'number' | 'select' | 'date';
  required?: boolean;
  props?: Record<string, unknown>;
  // 三个正交联动维度：纯函数，输入当前全量值
  visible?: (values: Record<string, any>) => boolean;
  disabled?: (values: Record<string, any>) => boolean;
  compute?: (values: Record<string, any>) => any;
  rules?: ((v: any, values: any) => string | null)[];
};

// ---- 2. 字段注册表：新控件注册即用 ----
const registry = {
  input: (p: any) => <input {...p} />,
  number: (p: any) => <input type="number" {...p} />,
  select: ({ options = [], ...p }: any) => (
    <select {...p}>{options.map((o: any) => <option key={o.value} value={o.value}>{o.label}</option>)}</select>
  ),
  date: (p: any) => <input type="date" {...p} />,
};

// ---- 3. 字段级订阅：只有自己变的字段重渲染 ----
const FormCtx = createContext<any>(null);
function useField(name: string) {
  const { values, setValue, errors } = useContext(FormCtx);
  return {
    value: values[name],
    error: errors[name],
    onChange: useCallback((v: any) => setValue(name, v), [name, setValue]),
  };
}

function Field({ schema }: { schema: FieldSchema }) {
  const { values, errors } = useContext(FormCtx);
  const { value, error, onChange } = useField(schema.name);
  if (schema.visible && !schema.visible(values)) return null; // 显隐联动
  const Comp = registry[schema.type];
  const disabled = schema.disabled?.(values) ?? false;
  return (
    <label style={{ display: 'block', opacity: disabled ? 0.5 : 1 }}>
      {schema.label}
      <Comp
        value={value ?? ''}
        disabled={disabled}
        onChange={(e: any) => onChange(e.target?.value ?? e.target)}
        {...schema.props}
      />
      {error && <em style={{ color: 'red' }}>{error}</em>}
    </label>
  );
}

// ---- 4. 引擎：状态、联动、校验收口 ----
export function FormEngine({ schema, fields, onSubmit }: {
  schema: { fields: FieldSchema[] };
  fields: FieldSchema[];
  onSubmit: (values: any) => void;
}) {
  const [values, setValues] = useState(schema.fields.reduce((a, f) => ({ ...a, [f.name]: undefined }), {}));
  const [errors, setErrors] = useState<Record<string, string>>({});

  const setValue = useCallback((name: string, v: any) => {
    setValues(prev => {
      const next = { ...prev, [name]: v };
      // 值联动：compute 字段重算
      fields.forEach(f => { if (f.compute) next[f.name] = f.compute(next); });
      return next;
    });
    setErrors(prev => ({ ...prev, [name]: '' })); // 输入即清错
  }, [fields]);

  const validate = useCallback(() => {
    const errs: Record<string, string> = {};
    fields.forEach(f => {
      const v = values[f.name];
      if (f.required && (v === undefined || v === '')) errs[f.name] = `${f.label}必填`;
      f.rules?.some(rule => { const msg = rule(v, values); if (msg) { errs[f.name] = msg; return true; } return false; });
    });
    setErrors(errs);
    return Object.keys(errs).length === 0;
  }, [fields, values]);

  const ctx = useMemo(() => ({ values, setValue, errors }), [values, setValue, errors]);

  return (
    <FormCtx.Provider value={ctx}>
      <form onSubmit={e => { e.preventDefault(); if (validate()) onSubmit(values); }}>
        {fields.map(f => <Field key={f.name} schema={f} />)}
        <button type="submit">提交</button>
      </form>
    </FormCtx.Provider>
  );
}

// ---- 5. 业务声明式使用 ----
// <FormEngine
//   schema={{ fields: [
//     { name: 'type', label: '类型', type: 'select', required: true,
//       props: { options: [{ value: 'a', label: 'A' }, { value: 'b', label: 'B' }] } },
//     { name: 'aCode', label: 'A 编码', type: 'input', required: true,
//       visible: v => v.type === 'a' },                       // 显隐联动
//     { name: 'total', label: '合计', type: 'number',
//       disabled: () => true,
//       compute: v => (v.aPrice ?? 0) * (v.count ?? 0) },     // 值联动
//     { name: 'name', label: '名称', type: 'input',
//       rules: [v => v && v.length < 2 ? '至少两个字符' : null] },
//   ] }}
//   onSubmit={save}
// />
```
