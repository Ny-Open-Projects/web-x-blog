---
title: [WCN-603] 为什么说 Web Components 是「框架无关的组件契约层」，落地时契约包含哪几部分？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-603：为什么说 Web Components 是「框架无关的组件契约层」，落地时契约包含哪几部分？

**答**：
- 结论：契约 = 标签名 + 属性/Property 协议 + 事件协议 + Slot 内容协议 + 样式定制点（::part/CSS 变量），与框架无关。
- 属性进、事件出：复杂数据走 property（避免属性序列化丢失类型），用户交互走 CustomEvent 且 composed/bubbles 均为 true，才能穿透 Shadow DOM。
- 追问钩子：契约变更如何管理？用版本化 + 契约测试（golden 快照），破坏性变更必须升大版本——考察平台化治理意识。

```javascript
// 契约的五个部分集中声明，便于生成文档与契约测试
const CONTRACT = {
  tag: 'ds-datepicker',
  props: { value: 'string', disabled: 'boolean', min: 'string' },
  events: ['ds-change', 'ds-open'],
  slots: ['prefix', 'footer'],
  cssVars: ['--ds-primary', '--ds-radius'],
  parts: ['input', 'calendar'],
};
function emit(el, type, detail) {
  el.dispatchEvent(new CustomEvent(type, {
    detail, bubbles: true, composed: true,
  }));
}
// 任何框架只需遵守 CONTRACT 即可消费，平台据此生成 wrapper 与测试用例
```
