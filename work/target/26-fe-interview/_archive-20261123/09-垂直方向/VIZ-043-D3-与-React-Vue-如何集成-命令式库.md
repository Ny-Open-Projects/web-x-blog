---
title: [VIZ-043] D3 与 React/Vue 如何集成？（命令式库的响应式包装）
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-043：D3 与 React/Vue 如何集成？（命令式库的响应式包装）
**答**：核心模式：**ref 拿容器 + effect 承载命令式生命周期 + 数据作为响应式依赖**。React 中在 useEffect 里执行 D3 逻辑，`[data]` 变化触发重跑，return 清理函数处理监听与节点；Vue 用 onMounted/onBeforeUnmount 同理。三条铁律：不在 render/模板期间直接操作 DOM；effect 要幂等（StrictMode 会双调用）；数据 join 配 key，尽量增量更新而非全量重建。复杂场景把"数据计算"交给 D3、"视图 diff"交给框架也是合法分工。

```jsx
// 命令式库接入响应式框架：ref + useEffect 桥接 + 数据作依赖
function BarChart({ data }) {
  const ref = useRef(null);
  useEffect(() => {
    const svg = d3.select(ref.current);
    svg.selectAll('*').remove(); // 幂等：StrictMode 双调用也安全
    const x = d3.scaleLinear([0, d3.max(data, d => d.value)], [0, 480]);
    svg.selectAll('rect').data(data, d => d.id).join('rect')
      .attr('width', d => x(d.value))
      .attr('height', 20)
      .attr('y', (_, i) => i * 24);
  }, [data]); // data 变化 -> effect 重跑 -> D3 重绘
  return <svg ref={ref} width="500" height={data.length * 24} />;
}
// 严禁在 render 期间执行 D3 副作用；清理逻辑放 effect 的 return 中
```
