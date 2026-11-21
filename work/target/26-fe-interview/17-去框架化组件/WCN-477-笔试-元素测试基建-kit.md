---
title: [WCN-477] 笔试：实现元素测试 kit（fixture/事件断言/属性等待）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-477：笔试：实现元素测试 kit（fixture/事件断言/属性等待）。
**题目**：`createFixture(tag, props)`：创建并挂载元素（props 设置 property），返回 `{el, cleanup}`；`waitForProp(el, name, match)` 轮询 property（超时失败）；`oneEvent(el, name)` Promise 化事件断言。

```javascript
async function createFixture(tag, props = {}) {
  if (!customElements.get(tag)) throw new Error(`未注册: ${tag}`);
  const el = document.createElement(tag);
  for (const [k, v] of Object.entries(props)) el[k] = v;   // property 注入
  document.body.append(el);
  await customElements.whenDefined(tag);
  return { el, cleanup: () => el.remove() };
}
async function waitForProp(el, name, match, { timeout = 2000 } = {}) {
  const t0 = Date.now();
  while (Date.now() - t0 < timeout) {
    if (match(el[name])) return el[name];
    await new Promise(r => setTimeout(r, 50));
  }
  throw new Error(`waitForProp 超时：${name}=${JSON.stringify(el[name])}`);
}

```

**评分点**：
- fixture：自动挂载 + cleanup（移除+dispose）。
- waitForProp：轮询 + 超时错误（含当前值）。
- oneEvent：超时失败（事件丢失可诊断）。
- kit 无框架依赖（纯 DOM）。
