---
title: [JS-207] async/await 与生成器的关系：编译产物怎么实现
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 异步]
type: 面试题
---

## JS-207：async/await 与生成器的关系

**答**：
- 语义等价：async 函数 ≈ Promise 驱动的生成器；await ≈ yield + 自动 co——Babel 编译产物（regenerator-runtime）就是把 async 函数转成 function* + 驱动器
- 区别：async/await 是语言级语法（原生引擎实现，性能好、栈信息好）；生成器是通用控制流原语（不限于异步）
- 生成器独占能力：双向通信、惰性序列、无限流——await 做不到
- 面试话术：能写出「10 行 co + function* 等价于 async 函数」是理解深度的硬证明

```javascript
// 两种写法语义完全一致
async function main() {
  const a = await fetchA();
  return await fetchB(a);
}
function* mainGen() {
  const a = yield fetchA();   // yield ≈ await
  return yield fetchB(a);
}
co(mainGen); // Promise 结果相同
```
