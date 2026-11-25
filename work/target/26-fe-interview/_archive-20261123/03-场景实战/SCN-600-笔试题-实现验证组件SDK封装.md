---
title: [SCN-600] 笔试题——实现验证组件 SDK 封装（Promise 化 + 场景配置 + 生命周期）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-600：手写验证组件 SDK 封装

**需求与边界**：
- 需求：对外暴露 `RiskSDK.verify(scene)` 返回 Promise；内部处理配置拉取、验证器挂载/卸载、埋点、错误兜底；支持重复调用排队。
- 边界：① 同一时刻只允许一个验证实例（后续调用排队或拒绝，可配置）；② unmount 后 pending Promise 以特定错误 reject；③ 埋点全程包裹。

**答**：
```javascript
const RiskSDK = (() => {
  let mounted = null, config = null, disposed = false;
  const queue = [];
  async function ensureConfig() {
    if (!config) {
      try { config = await api.get('/risk/config'); }
      catch { config = DEFAULT_CONFIG; }            // 配置失败用默认（可用性优先）
    }
    return config;
  }
  function verify(scene, { queue: allowQueue = false } = {}) {
    return track(scene, async () => {
      if (disposed) throw Object.assign(new Error('SDK_DISPOSED'), { code: 'DISPOSED' });
      if (mounted) {
        if (!allowQueue) throw Object.assign(new Error('BUSY'), { code: 'BUSY' });
        await new Promise(res => queue.push(res));  // 排队等前一个完成
      }
      const cfg = (await ensureConfig())[scene];
      const impl = registry.get(cfg.verifier);
      mounted = { scene };
      try {
        const r = await impl.run({ ...cfg, scene });
        return { pass: r.pass, token: r.token };
      } finally {
        mounted = null;
        queue.shift()?.();                          // 唤醒排队调用
      }
    });
  }
  function track(scene, fn) {                       // 埋点包裹
    const t0 = performance.now();
    return fn().then(
      (r) => { reporter.push({ scene, pass: r.pass, cost: performance.now() - t0 }); return r; },
      (e) => { reporter.push({ scene, error: e.code, cost: performance.now() - t0 }); throw e; },
    );
  }
  function dispose() {                              // 页面卸载清理
    disposed = true;
    queue.forEach(res => res());                    // 唤醒排队让它们 reject
  }
  return { verify, dispose };
})();
```

**评分点**:
- Promise 化 API + 埋点全包裹（成功/失败均记录耗时）。
- 并发控制：BUSY 拒绝或排队两种模式。
- dispose 后 pending Promise 以 DISPOSED reject（不悬挂）。
- 配置拉取失败回退默认配置（可用性优先）。
