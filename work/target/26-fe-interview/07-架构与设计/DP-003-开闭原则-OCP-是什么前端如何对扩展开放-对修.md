---
title: [DP-003] 开闭原则 OCP 是什么？前端如何"对扩展开放、对修改关闭"？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-003：开闭原则 OCP 是什么？前端如何"对扩展开放、对修改关闭"？
**答**：
- OCP：新增能力时应新增代码，而不是修改已有代码——核心是"找到变化点并把它参数化/多态化"。
- 前端实例：报表导出新增一种格式，不应去改 `export` 函数的 if-else，而是注册一个新 exporter。
- OCP 是几乎所有模式的目的：策略模式封装算法族、工厂封装创建逻辑、插件机制封装扩展点。
- 面试提示：OCP 不等于无限抽象，只有"确实会变化"的方向才值得开放扩展点。

```javascript
// 反例：每加一种格式都要改 exportFile 的 switch，风险随格式数线性增长
function exportFile(data, type) {
  if (type === 'json') return JSON.stringify(data);
  else if (type === 'csv') return data.map(Object.values).join('\n');
  // else if (type === 'excel') ... 无限膨胀
}

// 正例：注册表 + 统一接口，新增格式 = 新增一行注册，老代码零修改（OCP）
const exporters = {
  json: (data) => JSON.stringify(data),
  csv: (data) => data.map((row) => Object.values(row).join(',')).join('\n'),
};
function registerExporter(type, fn) {
  exporters[type] = fn; // 扩展点：对扩展开放
}
function exportFile(data, type) {
  const fn = exporters[type];
  if (!fn) throw new Error(`不支持的格式 ${type}`);
  return fn(data); // 不再感知具体格式，对修改关闭
}
registerExporter('tsv', (data) => data.map((r) => Object.values(r).join('\t')).join('\n'));
console.log(exportFile([{ a: 1, b: 2 }], 'tsv')); // a\tb\n1\t2
```
