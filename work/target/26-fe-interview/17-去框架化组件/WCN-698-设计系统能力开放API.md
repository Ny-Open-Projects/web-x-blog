---
title: [WCN-698] 笔试：实现设计系统平台的能力开放 API（插件机制：注册/查询/权限校验/沙箱执行）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-698：笔试：实现设计系统平台的能力开放 API（插件机制：注册/查询/权限校验/沙箱执行）

**答**：
- 需求：实现 PluginHub：register(plugin) 校验插件契约（id/name/activate）；list() 返回插件元信息；run(id, ctx) 在受限上下文执行插件并做权限校验；未知 id 或权限不足抛错。
- 思路：Map 存插件；契约校验必填字段；权限用 capabilities 数组校验；执行用 try/catch + 冻结 ctx 防止篡改。
- 边界：重复 id 覆盖需告警；插件抛错不影响 Hub；ctx 只读（Object.freeze）。

```javascript
export class PluginHub {
  constructor() { this.plugins = new Map(); }
  register(plugin) {
    const missing = ['id', 'name', 'activate'].filter(k => !plugin[k]);
    if (missing.length) throw new Error(`插件契约缺失: ${missing.join(',')}`);
    if (this.plugins.has(plugin.id)) console.warn('覆盖已有插件', plugin.id);
    this.plugins.set(plugin.id, plugin);
  }
  list() {
    return [...this.plugins.values()].map(({ id, name, capabilities }) =>
      ({ id, name, capabilities }));
  }
  run(id, ctx, required = []) {
    const p = this.plugins.get(id);
    if (!p) throw new Error(`未知插件 ${id}`);
    const caps = p.capabilities || [];
    if (!required.every(c => caps.includes(c)))
      throw new Error(`权限不足: 需要 ${required.join(',')}`);
    try { return p.activate(Object.freeze({ ...ctx })); }
    catch (e) { console.error('[plugin] 执行失败', id, e); return null; }
  }
}
const hub = new PluginHub();
hub.register({ id: 'export', name: '导出', capabilities: ['read'],
  activate: (ctx) => ctx.data });
console.log(hub.list());
```

**评分点**：
- 插件契约校验（id/name/activate 必填）。
- 权限 capabilities 校验，required 未满足抛错。
- ctx 冻结（Object.freeze）防止插件篡改宿主上下文。
- 插件执行 try/catch 隔离，单插件失败不影响 Hub。

## 变体与延伸（补充）

**变体与延伸**：

1. `Object.freeze({ ...ctx })` 只是浅冻结，插件改嵌套对象还拦得住吗 → 拦不住，要深冻结或传 Proxy 只读视图，并说明深冻结大对象的性能代价。
2. 插件是异步的（`activate` 返回 Promise），同步 `try/catch` 还兜得住吗 → 兜不住，rejected promise 逃出同步栈，必须 `await` 包一层并处理 rejection。
3. `required` 由调用方传入，调用方传空数组不就绕过权限了 → 权限应由 Hub 按 action 映射表决定，调用方只声明意图（`run('export', ctx)`），不自己声明所需能力。
