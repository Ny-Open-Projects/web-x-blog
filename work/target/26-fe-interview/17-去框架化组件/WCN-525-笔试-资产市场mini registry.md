---
title: [WCN-525] 元素资产市场的「依赖解析 + 按需打包 + 版本锁定」如何实现？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-525：元素资产市场的「依赖解析 + 按需打包 + 版本锁定」如何实现？

**答**：
- 结论：registry 维护元素依赖图，按入口元素解析传递依赖，生成锁定版本的打包清单。
- 依赖解析：DFS 遍历 deps，检测循环依赖并报错；同名多依赖取满足所有区间的版本。
- 版本锁定：输出 lock 文件（tag → 精确版本 + URL），保证构建可复现。
- 追问：如何处理 peer 依赖由宿主提供而非打包？（答：标记 external，不进入打包清单）

```javascript
function resolveDeps(entries, catalog) {
  const out = new Map(), visiting = new Set();
  function visit(name, range) {
    if (visiting.has(name)) throw new Error('循环依赖: ' + name);
    if (out.has(name)) return;
    const meta = catalog[name]; if (!meta) throw new Error('未找到: ' + name);
    if (meta.external) return;                    // peer 由宿主提供
    visiting.add(name);
    (meta.deps || []).forEach(d => visit(d.name, d.range));
    visiting.delete(name);
    out.set(name, pickVersion(meta.versions, range));
  }
  entries.forEach(e => visit(e.name, e.range));
  return Object.fromEntries(out);                 // lock 文件
}
function pickVersion(versions, range) { return versions.filter(v => v.startsWith(range.replace('^',''))).pop(); }
```
