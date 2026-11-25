---
title: [WCN-642] 笔试：实现 signal 持久化中间件（节流写 + 版本迁移 + 多标签同步 + 命名空间）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-642：笔试：实现 signal 持久化中间件（节流写 + 版本迁移 + 多标签同步 + 命名空间）

**答**：
- 需求：实现 createPersistent(sig, {key, version, migrate, throttle})：启动时读取并按 version 迁移；变更节流写；storage 事件同步；key 带命名空间防冲突。
- 思路：读写包裹 try/catch；迁移函数链按版本升级；节流用时间戳；命名空间前缀拼接 key。
- 边界：JSON 解析失败回退默认值；storage 事件只响应同 key；写失败静默；dispose 清定时器与监听。

```javascript
export function createPersistent(sig, opts) {
  const { key, version = 1, migrate = x => x, throttle = 300, ns = 'ds' } = opts;
  const fullKey = `${ns}:${key}`;
  let timer = null, lastWrite = 0;
  try {
    const raw = JSON.parse(localStorage.getItem(fullKey) || 'null');
    if (raw) sig.set(migrate(raw.data, raw.version ?? 0));
  } catch {}
  const off = effect(() => {
    const value = sig.get(), now = Date.now();
    clearTimeout(timer);
    timer = setTimeout(() => {
      if (now - lastWrite < throttle) return;
      lastWrite = now;
      try { localStorage.setItem(fullKey, JSON.stringify({ v: version, data: value })); }
      catch {}
    }, throttle);
  });
  const onStorage = e => {
    if (e.key !== fullKey) return;
    try { sig.set(migrate(JSON.parse(e.newValue).data, JSON.parse(e.newValue).v)); }
    catch {}
  };
  window.addEventListener('storage', onStorage);
  return () => { off(); clearTimeout(timer); window.removeEventListener('storage', onStorage); };
}
```

**评分点**：
- 按 version 执行迁移函数，兼容旧数据（向前兼容）。
- 节流写入，且时间戳去重，避免频繁写 localStorage。
- storage 事件只处理同命名空间同 key 的变化。
- 返回 dispose 清理定时器与监听（可测试、无泄漏）。
