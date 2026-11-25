---
title: [TST-928] 主应用与子应用的「生命周期契约」（bootstrap/mount/unmount）怎么测试？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-928：主应用与子应用的「生命周期契约」（bootstrap/mount/unmount）怎么测试？
**答**：
- 结论：生命周期是微前端最容易被忽略的契约——要验证「按序调用、幂等、卸载不留痕」，否则切应用多次后内存泄漏和事件重复绑定。
- 要点：bootstrap 只一次；mount 可多次且每次重建 DOM 与事件；unmount 必须解绑事件、清定时器、还原全局副作用。
- 测法：用 spy 记录调用顺序；连续 mount/unmount 10 次后断言 window 上无残留监听、DOM 节点数归零。
- 追问钩子：用户在大促页和购物车之间切了 20 次，页面越来越卡，生命周期契约测试怎么提前发现？

```javascript
test('子应用生命周期契约', async () => {
  const calls = [];
  const app = {
    bootstrap: async () => calls.push('bootstrap'),
    mount: async (p) => { calls.push('mount'); p.container.innerHTML = '<div id="sub"></div>'; },
    unmount: async (p) => { calls.push('unmount'); p.container.innerHTML = ''; },
  };
  const props = { container: document.createElement('div') };
  await app.bootstrap(props);
  for (let i = 0; i < 10; i++) { await app.mount(props); await app.unmount(props); }
  expect(calls[0]).toBe('bootstrap');
  expect(calls.filter(c => c === 'bootstrap')).toHaveLength(1);
  expect(props.container.childElementCount).toBe(0); // 卸载不留痕
});
```
