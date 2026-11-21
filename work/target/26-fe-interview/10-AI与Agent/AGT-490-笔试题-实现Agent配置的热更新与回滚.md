---
title: [AGT-490] 笔试题——实现配置热更新（版本化+灰度生效+校验拦截+回滚）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-490：手写配置热更新：schema 校验、灰度生效、运行时订阅、秒级回滚

**需求与边界**：
- 输入：配置变更（含 schema）、灰度比例；输出：配置管理服务。
- 边界要求：① 变更 schema 校验（非法配置拒绝入库）；② 配置版本化（当前/上一版本指针）；③ 灰度生效（按用户 hash 分流新旧）；④ 运行时订阅推送（热更新不重启）；⑤ 回滚=指针切回上一版本。

**答**：
```javascript
class ConfigManager {
  constructor({ schema, store, bus }) {
    this.schema = schema; this.store = store;
    this.bus = bus;                            // 运行时订阅
  }
  async update(cfg, { rollout = 1.0, userId }) {
    // 1. schema 校验（拒绝非法配置）
    const check = this.schema.safeParse(cfg);
    if (!check.success)
      return { accepted: false, error: check.error.message };
    // 2. 版本化：保存新版本，指针按灰度切换
    const ver = await this.store.save(cfg);    // {id, data, ts}
    const bucket = hash(userId ?? 'global') % 100 / 100;
    const useNew = bucket < rollout;
    const active = useNew ? ver : await this.store.current();
    // 3. 运行时推送（订阅方热更新）
    this.bus.publish('config', { version: active.id,
      data: active.data, ts: active.ts });
    await this.store.setPointer(active.id);
    return { accepted: true, version: active.id,
      rollout, prev: await this.store.previous() };
  }
  subscribe(fn) {                              // 服务方热更新
    return this.bus.subscribe('config', ({ data }) => fn(data));
  }
  async rollback() {                           // 秒级回滚
    const prev = await this.store.previous();
    await this.store.setPointer(prev.id);
    this.bus.publish('config', { version: prev.id, data: prev.data });
    return { rolledBackTo: prev.id };
  }
  async get(userId) {                          // 读取：按灰度分流
    const bucket = hash(userId) % 100 / 100;
    const v = bucket < (await this.store.rollout())
      ? await this.store.current() : await this.store.previous();
    return v.data;
  }
}
// 订阅方：模型路由/prompt 资产/护栏阈值全部热更新；
// 指针切换=回滚，不重部署。
```

**评分点**:
- schema 校验前置（非法配置不入库不生效）。
- 版本指针+灰度分流（rollout 按用户 hash），读取时按桶取版本。
- bus 发布订阅实现运行时热更新（不重启）。
- 回滚=指针切回上一版本，秒级生效。
