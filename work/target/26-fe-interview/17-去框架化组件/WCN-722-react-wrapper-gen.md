---
title: [WCN-722] 笔试：手写从组件元数据生成 React wrapper 的代码生成器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-722：笔试：手写从组件元数据生成 React wrapper 的代码生成器

**答**：
- 需求：输入 `{ tag, props: string[], events: string[] }`，输出一个 React 函数组件源码字符串：把 props 以属性传给自定义元素，并在 useEffect 里为每个 event 绑定 addEventListener，卸载时解绑。
- 要点：组件名由 tag 转帕斯卡命名；事件名 ds-change → onDsChange；边界：无 props/events 时生成合法代码，字符串转义。

```javascript
function pascal(tag) {
  return tag.split('-').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join('');
}
function toHandler(ev) {                      // ds-change -> onDsChange
  return 'on' + ev.split('-').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join('');
}
function genWrapper(meta) {
  const name = pascal(meta.tag);
  const props = meta.props || [], events = meta.events || [];
  const destruct = props.length ? `{ ${props.join(', ')}, ...rest }` : '{ ...rest }';
  const listeners = events.map((ev) =>
    `el.addEventListener('${ev}', (e) => rest[${JSON.stringify(toHandler(ev))}]?.(e));`).join('\n    ');
  const cleanups = events.map((ev) =>
    `el.removeEventListener('${ev}', rest[${JSON.stringify(toHandler(ev))}]);`).join('\n      ');
  return `function ${name}(${destruct}) {
  const ref = React.useRef(null);
  React.useEffect(() => {
    const el = ref.current;
    ${listeners}
    return () => { ${cleanups} };
  }, []);
  return React.createElement('${meta.tag}', { ref, ${props.join(', ')}, ...rest });
}`;
}
console.log(genWrapper({ tag: 'ds-switch', props: ['checked'], events: ['ds-change'] }));
```

**评分点**：
- tag→帕斯卡、事件名→onXxx 命名转换正确。
- useEffect 中既绑定也在 cleanup 解绑，无事件监听泄漏。
- props 以 property 透传并保留 rest，扩展性好。
- 空 props/events 时仍生成合法可运行代码。
