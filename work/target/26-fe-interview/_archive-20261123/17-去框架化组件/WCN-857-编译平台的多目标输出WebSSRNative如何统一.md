---
title: [WCN-857] 编译平台的「多目标输出」（Web / SSR / Native）如何统一？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-857：编译平台的「多目标输出」（Web / SSR / Native）如何统一？

**答**：
- 结论先行：统一靠「同一份 IR + 不同后端 + 统一运行时契约」——前端只解析一次，IR 承载全部语义，各后端生成目标代码，但都依赖一套行为一致的最小运行时（读信号、调度、DOM/宿主 API 适配）。
- 后端差异：Web 后端生成「创建 DOM + 细粒度绑定」指令；SSR 后端生成「字符串拼接 + 初始状态序列化」代码（无 DOM/effect）；Native 后端把模板编译成原生视图指令（如小程序/Flutter 模板）——差异只在「怎么表达更新」。
- 统一运行时契约：定义抽象操作（`createElement`/`setText`/`bindEffect`/`hydrate`），各平台用不同实现——编译产物调用同一套 API，运行时按平台注入实现，从而「一份组件代码多端运行」。
- 水合桥接：SSR 产物输出 HTML + 状态快照，Web 后端产物负责「采用」这些 DOM（hydrate）而非重建——两端要约定 DOM 结构与状态注入格式。
- 边界：不是所有能力都能多端统一（平台特有 API 如 WebGL、原生手势），用「平台能力探测 + 降级/条件编译」处理，避免为了统一牺牲体验。
- 追问钩子：面试官会问「SSR 里没有 effect 怎么办」——答：SSR 后端在编译期把响应式表达式静态求值成初始 HTML，effect 只在客户端激活阶段建立——这是「编译时求值 + 运行时接管」的组合。

```javascript
// 统一运行时契约 + 多后端
const runtime = {
  web:     { setText: (el, v) => el.textContent = v, bind: (fn) => queueMicrotask(fn) },
  ssr:     { setText: (_, v) => v, bind: (fn) => fn() },                     // 编译期静态求值
  native:  { setText: (id, v) => nativeBridge.setText(id, v), bind: (fn) => fn() },
};
function emit(ir, target) {
  return ir.exprs.map(e => `${target}.setText(node, ${e.expr})`).join('\n');
}
// 同一 IR，不同目标
const ir = { exprs: [{ expr: 'count * 2' }, { expr: 'user.name' }] };
console.log('== web ==\n' + emit(ir, 'web'));
console.log('== ssr ==\n' + emit(ir, 'ssr'));
// 运行时注入：import runtime[platform] 实现具体 setText/bind
```
