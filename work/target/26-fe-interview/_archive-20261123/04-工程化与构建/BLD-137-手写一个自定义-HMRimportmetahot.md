---
title: [BLD-137] 手写一个自定义 HMR：import.meta.hot 边界与 accept 的完整实现。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 笔试题, 18]
type: 笔试题
---

## BLD-137：手写一个自定义 HMR：import.meta.hot 边界与 accept 的完整实现。
**答**：
- HMR 协议三要素：模块声明边界（`import.meta.hot.accept(cb)`）、vite 检测文件变化后**从变更文件沿 importers 反向找 accept 边界**、通过 ws 通知客户端执行回调（fetch 新模块 → 回调内替换）。
- `hot.accept(deps, cb)`（接受依赖更新，自己重渲染）与 `hot.accept(cb)`（接受自身更新）的区别：前者是"父组件作为边界"，后者是"自更新模块"；`hot.dispose` 清理旧副作用，`hot.data` 跨更新存状态（如 keep-alive 的 store）。
- 无边界时逐层冒泡到入口 → full reload；插件可通过 `handleHotUpdate` 自定义更新范围（如 i18n json 只广播 custom event，不刷任何模块）。
- 面试加分：说出 `import.meta.hot` 在 build 期被替换为空对象（死代码消除）——所以随意调用不会进产物。

```javascript
// src/counter.js：自更新模块 + 状态保留（vite HMR API 完整用法）
if (import.meta.hot) {
  import.meta.hot.dispose((data) => {
    document.getElementById('app').innerHTML = '';   // 清理旧副作用
  });
  import.meta.hot.accept((newModule) => {
    // 自身更新：重执行 render（模块级"刷新"而非页面刷新）
    newModule.render(document.getElementById('app'), import.meta.hot.data.count ?? 0);
  });
}
export let count = 0;
export function render(el, initial = 0) {
  count = initial;
  el.innerHTML = `<button>${count}</button>`;
  el.querySelector('button').onclick = () => (count++, el.querySelector('button').textContent = count);
  return count;
}

// src/store.js：hot.data 保留状态（跨 HMR 不丢）
if (import.meta.hot) {
  import.meta.hot.accept((m) => useStore.setState(m.default.getState()));
  import.meta.hot.data.snapshot ??= null;
}

// vite-plugin 侧：自定义 json 热更（插件内）
// handleHotUpdate({ file, server }) {
//   if (!file.endsWith('.lang.json')) return;
//   server.ws.send({ type: 'custom', event: 'lang-update', data: JSON.parse(fs.readFileSync(file)) });
//   return [];  // 返回空数组：不让 vite 继续走默认模块更新（即不触发任何模块失效）
// }
```
