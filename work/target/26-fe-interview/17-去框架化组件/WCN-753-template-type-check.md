---
title: [WCN-753] 编译响应式框架如何做跨组件类型推导与模板类型检查？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-753：编译响应式框架如何做跨组件类型推导与模板类型检查？

**答**：
- 结论：为每个组件生成 `.d.ts`，模板编译器把模板转成 TS 虚拟代码（如 Volar 的 virtual file），交给 TS 语言服务做类型检查与补全。
- props/emit/slots 都从组件定义推导类型；模板里表达式映射到虚拟 TS 的对应位置，实现「模板里写错属性名也报错」。
- 追问钩子：自定义元素（WC）没有 .d.ts 怎么办？考察从 Custom Elements Manifest 生成类型声明的方案。

```javascript
// 组件定义 -> 虚拟 TS（供语言服务检查）
const def = { props: { size: String, disabled: Boolean }, emits: ['change'] };
function genVirtualCode(def) {
  return `
declare const props: { size?: string; disabled?: boolean };
// 模板 <Comp size="large" disabled /> 会映射到此处的类型检查
const checked: boolean = props.disabled;
`;
}
console.log(genVirtualCode(def));
// 没有 d.ts 的 WC：从 Custom Elements Manifest 生成
const manifest = { tagName: 'ds-button', attributes: [{ name: 'size', type: 'string' }] };
```
