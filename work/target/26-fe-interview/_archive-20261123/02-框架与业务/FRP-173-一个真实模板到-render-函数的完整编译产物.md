---
title: [FRP-173] 一个真实模板到 render 函数的完整编译产物长什么样？（输入输出对照）
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-173：一个真实模板到 render 函数的完整编译产物长什么样？（输入输出对照）

**答**：
- 编译三阶段落地的完整示例：parse 生成 AST → transform（静态提升、patchFlag 标注、block 收集）→ generate 拼出代码字符串。
- 产物特征：helpers 按需 import（用到什么导什么）、静态子树提升到作用域外（只创建一次）、动态节点带 patchFlag + dynamicProps、事件走缓存。
- `_openBlock/_createElementBlock` 组织 Block 树：动态后代节点按扁平顺序收集进 `dynamicChildren`，diff 时跳过静态部分直接走这个列表。
- 从输出反推优化动机：产物里的每个"奇怪变量"都对应一个运行时优化（见 FRP-013/060-063）。

```javascript
// 简化实现，帮助理解模板到 render 的对照
// —— 输入模板 ——
// <div id="app">
//   <span>静态标题</span>
//   <span>{{ msg }}</span>
//   <button @click="go">go</button>
// </div>
//
// —— 编译产物（实际 SFC 编译输出，去掉部分 noise） ——
const _hoisted_1 = { id: "app" };          // 静态 props 提升对象
const _hoisted_2 = /*#__PURE__*/_createElementVNode("span", null, "静态标题"); // 完整静态节点提升
const _hoisted_3 = /*#__PURE__*/_createElementVNode("span", null, "go");       // 按钮文本提升

export function render(_ctx, _cache) {
  return (_openBlock(), _createElementBlock("div", _hoisted_1, [
    _hoisted_2,                                              // 静态：不进 dynamicChildren，diff 跳过
    _createElementVNode("span", null,                        // 动态文本：patchFlag = TEXT(1)
      _toDisplayString(_ctx.msg), 1 /* TEXT */),
    _createElementVNode("button", {
      onClick: _cache[0] || (_cache[0] = (...args) => (_ctx.go && _ctx.go(...args)))
    }, [                                                     // 事件缓存：handler 不再是每次新建
      _hoisted_3
    ])
  ]));
}
// helpers 按需导入（生成代码头部）：
// import { createElementVNode, createElementBlock, openBlock, toDisplayString }
//   from 'vue' —— 只导入用到的，tree-shaking 友好

// —— 最小化生成器示意 ——
function generate(ast) {
  const ctx = { code: '', helpers: new Set() };
  genFunctionPreamble(ctx);                       // helpers import + 静态提升变量
  genFunctionDecl(ast, ctx);                      // export function render(_ctx, _cache)
  walk(ast.children, ctx);                        // 递归：遇到动态绑定
  //   ctx.helpers.add('toDisplayString')
  //   ctx.code += `, 1 /* TEXT */`               // patchFlag 注解
  return ctx.code;
}
```
