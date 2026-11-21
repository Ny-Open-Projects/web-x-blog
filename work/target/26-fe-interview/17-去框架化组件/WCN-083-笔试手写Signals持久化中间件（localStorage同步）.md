---
title: [WCN-083] 笔试：手写 Signals 持久化中间件（localStorage 双向同步）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-083：笔试：手写 Signals 持久化中间件

**题目**：实现 `persist(signal, key, opts)`：① 初始化时从 localStorage 读取（解析失败/缺失用默认值）；② signal 变化写回 storage（JSON 序列化）；③ 监听 `storage` 事件实现多标签页同步（跳过自己写入的 key）；④ 可配 `serialize/deserialize`；⑤ 返回 `{ stop, flush }`。

**答**：

```javascript
export function persist(sig, key, {
  storage = localStorage, serialize = JSON.stringify, deserialize = JSON.parse,
} = {}) {
  const tag = `${key}@${Math.random().toString(36).slice(2)}`; // 标识自己写入

  // 1) 初始化：storage → signal
  try {
    const raw = storage.getItem(key);
    if (raw !== null) sig(deserialize(raw));
  } catch (e) { console.warn('persist parse fail', key, e); }

  // 2) signal → storage（节流写避免高频）
  let timer, pendingValue;
  const write = () => {
    try {
      pendingValue.__src = tag;
      storage.setItem(key, serialize(pendingValue));
    } catch { /* 配额溢出静默 */ }
  };
  const stop = effect(() => {
    const v = sig();
    pendingValue = v;
    clearTimeout(timer);
    timer = setTimeout(write, 300);   // 简单节流
  });

  // 3) 多标签页同步：storage 事件（其他标签页触发）
  const onStorage = (e) => {
    if (e.key !== key || e.newValue === null) return;
    const val = deserialize(e.newValue);
    if (val?.__src === tag) return;   // 自己的写入跳过
    untrack(() => sig(val));          // 读取方更新不建立依赖
  };
  window.addEventListener('storage', onStorage);

  return {
    flush() { clearTimeout(timer); pendingValue = sig(); write(); },
    stop() { stop(); window.removeEventListener('storage', onStorage); },
  };
}
```

**评分点**：
- 初始化方向：storage → signal 先执行（读取优先于写回，避免覆盖）。
- storage 事件只在"其他标签页"触发，`__src` 标识防回环。
- 反序列化 try/catch 降级；quota 溢出不抛。
- 写入节流 + flush 强制落盘（页面关闭前场景）；stop 双清理。
