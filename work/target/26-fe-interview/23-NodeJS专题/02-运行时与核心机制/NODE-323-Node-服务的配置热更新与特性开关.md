---
title: [NODE-323] Node 服务的配置热更新与特性开关？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-323：Node 服务的配置热更新与特性开关？
**答**:
- 配置热更链路：配置中心长轮询（NODE-150 客户端 NODE-349）→ 变更回调 → schema 校验（zod）→ 热替换运行时配置对象 → 各模块订阅生效。
- 特性开关服务端版：flag 求值（用户属性/百分比）在请求入口一次完成，放 ALS（NODE-292）供深层使用。
- 安全边界：热更配置失败必须回滚到 last-good（NODE-349 快照）——配置错误不能打挂服务。
- 与灰度联动：配置本身灰度发布（NODE-150）。

```javascript
// 配置热更管理器
class ConfigService {
  #cfg = loadDefaults();
  onRemoteChange(newCfg) {
    const parsed = schema.safeParse(newCfg);
    if (!parsed.success) return alarm('config-invalid', parsed.error);   // 校验失败：保持旧值
    const prev = this.#cfg;
    this.#cfg = parsed.data;
    emitter.emit('config-changed', { prev, next: this.#cfg });
  }
  get() { return als.getStore()?.cfg ?? this.#cfg; }   // 请求级快照（一致性）
}
// flag 求值（请求入口一次）
app.use((ctx, next) => als.run({ flags: flagsEngine.evalAll(ctx.state.user) }, next));
// 深层：const { flags } = als.getStore(); flags['new-checkout'] ? newFlow() : oldFlow();
```
