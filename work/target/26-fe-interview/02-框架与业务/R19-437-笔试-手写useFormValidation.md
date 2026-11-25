---
title: [R19-437] 笔试：手写 useFormData（受控表单 + 校验 + 提交锁）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 表单]
type: 笔试题
---

## R19-437：笔试：手写 useFormData

**答**：实现 `useFormData(initial, { validators })`：① values 单一 state 对象（不可变更新）；② setField(name, value) + 动态字段；③ 校验：blur 触发单字段校验（errors 独立 state）、提交前全量校验聚焦第一个错误；④ 提交锁（submitting 防重复）；⑤ touched 跟踪（只有碰过的字段才显示错误——避免首屏红字）。写出实现。

```javascript
export function useFormData(initial, { validators = {} } = {}) {
  const [values, setValues] = useState(initial);
  const [errors, setErrors] = useState({});
  const [touched, setTouched] = useState({});
  const [submitting, setSubmitting] = useState(false);
  const firstErrorRef = useRef(null);

  const validateField = useCallback(async (name, v) => {
    const fn = validators[name];
    if (!fn) return true;
    const msg = await fn(v, values);
    setErrors((e) => ({ ...e, [name]: msg || undefined }));
    return !msg;
  }, [values]);

  const setField = useCallback((name, value) => {
    setValues((s) => ({ ...s, [name]: value }));
    setTouched((t) => ({ ...t, [name]: true }));
    if (touched[name]) validateField(name, value);    // 已碰过才实时校验
  }, [touched, validateField]);

  const blurField = useCallback((name) => {
    setTouched((t) => ({ ...t, [name]: true }));
    validateField(name, values[name]);
  }, [values, validateField]);

  const submit = useCallback(async (onSubmit) => {
    if (submitting) return;                            // 提交锁
    const results = await Promise.all(
      Object.keys(validators).map((n) => validateField(n, values[n])));
    const badField = Object.keys(validators).find((n, i) => !results[i]);
    if (badField) { firstErrorRef.current?.focus(); return; }  // 聚焦第一个错误
    setSubmitting(true);
    try { await onSubmit(values); } finally { setSubmitting(false); }
  }, [values, validators, submitting, validateField]);

  return { values, errors: pickTouched(errors, touched), setField, blurField, submit, submitting, firstErrorRef };
}
```

**评分点**：
- values 不可变更新（单一 state 对象）
- touched 门控（未碰字段不显错）与 blur 实时校验
- 提交锁 + 全量校验聚焦第一个错误
- errors 独立 state（校验不牵连输入组件）
