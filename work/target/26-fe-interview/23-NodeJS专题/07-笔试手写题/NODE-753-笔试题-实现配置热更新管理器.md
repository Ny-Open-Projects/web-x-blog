---
title: [NODE-753] 笔试题——实现配置热更新管理器（分类目 + fail-safe）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-753：手写配置热更

**需求与边界**：
- 需求：配置热更管理器（SCN-NODE-663）——① schema 校验（坏配置拒绝——保留旧值）；② 分类目路由（hotReload 回调 / needsRestart 标记）；③ 变更审计（diff 记录——SCN-OPS-219）；④ 灰度生效（按实例百分比——SCN-OPS-228）。
- 边界：① 回调异常隔离（某组件 reload 失败不影响其他——逐个 try）；② 旧值快照（回滚通道——SCN-OPS-228 快照回滚）；③ 配置拉取失败的兜底（保留旧值 + 告警）。

**答**：
```javascript
class HotConfig {
  constructor(schema, components) { this.schema = schema; this.current = null; }
  onPush(newRaw) {                                     // 配置中心推送
    const parsed = this.schema.safeParse(newRaw);
    if (!parsed.success) {                             // fail-safe：坏配置保留旧值
      alert({ type: 'BAD_CONFIG', issues: parsed.error });
      return;
    }
    const old = this.current;
    const diff = diffConfig(old, parsed.data);
    for (const c of this.components.hotReload) {       // 分类目路由（SCN-NODE-663）
      try { c.reload(diff, parsed.data); }             // 逐组件回调
      catch (e) { alert({ type: 'RELOAD_FAIL', comp: c.name, err: e.message }); }   // 隔离
    }
    for (const c of this.components.needsRestart)
      markNeedsRestart(c);                             // 重启类目标记（诚实分类）
    audit({ diff });                                   // 变更审计
    this.snapshotOld(old);                             // 旧值快照（回滚通道）
    this.current = parsed.data;
  }
}
```

**评分点**:
- fail-safe（坏配置保留旧值——SCN-NODE-663 容错）。
- 分类目路由（hotReload/needsRestart 诚实分类——SCN-NODE-663 假热更防御）。
- 回调异常隔离（逐组件 try——单个失败不影响）。
- 审计 + 旧值快照（SCN-OPS-228 回滚通道）。
