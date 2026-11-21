---
title: [WCN-102] WCN 在 React 中如何封装？React 19 对自定义元素的改进与旧版痛点？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 跨框架复用]
type: 面试题
---

## WCN-102：WCN 在 React 中如何封装？React 19 对自定义元素的改进与旧版痛点？

**答**：
- React ≤18 三个痛点：① 非 string/number 的 props 会被序列化为 attribute（对象/函数/数组丢失）；② 自定义事件不认识，要 ref 手动 addEventListener；③ SSR 输出 unknown element 标签且不注入任何配置。
- React 19 改进：props 与 element property/attribute 智能匹配——元素上有同名 property 时按 property 传递（对象/函数可用）；事件 props（onXxx）按 CustomEvent 监听规则自动绑定；ref 指向元素本身。
- 封装模式一：薄包装 `forwardRef` + useEffect 绑定事件 + JSX.IntrinsicElements 类型声明，让 `<x-dialog onclose={...}>` 有完整 TS 支持。
- 封装模式二：用 `@lit/react` 的 createComponent 自动生成（事件映射表声明式）。
- 仍需注意：attributeOnly 组件在 18 的老项目里要用白名单序列化或直接 setAttribute。

```tsx
// React 19 直接使用 + 类型声明
import type { DetailedHTMLProps, CustomElements } from 'react';
declare module 'react' {
  namespace JSX {
    interface IntrinsicElements {
      'x-dialog': DetailedHTMLProps<React.HTMLAttributes<HTMLElement> & {
        open?: boolean; ondialogclose?: (e: CustomEvent<{ action: string }>) => void;
      }, HTMLElement>;
    }
  }
}

export function Confirm() {
  return (
    <x-dialog open ondialogclose={(e) => console.log(e.detail.action)}>
      <button>确定</button>   {/* light DOM 通过 slot 投影 */}
    </x-dialog>
  );
}
```
