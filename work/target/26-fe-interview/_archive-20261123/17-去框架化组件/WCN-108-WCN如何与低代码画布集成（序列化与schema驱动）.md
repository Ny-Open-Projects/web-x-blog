---
title: [WCN-108] WCN 如何与低代码画布集成？schema 驱动渲染与拖入识别怎么实现？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 跨框架复用]
type: 面试题
---

## WCN-108：WCN 如何与低代码画布集成？schema 驱动渲染与拖入识别怎么实现？

**答**：
- schema 驱动：物料协议用 `{ tag, attrs, children, slot }` JSON 描述 WC 树；渲染器 `createElement + setAttribute + appendChild`（或 innerHTML 白名单构建）递归还原；框架无关是 WCN 的天然优势。
- 拖入识别：物料库注册"可放置 tag 清单"，拖拽到画布时创建 unknown element（define 可延迟）先渲染占位，drop 后按 manifest 补 attribute。
- 画布交互与组件冲突：编辑态要拦截组件自身交互（点击选中而不是触发按钮）——常见做法是渲染"幽灵实例"（影子树内 pointer-events:none + 蒙层），真实组件仅在预览态启用。
- 属性面板绑定 manifest：attribute 类型/枚举驱动表单生成；事件绑定输出为 `wc-event` 声明（消费侧再注册监听）。
- 代码导出：schema → HTML/DSD 片段或带 import 的 vanilla js 代码，供"导出静态页"。

```javascript
// 迷你 schema 渲染器
function renderSchema(node) {
  const el = document.createElement(node.tag);
  for (const [k, v] of Object.entries(node.attrs ?? {})) {
    typeof v === 'object' ? ((el[k] = v), null) : el.setAttribute(k, v);
  }
  for (const child of node.children ?? []) {
    typeof child === 'string'
      ? el.append(child)
      : child.slot ? Object.assign(el.append(child.tag), { slot: child.slot })
      : el.append(renderSchema(child));
  }
  return el;
}
// { tag:'x-card', attrs:{ title:'标题' }, children:[ {tag:'x-input', attrs:{label:'姓名'}} ] }
```
