---
title: [DP-014] 手写简单工厂：按 type 渲染不同组件？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-014：手写简单工厂：按 type 渲染不同组件？
**答**：
- 简单工厂：定义一个工厂函数，根据参数决定创建哪种产品，调用方不感知具体类。
- 前端最常见形态：`renderChart(type)`、`renderFormItem(type)`、消息列表按 `msgType` 渲染不同气泡。
- 本质是一张"类型 → 构造器"的映射表，天然符合 OCP：新增类型只加映射项。
- 注意：类型太多时不要写成巨型 switch，用对象映射或组件注册表。

```javascript
// 图表组件工厂：调用方只说"要什么"，不说"怎么造"
class LineChart { render(data) { return `折线图: ${data.join(',')}`; } }
class BarChart { render(data) { return `柱状图: ${data.join(',')}`; } }
class PieChart { render(data) { return `饼图: ${data.join(',')}`; } }

const chartFactory = {
  line: () => new LineChart(),
  bar: () => new BarChart(),
  pie: () => new PieChart(),
};
function createChart(type) {
  const ctor = chartFactory[type];
  if (!ctor) throw new Error(`未知图表类型 ${type}`);
  return ctor();
}
// 使用
console.log(createChart('line').render([1, 2, 3])); // 折线图: 1,2,3
console.log(createChart('bar').render([4, 5]));     // 柱状图: 4,5

// React 场景：按 type 渲染组件的工厂（消息气泡）
function Message({ msg }) {
  const map = {
    text: (m) => <div className="bubble">{m.content}</div>,
    image: (m) => <img src={m.url} alt="" />,
    system: (m) => <div className="sys">{m.content}</div>,
  };
  const render = map[msg.type] || map.text; // 兜底策略 + 工厂分派
  return render(msg);
}
// <Message msg={{ type: 'image', url: 'a.png' }} /> —— 调用方完全不感知分支
```
