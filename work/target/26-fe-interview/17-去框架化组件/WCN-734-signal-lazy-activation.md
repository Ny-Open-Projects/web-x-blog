---
title: [WCN-734] 信号依赖图很大时，如何做按需惰性激活支撑超大应用？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-734：信号依赖图很大时，如何做按需惰性激活支撑超大应用？

**答**：
- 结论：signal 的订阅默认不立即求值，改用「脏标记 + 惰性拉取」：依赖变化时只标记 dirty，真正读取 computed 时才向上重算，跳过未被消费的分支。
- 结合引用计数：无订阅者的子树不参与传播；用「惰性订阅」让只有在视图真正挂载时才 subscribe，卸载即退订。
- 追问钩子：惰性计算下如何保证 effect 不被漏通知？考察「effect 主动拉取 + dirty 传播」的闭环。

```javascript
function computed(fn) {
  let value, dirty = true, subs = new Set();
  const c = {
    get value() {
      if (dirty) { value = fn(); dirty = false; }     // 读取时才重算
      return value;
    },
    subscribe(s) { subs.add(s); },
    markDirty() {
      if (dirty) return;
      dirty = true;
      subs.forEach((s) => s.markDirty?.());          // 向上传播脏标记
    },
  };
  return c;
}
const a = { value: 1, subs: new Set() };
const doubled = computed(() => a.value * 2);
console.log(doubled.value);   // 读取触发计算
```
