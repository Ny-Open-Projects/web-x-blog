---
title: [RBL-046] 笔试：手写 loader 链调度器（倒序执行 + pitch 正序 + 拦截）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-046：笔试：手写 loader 链调度器（倒序执行 + pitch 正序 + 拦截）
**题目**：实现 runLoaders(loaders, source)：1) 先正序执行 pitch，任一 pitch 返回非 undefined 值则进入「回跳」：跳过其后的 loader 常规阶段与剩余 pitch，从该 loader 前一个 loader 的常规阶段倒序执行；2) 无拦截时倒序执行常规阶段（最后一个 loader 先处理）；3) 每个 loader 以 (source, remaining) 调用；4) 返回最终转换结果与实际执行的 loader 名单；5) 画出两次执行顺序图。

```javascript
function runLoaders(loaders, source) {
  const executed = [];
  // Phase 1: pitch 正序
  let intercepted = -1;
  for (let i = 0; i < loaders.length; i++) {
    const l = loaders[i];
    executed.push(`${l.name}:pitch`);
    const ret = l.pitch ? l.pitch() : undefined;
    if (ret !== undefined) { intercepted = i; source = ret; break; }
  }
  // Phase 2: 常规阶段
  if (intercepted === -1) {
    // 完整链：从最后一个 loader 倒序执行
    for (let i = loaders.length - 1; i >= 0; i--) {
      executed.push(`${loaders[i].name}:normal`);
      source = loaders[i].fn(source);
    }
  } else {
    // 回跳：从 intercepted-1 倒序执行（intercepted 自身的常规阶段被跳过）
    for (let i = intercepted - 1; i >= 0; i--) {
      executed.push(`${loaders[i].name}:normal`);
      source = loaders[i].fn(source);
    }
  }
  return { source, executed };
}

// 示例
const loaders = [
  { name: 'a', fn: s => s + 'A', pitch: () => undefined },
  { name: 'b', fn: s => s + 'B', pitch: () => 'P' }, // 拦截
  { name: 'c', fn: s => s + 'C' },
];
console.log(runLoaders(loaders, ''));
// executed: ['a:pitch','b:pitch','a:normal']，结果 'P' + 'A'
// c 的常规阶段被跳过 —— 拦截语义
```
**评分点**：
- 无拦截：pitch 正序→常规倒序（两阶段方向相反，最常见错误点）。
- 拦截：从「被拦截 loader 的前一个」开始倒序回跳（不是从最后一个）。
- 被拦截 loader 自身常规阶段不执行。
- 返回执行轨迹便于断言（可测试性）。
- 能对应到 style-loader/babel-cache 的实际拦截应用。
