---
title: [FRP-136] defineModel 的实现原理是什么（v-model 参数与修饰符如何处理）？（高频）
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-136：defineModel 的实现原理是什么（v-model 参数与修饰符如何处理）？（高频）

**答**：
- `defineModel()` 宏编译为三件事：① 在 props 声明里加 `modelValue` 与 `modelModifiers`；② 内部创建一个**自定义 ref**：get 读 `props.modelValue`，set 时 `emit('update:modelValue', v)`；③ 返回这个 ref，使用上与普通 ref 无异。
- 修饰符（`v-model.trim`）编译到 `modelModifiers` prop：setter 里先按修饰符转换（trim/number）再 emit；自定义修饰符同样进这个对象，由组件自己解释。
- 带参数 `defineModel('title')` → 对应 `props.title` + `emit('update:title')`；未传值时（父没用 v-model）回落到**本地 ref**，变更后 emit 但本地也更新——这就是"非受控可用"的实现。
- 本地兜底值的变化不会反向影响父——严格保持"父优先"语义，除非父绑定存在。

```javascript
// 简化实现，帮助理解 defineModel 的编译产物
// 源码：
//   const model = defineModel({ default: 0 })
//   const title = defineModel('title', { set: v => v.trim() })
// 产物（伪代码）：
function compiledSetup(props, { emit }) {
  // ① 宏被展开为对内部 API 的调用
  const model = useModel(props, 'modelValue', { default: 0 });
  const title = useModel(props, 'title', { set: v => v.trim() });

  model.value = 3;   // 自动变成 emit('update:modelValue', 3) —— 使用侧无感
  return { model, title };
}

// —— useModel 简化实现（真正干活的） ——
function useModel(props, name, options = {}) {
  const modifiers = props[`${name}Modifiers`] || {};          // ② 修饰符从 props 来
  const localValue = ref(props[name] ?? options.default);     // 非受控兜底
  const isParentBound = () => props[name] !== undefined;      // 父是否绑定了 v-model

  return customRef((track, trigger) => ({
    get() {
      track();
      return isParentBound() ? props[name] : localValue.value;
    },
    set(value) {
      // ③ 修饰符管道：先转换再 emit
      if (modifiers.trim)  value = value.trim();
      if (modifiers.number) value = toNumber(value);
      if (options.set) value = options.set(value);           // 3.4+ 的 get/set 转换选项
      localValue.value = value;                              // 本地同步（非受控时也有值）
      emit(`update:${name}`, value);                         // ④ 通知父
    }
  }));
}

// 父组件 <Child v-model.trim="msg" /> 编译产物：
// h(Child, { modelValue: msg, 'onUpdate:modelValue': v => (msg = v), modelModifiers: { trim: true } })
// 子组件内 model.value = '  hi  ' -> modifiers.trim 生效 -> emit('update:modelValue', 'hi')
```
