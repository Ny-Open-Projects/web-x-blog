---
title: [WCN-912] 原生 CustomEvent 不被 React 合成事件捕获，跨框架事件怎么桥接
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-912：原生 CustomEvent 不被 React 合成事件捕获，跨框架事件怎么桥接

**答**：
- 结论先行：React 17+ 把事件委托挂在 root 容器上，WC 从 shadow DOM 派发的 CustomEvent 需设置 `composed: true, bubbles: true` 才能穿透影子树并被根捕获。
- 三个标志缺一不可：`bubbles` 让它冒泡、`composed` 让它越过 shadow boundary、`detail` 携带 payload（微前端子应用事件常被这个漏掉）。
- React 侧监听：对自定义元素用 `ref` + `addEventListener` 手动绑定，或用 `onEventName` 需框架支持（React 19 才较好支持自定义事件 prop）。
- 事件命名规范：与框架事件区分用命名空间前缀（如 `ds-change`），避免和原生 `change` 混淆导致双重处理。
- 追问钩子：面试官问「事件在 shadow DOM 里 retarget 后 target 变了怎么办」——答：用 `event.composedPath()[0]` 拿到真实派发元素，做精确判断。

```javascript
// WC 派发（composed 穿透影子树）+ React ref 手动桥接
class DsInput extends HTMLElement {
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    const input = document.createElement('input');
    input.addEventListener('input', e => {
      this.dispatchEvent(new CustomEvent('ds-change', {
        detail: { value: e.target.value },
        bubbles: true, composed: true, // 关键：越过 shadow boundary
      }));
    });
    root.appendChild(input);
  }
}
customElements.define('ds-input', DsInput);
// React 侧：
function ReactForm() {
  const ref = useRef(null);
  useEffect(() => {
    const h = e => console.log('react got:', e.detail.value);
    ref.current.addEventListener('ds-change', h);
    return () => ref.current.removeEventListener('ds-change', h);
  }, []);
  return <ds-input ref={ref} />;
}
```
