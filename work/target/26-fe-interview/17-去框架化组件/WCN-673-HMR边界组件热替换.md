---
title: [WCN-673] 笔试：实现 HMR 边界更新器（模块替换 + 状态保留 + 失败回退整页）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-673：笔试：实现 HMR 边界更新器（模块替换 + 状态保留 + 失败回退整页）

**答**：
- 需求：实现 HMRLayer：register(id, module, stateKey) 记录模块与状态快照；update(id, newModule) 用新模块替换并恢复状态；若新模块 export.hmrAccept=false 则返回 'reload' 让调用方整页刷新。
- 思路：Map 存 {module, state}；update 时校验 accept；用状态代理合并新旧 state；调用 newModule.render；失败捕获返回 reload。
- 边界：依赖未注册的 id 报错；状态深拷贝避免污染；连续 update 幂等。

```javascript
export class HMRLayer {
  constructor() { this.modules = new Map(); }
  register(id, mod, state = {}) {
    this.modules.set(id, { mod, state: { ...state } });
  }
  update(id, newMod) {
    const prev = this.modules.get(id);
    if (!prev) throw new Error(`未注册模块 ${id}`);
    if (newMod.hmrAccept === false) return 'reload';
    try {
      const merged = { ...prev.state, ...(newMod.initialState || {}) };
      newMod.render?.(merged);
      this.modules.set(id, { mod: newMod, state: merged });
      return 'updated';
    } catch (e) {
      console.error('[HMR] 更新失败，回退整页', e);
      return 'reload';
    }
  }
}
const hmr = new HMRLayer();
hmr.register('counter', { render: (s) => console.log(s.n) }, { n: 1 });
console.log(hmr.update('counter', { render: (s) => console.log('新', s.n) }));
// updated：状态 n=1 被保留
```

**评分点**：
- 状态快照在替换时保留并合并（浅拷贝隔离）。
- hmrAccept=false 返回 reload 信号（明确回退路径）。
- render 异常被捕获并返回 reload（不静默失败）。
- 未注册模块报错，重复 update 幂等。
