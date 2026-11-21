---
title: [R19-176] React 组件如何封装为 Web Component？两套体系如何互操作？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-176：React 组件如何封装为 Web Component？两套体系如何互操作？
**答**：
- 价值：把 React 组件发布成自定义元素，供 Vue/Angular/原生页面直接使用，是跨框架分发的通用方案（React 19 也正式支持在 JSX 中直接用自定义元素）。
- 封装模式：customElements.define 一个宿主元素，内部用 createRoot 挂 React 组件；attribute 变化 -> observedAttributes -> 转 props 重渲染；事件用 CustomEvent 冒泡。
- 边界处理：只传字符串的 attribute 不够表达复杂 props，用 property setter + JSON 约定；子内容用 slot（React 侧包装 children）。
- 陷阱：每次 attribute 变化不能重复 createRoot；样式隔离建议 Shadow DOM + 将关键样式内联进 shadow。

```tsx
// define-react-element.ts —— React 组件封装为 Web Component
import { createRoot, type Root } from 'react-dom/client';
import { StrictMode } from 'react';

type Props = Record<string, unknown>;

export function defineReactElement(
  tagName: string,
  Component: (props: Props) => React.ReactNode,
) {
  if (customElements.get(tagName)) return; // 防重复注册

  class ReactBridge extends HTMLElement {
    private root: Root | null = null;
    private mountPoint: HTMLDivElement | null = null;
    static get observedAttributes() {
      return ['title', 'count', 'disabled']; // 简单值走 attribute
    }

    connectedCallback() {
      this.attachShadow({ mode: 'open' });            // 样式隔离
      this.mountPoint = document.createElement('div');
      this.shadowRoot!.appendChild(this.mountPoint);
      this.root = createRoot(this.mountPoint);        // 生命周期内只 createRoot 一次
      this.render();
    }

    attributeChangedCallback() {
      this.render();                                  // attribute 变化 -> 重渲染 React
    }

    disconnectedCallback() {
      // React 19：root.unmount 可传清理回调
      this.root?.unmount();
      this.root = null;
    }

    // 复杂 props 走 property：el.items = [...]
    get items() { return JSON.parse(this.getAttribute('items-json') ?? '[]'); }
    set items(v: unknown[]) { this.setAttribute('items-json', JSON.stringify(v)); this.render(); }

    private render() {
      const props: Props = {
        title: this.getAttribute('title') ?? '',
        count: Number(this.getAttribute('count') ?? 0),
        disabled: this.hasAttribute('disabled'),
        items: this.items,
        // React -> 宿主：onAction 转发为 CustomEvent
        onAction: (detail: unknown) => {
          this.dispatchEvent(new CustomEvent('action', { detail, bubbles: true }));
        },
      };
      this.root?.render(<StrictMode><Component {...props} /></StrictMode>);
    }
  }
  customElements.define(tagName, ReactBridge);
}

// 声明：<x-counter title="计数" count="3"></x-counter>
// 监听：el.addEventListener('action', e => console.log(e.detail))

// React 19 反向互操作：JSX 里直接使用自定义元素（无需 @lit/react 包装）
function Page() {
  return <x-counter title="计数" count={3} onAction={() => console.log('fired')} />;
}
// React 19 识别 onAction -> 对应自定义元素的事件监听，而不再是普通 prop 透传

// 注册入口
import CounterApp from './counter-app';
defineReactElement('x-counter', CounterApp);
```
