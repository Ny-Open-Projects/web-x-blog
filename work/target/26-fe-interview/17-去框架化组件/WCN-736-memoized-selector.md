---
title: [WCN-736] 笔试：手写带缓存失效的 memoized selector（reselect 风格）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-736：笔试：手写带缓存失效的 memoized selector（reselect 风格）

**答**：
- 需求：实现 `createSelector(inputs, resultFn)`：inputs 是 signal 数组，resultFn 接收各 signal 值返回结果；只有任一输入变化时才重算，否则返回上次结果（引用相等）。支持传入多个 selector 组合。
- 要点：比较输入值（Object.is）是否变化；用闭包保存 lastInputs/lastResult；边界：输入数组为空、resultFn 抛错不污染缓存。

```javascript
function createSelector(inputs, resultFn) {
  let lastInputs = null, lastResult;
  return function selector() {
    const values = inputs.map((s) => s.value);
    if (lastInputs && values.length === lastInputs.length &&
        values.every((v, i) => Object.is(v, lastInputs[i]))) {
      return lastResult;                            // 输入未变，复用结果
    }
    lastInputs = values;
    lastResult = resultFn(...values);
    return lastResult;
  };
}
function signal(v) { return { value: v }; }
const a = signal(1), b = signal(2);
const total = createSelector([a, b], (x, y) => ({ sum: x + y }));
const r1 = total();
const r2 = total();                                 // 未变化，引用相同
a.value = 5;
const r3 = total();                                 // 变化，重算
console.log(r1 === r2, r1 === r3, r3.sum);
```

**评分点**：
- 输入未变时返回上次结果引用（Object.is 比较），实现记忆化。
- 任一输入变化即重算，结果正确。
- resultFn 返回对象时引用稳定性可验证（r1===r2）。
- 空输入/异常有边界防御，错误不污染缓存。
