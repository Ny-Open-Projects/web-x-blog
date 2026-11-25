---
title: [VIZ-134] 可视化 DSL 是什么？如何设计图表描述语言？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-134：可视化 DSL 是什么？如何设计图表描述语言？
**答**：DSL 是比 schema 更接近"意图"的描述层：用户写 `line: x=month y=amount | smooth` 这类声明，编译器翻译成图表库配置。设计要点：① **分层**——意图层（图表类型 + 数据角色）→ 编译层（词法/语法解析 → 目标 option）→ 执行层；② **图形语法思想**——借 G2/Vega-Lite 的"数据→变换→标记→通道"四段式，DSL 只暴露高频子集；③ **容错**——非法描述给出可读报错与建议（"字段不存在，可用 amount"）；④ 应用——聊天式 BI（自然语言→DSL→图表）、低代码平台序列化存储。Vega-Lite 是成熟参照。

```javascript
// 极简图表 DSL：解析 -> 编译为 ECharts option
const DSL = `line: x=month y=amount title=月度销售 | smooth`;
function compileDSL(src, datasets) {
  const [head, ...mods] = src.split('|').map(s => s.trim());
  const [type, ...assigns] = head.split(/\s+/);
  const cfg = {};
  assigns.forEach(a => { const [k, v] = a.split('='); cfg[k] = v; });
  const flags = new Set(mods);                         // 布尔开关：smooth 等
  const ds = datasets[cfg.dataset || 'default'];
  if (!ds?.columns?.includes(cfg.x)) throw new Error(`x 字段不存在 ${cfg.x}，可用: ${ds.columns}`); // 可读报错
  if (!ds.columns.includes(cfg.y)) throw new Error(`y 字段不存在 ${cfg.y}`);
  return {
    title: { text: cfg.title || '' },
    xAxis: { type: 'category', data: ds.rows.map(r => r[cfg.x]) },
    yAxis: { type: 'value' },
    series: [{ type, smooth: flags.has('smooth'), data: ds.rows.map(r => r[cfg.y]) }],
  };
}
```
