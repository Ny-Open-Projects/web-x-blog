---
title: [FRP-186] 手写 v-model 的三个修饰符：.lazy / .number / .trim 的完整实现？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-186：手写 v-model 的三个修饰符：.lazy / .number / .trim 的完整实现？

**答**：
- 修饰符的本质是**编译期把 modifiers 传给运行时**，运行时在"事件 → 赋值"的管道里插入转换：`.lazy` 把 input 事件换成 change、`.number` 用 toNumber 转换、`.trim` 去首尾空格。
- 完整实现：一个通用的 `assignEventValue(el, value, modifiers, cb)` 管道，按修饰符顺序处理（trim → number，lazy 只影响事件类型）。
- 细节：`.number` 输入非数字时保留原字符串（toNumber 返回原值），避免输入中途被清空；`.lazy` 失焦才同步，配合表单校验场景。
- 自定义组件上的修饰符走 modelModifiers prop（见 FRP-136），原生表单上直接在指令/编译产物里处理。

```javascript
// 简化实现，帮助理解 v-model 修饰符
// 编译产物对照：
// <input v-model.lazy.trim="msg" />
// =>
// withDirectives(h('input', {
//   'onUpdate:modelValue': $event => ((_ctx.msg) = $event),
//   value: _ctx.msg
// }, null, 512), [[vModelText, _ctx.msg, '', { lazy: true, trim: true }]])
// —— modifiers 对象进入指令的 binding

const vModelText = {
  created(el, { modifiers: { lazy, trim, number } }, vnode) {
    // 赋值管道：修饰符按序转换后写回（el 一起闭包传入）
    el.__assign = makeAssign(el, vnode, { trim, number });

    // 事件选择：lazy 用 change（失焦），否则 input
    const event = lazy ? 'change' : 'input';
    el.addEventListener(event, () => {
      el.__assign(el.value);
    });
    if (!lazy) {
      // 组合输入法（中文 IME）期间不同步 —— 真实实现的必要细节
      el.addEventListener('compositionstart', () => el.__composing = true);
      el.addEventListener('compositionend', () => {
        el.__composing = false;
        el.__assign(el.value);
      });
    }
  },
  beforeUpdate(el, { value, oldValue, modifiers: { trim, number } }) {
    // 外部值变化 -> 同步回 DOM（受控方向的另一半）
    if (document.activeElement !== el) {           // 焦点内不覆盖用户输入
      if (trim && value === oldValue) {
        el.value = value.trim();                   // 值未变但需要 trim 视图
      } else if (value !== el.value || number) {
        el.value = value ?? '';
      }
    }
  }
};

function makeAssign(el, vnode, { trim, number }) {
  return function assign(value) {
    if (el.__composing) return;                    // IME 期间跳过
    let v = value;
    if (trim) v = v.trim();                        // 1. trim 先行
    if (number || vnode.props?.type === 'number') {
      v = toNumber(v);                             // 2. number：转不动就保留字符串
    }
    vnode.props['onUpdate:modelValue'](v);         // 3. 触发更新
  };
}

function toNumber(v) {
  const n = parseFloat(v);
  return isNaN(n) ? v : n;   // 'abc' -> 'abc'（不清空输入），'12a' -> parseFloat 得 12
}

// 验证三种修饰符：
// <input v-model.number="age">    输入 '25'  -> age = 25；输入 'abc' -> age = 'abc'
// <input v-model.trim="name">     输入 ' hi ' -> name = 'hi'
// <input v-model.lazy="draft">    键入过程不更新，失焦才同步
```
