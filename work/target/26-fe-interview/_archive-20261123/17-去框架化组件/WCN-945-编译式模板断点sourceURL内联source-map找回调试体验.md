---
title: [WCN-945] 编译式模板断点打不到表达式：怎么用 sourceURL / 内联映射找回调试体验
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-945：编译式模板断点打不到表达式：怎么用 sourceURL / 内联映射找回调试体验

**答**：
- 结论先行：模板被编译成 `new Function` 或 eval 字符串时，浏览器里它只是匿名 eval 代码，没有文件、没有断点——靠 `//# sourceURL=xxx.js` 给它一个虚拟文件名，DevTools 才能打开并下断点。
- 内联 source map：对 eval/Function 生成的代码用 `//# sourceMappingURL=data:application/json;base64,...` 内联 map，映射到模板源码，实现「在模板表达式上打断点」。
- 开发/生产分叉：dev 模式保留 sourceURL + 内联 map（体积不重要），生产模式彻底剥离 new Function（CSP 也禁 eval），改用预编译产物。
- CSP 冲突：严格 CSP 禁止 unsafe-eval，编译式模板要么构建期预编译、要么用 `trustedTypes` + 受限求值，不能运行时 eval。
- 追问钩子：面试官问「sourceURL 会不会污染生产」——答：只在 dev 注入，生产构建通过环境变量剔除，避免虚拟文件名出现在错误上报里。

```javascript
// 编译式模板：给生成的函数一个可调试的虚拟文件名
function compileTemplate(tpl) {
  const js = `return (ctx) => ${tpl};`;
  const debug = `\n//# sourceURL=tpl://Card.js`; // DevTools 里可打开下断点
  return new Function(js + debug)();
}
const render = compileTemplate('ctx.user.name');
console.log(render({ user: { name: 'Ada' } })); // Ada
// 更进一步：内联 source map 映射到模板源码
// return fn + '\n//# sourceMappingURL=data:application/json;base64,...'
```
