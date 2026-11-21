---
title: [JS-199] 设计一个 SDK 初始化器？异步依赖与超时降级怎么实现？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-199：设计一个 SDK 初始化器？异步依赖与超时降级怎么实现？

**答**：
- 现实问题：SDK 启动依赖多个异步资源（配置中心、授权、设备信息），彼此有依赖关系又不能互相阻塞——需要并行加载 + 依赖等待 + 整体超时。
- 模块声明式：每个模块声明 name / init(deps) / dependsOn / timeout / critical / degrade；initModule 先等依赖就绪再执行自身。
- 超时降级：模块加载失败或超时不阻塞整体，用 degrade 兜底（默认配置/空实现）并上报降级原因；critical 模块失败才整体失败。
- 幂等与并发防护：init 只执行一次返回同一 Promise；模块用 cache + pending 双 Map 防止同模块重复初始化。
- 对外 API：init() 启动、ready() 等全部就绪并返回实例表、get(name) 按需取模块。

```javascript
// 1. SDK 初始化器：并行加载 + 依赖等待 + 超时降级
function createSDK(modules) {
  const cache = new Map();        // 模块名 -> 实例或降级实例
  const pending = new Map();      // 模块名 -> 初始化 Promise，防并发重复 init
  let initPromise = null;

  const withTimeout = (p, ms, label) => Promise.race([
    p,
    new Promise((_, rej) => setTimeout(() => rej(new Error(`${label} 超时 ${ms}ms`)), ms)),
  ]);

  async function initModule(mod) {
    if (cache.has(mod.name)) return cache.get(mod.name);
    if (pending.has(mod.name)) return pending.get(mod.name);
    const p = (async () => {
      // 先等依赖模块就绪（依赖内部会递归初始化，天然拓扑序）
      const deps = {};
      for (const name of mod.dependsOn || []) {
        deps[name] = await initModule(modules.find((m) => m.name === name));
      }
      try {
        const instance = await withTimeout(mod.init(deps), mod.timeout ?? 3000, mod.name);
        cache.set(mod.name, instance);
        return instance;
      } catch (err) {
        if (mod.critical) throw err;                // 关键模块失败：整体失败
        console.warn(`[SDK] ${mod.name} 降级`, err.message);
        const fallback = mod.degrade ? mod.degrade(err) : null;
        cache.set(mod.name, fallback);              // 降级兜底，不阻塞其他模块
        return fallback;
      }
    })();
    pending.set(mod.name, p);
    return p;
  }
  const getModule = (name) => initModule(modules.find((m) => m.name === name));

  function init() {
    if (!initPromise) {
      // 所有模块并行启动，依赖在各自内部等待；一个 critical 失败整体失败
      initPromise = Promise.all(modules.map(getModule))
        .then(() => ({ ok: true }))
        .catch((err) => ({ ok: false, error: err }));
    }
    return initPromise;
  }
  const ready = () => init().then(() => Object.fromEntries(cache));
  return { init, ready, get: getModule };
}

// 2. 模块声明：config 可选降级，auth 关键，reporter 依赖前两者
const sdk = createSDK([
  {
    name: 'config',
    timeout: 2000,
    init: async () => (await fetch('/api/sdk-config')).json(),
    degrade: () => ({ reportUrl: '/default-collect', appKey: 'dev' }), // 超时用默认配置
  },
  {
    name: 'auth',
    critical: true,                                 // 失败则 SDK 整体初始化失败
    dependsOn: ['config'],
    init: async (deps) => ({ token: 'tk-' + btoa(deps.config.appKey) }),
  },
  {
    name: 'reporter',
    dependsOn: ['config', 'auth'],
    init: async (deps) => ({
      send: (e) => navigator.sendBeacon(deps.config.reportUrl, JSON.stringify({ ...e, token: deps.auth.token })),
    }),
  },
]);

sdk.ready().then((mods) => {
  console.log('SDK 就绪', Object.keys(mods));
  mods.reporter.send({ type: 'sdk-ready' });
});
```
