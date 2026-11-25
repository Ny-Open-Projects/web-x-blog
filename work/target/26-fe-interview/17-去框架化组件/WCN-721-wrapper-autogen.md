---
title: [WCN-721] React/Vue/Angular 的 WC wrapper 如何从元数据自动生成并保持同步？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-721：React/Vue/Angular 的 WC wrapper 如何从元数据自动生成并保持同步？

**答**：
- 结论：定义一份组件元数据（tag、props 类型、事件、slots），用代码生成器产出各框架 wrapper；React wrapper 处理 property 与事件订阅，Vue wrapper 处理 v-model 与自定义事件。
- 把生成纳入 CI：元数据变更自动生成并 diff，避免手写 wrapper 漂移；用类型声明保证属性类型提示同步。
- 追问钩子：React 对自定义元素事件的支持有历史坑（onClick vs 自定义事件），wrapper 如何抹平？考察对 React 合成事件与 addEventListener 差异的理解。

```javascript
// 元数据 → React wrapper（简化生成逻辑）
const meta = { tag: 'ds-switch', props: ['checked'], events: ['ds-change'] };
function genReactWrapper(m) {
  const props = m.props.join(', ');
  return `
export function ${m.tag.replace(/^ds-/, '').replace(/-/g, '')}({ ${props}, ...rest }) {
  const ref = React.useRef(null);
  React.useEffect(() => {
    const el = ref.current;
    ${m.events.map(e => `el.addEventListener('${e}', e => rest['on${e}']?.(e));`).join('\n    ')}
  }, []);
  return React.createElement('${m.tag}', { ref, ${props}, ...rest });
}`;
}
console.log(genReactWrapper(meta));
```
