---
title: [HW-044] 手写受控组件表单验证 hook
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-044：手写受控组件表单验证 hook

**答**：
- 评分点：受控核心——value 由 state 驱动，onChange 把输入写回 state（`values` 与 `errors` 分开管理）；change 时**只校验当前字段**，submit 时**全量校验**（两种时机要区分）；validator 返回错误文案或 undefined（无错误）；submit 要 preventDefault、全量校验不通过则不提交并滚到错误处；返回 `{ values, errors, handleChange, handleSubmit, reset }` 这类 API 与 Formik/antd Form 对齐；能提一句「受控 vs 非受控」——受控强一致可即时校验，非受控（defaultValue + ref）性能更好。

```javascript
// ===== 5 分钟速写版 =====
function useForm(initialValues, validators) {
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState({});
  const handleChange = (name, value) => {
    setValues(v => ({ ...v, [name]: value }));
    // 实时校验当前字段
    setErrors(e => ({
      ...e,
      [name]: validators[name] ? validators[name](value, values) : undefined
    }));
  };
  const handleSubmit = onSubmit => e => {
    e.preventDefault();
    const nextErrors = {};
    Object.keys(validators).forEach(name => {
      const err = validators[name](values[name], values);
      if (err) nextErrors[name] = err;
    });
    setErrors(nextErrors);
    if (Object.keys(nextErrors).length === 0) onSubmit(values);
  };
  return { values, errors, handleChange, handleSubmit };
}

// ===== 标准完整版（含边界处理）=====
function useFormPro(initialValues, validators, { validateOnBlur = true } = {}) {
  if (typeof initialValues !== 'object' || initialValues === null) {
    throw new TypeError('initialValues must be an object');
  }
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState({});
  const [touched, setTouched] = useState({});
  const validateField = (name, value, allValues) =>
    validators[name] ? validators[name](value, allValues) : undefined;
  const handleChange = (name, value) => {
    // 函数式更新：连续输入时基于最新值（React 批处理下直接用 values 会读到旧值）
    setValues(prev => {
      const next = { ...prev, [name]: value };
      setErrors(prevErrors => ({
        ...prevErrors,
        [name]: validateField(name, value, next)
      }));
      return next;
    });
  };
  const handleBlur = name => () => {
    if (!validateOnBlur) return;
    setTouched(t => ({ ...t, [name]: true }));
    setErrors(e => ({ ...e, [name]: validateField(name, values[name], values) }));
  };
  const validateAll = currentValues => {
    const nextErrors = {};
    Object.keys(validators).forEach(name => {
      const err = validateField(name, currentValues[name], currentValues);
      if (err) nextErrors[name] = err;
    });
    return nextErrors;
  };
  const handleSubmit = onSubmit => e => {
    e.preventDefault();
    const nextErrors = validateAll(values);
    setErrors(nextErrors);
    setTouched(Object.keys(values).reduce((t, k) => ({ ...t, [k]: true }), {}));
    if (Object.keys(nextErrors).length === 0) {
      onSubmit(values);
    }
  };
  const reset = () => {           // 提交成功或取消时恢复初始状态
    setValues(initialValues);
    setErrors({});
    setTouched({});
  };
  const isValid = Object.values(errors).every(v => v === undefined);
  return { values, errors, touched, isValid, handleChange, handleBlur, handleSubmit, reset };
}
// validators 示例：
// { phone: v => /^1\d{10}$/.test(v) ? undefined : '手机号格式不正确',
//   password: (v, all) => v.length >= 8 ? undefined : '至少 8 位' }
```

---
