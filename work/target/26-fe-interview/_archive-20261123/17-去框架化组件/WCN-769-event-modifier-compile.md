---
title: [WCN-769] 模板里的事件修饰符（.stop/.prevent/.once）是如何被编译的？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-769：模板里的事件修饰符（.stop/.prevent/.once）是如何被编译的？

**答**：
- 结论：编译器解析 `@click.stop.prevent` 的修饰符，生成一个包裹函数：`e => { e.stopPropagation(); e.preventDefault(); handler(e) }`，把声明式修饰符转成命令式调用，运行时无需解析修饰符字符串。
- `.once` 编译为「调用后移除监听器」的包装；`.capture` 影响 addEventListener 的第三个参数；按键修饰符 `.enter` 编译为 `e.key === 'Enter'` 判断。
- 追问钩子：`.passive` 为什么不能和 `.prevent` 一起用？考察「passive 监听器里 preventDefault 无效且被浏览器忽略」的底层约束。

```javascript
// 模板：<button @click.stop.prevent.once="submit">提交</button>
function compileHandler(handler, mods) {
  let body = '';
  if (mods.includes('stop')) body += 'e.stopPropagation();';
  if (mods.includes('prevent')) body += 'e.preventDefault();';
  body += `handler(e);`;
  let fn = `function(e){${body}}`;
  if (mods.includes('once')) fn = `function(e){${body} e.currentTarget.removeEventListener(e.type, this);}`;
  return new Function('handler', `return ${fn}`);
}
const wrapped = compileHandler((e) => console.log('submit'), ['stop', 'prevent']);
const fake = { stopPropagation() {}, preventDefault() {} };
wrapped(fake);
```
