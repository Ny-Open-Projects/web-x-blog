---
title: [VIZ-037] ECharts 内存泄漏如何排查与根治？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-037：ECharts 内存泄漏如何排查与根治？
**答**：泄漏三大来源：① 切换页面/组件卸载时**没 dispose**，实例与 detached DOM 一起挂在内存；② resize 监听/定时器/ZRender 事件没清理；③ 全局变量、Map 缓存长期持有 chart 引用。排查方法：Chrome DevTools Performance Monitor 看 JS Heap 与 DOM Nodes 是否随操作单调上涨；Heap Snapshot 对比两次快照，搜 `ECharts` / `ECInstance` / detached 节点。根治：图表生命周期与框架生命周期强绑定，mount 建实例、unmount 必 dispose。

```javascript
// React 中防泄漏三件套：dispose 图表、移除 resize 监听、清理定时器
function useChart(elRef, option) {
  const chartRef = useRef(null);
  useEffect(() => {
    const chart = echarts.init(elRef.current);
    chartRef.current = chart;
    const onResize = () => chart.resize();
    window.addEventListener('resize', onResize);
    return () => {                       // 卸载必须清理，否则 SPA 路由切换累积实例
      window.removeEventListener('resize', onResize);
      chart.dispose();
      chartRef.current = null;
    };
  }, []);
  useEffect(() => {
    chartRef.current?.setOption(option);
  }, [option]);
  return chartRef;
}
// 排查：Performance Monitor 看 JS Heap / DOM Nodes；Heap Snapshot 对比搜 ECharts 实例
```

---

## 六、D3 思想（VIZ-038 ~ VIZ-044）
