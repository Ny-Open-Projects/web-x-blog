---
title: [MFW-895] tree-shaking 结果的确定性：编译器版本和模块顺序怎么影响产物
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-895：tree-shaking 结果的确定性：编译器版本和模块顺序怎么影响产物

**答**：
- 结论：tree-shaking 依赖静态分析与模块图遍历顺序；编译器小版本变化、依赖安装顺序、符号迭代顺序都可能导致保留/剔除不同代码，产物字节变化。
- 落地：锁定编译器版本、稳定模块解析顺序、固定 minifier 配置；用产物哈希对拍检测非确定性。
- 追问钩子：sideEffects 声明为什么重要？——错误声明会让编译器过度剔除有副作用的模块，且不同版本处理不一致。

```javascript
// 对拍：两次构建产物逐字节比对
async function assertDeterministic(build) {
  const h1 = await hashBuild(await build());
  const h2 = await hashBuild(await build());
  if (h1 !== h2) {
    throw new Error('非确定性产物: ' + h1 + ' != ' + h2);
  }
  return h1;
}
// 固定输入：编译器版本、模块顺序、minify 配置
const cfg = { compiler: 'swc@1.3.x', minify: true, moduleOrder: 'sorted' };
// 若某次构建引入随机顺序 → 哈希漂移被对拍捕获
```
