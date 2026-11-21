---
title: [R19-173] React 如何封装命令式 Canvas 库？通用的集成模式是什么？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-173：React 如何封装命令式 Canvas 库？通用的集成模式是什么？
**答**：
- 命令式库（Canvas/SVG 渲染器、编辑器）与声明式 React 的桥接模板：**挂载期初始化实例**（useEffect 建立一次）-> **声明式 props 增量同步**（effect 里对比 props 调用实例 API）-> **事件上抛**（实例回调转 React props）-> **卸载销毁**（cleanup 调 destroy）。
- ref 暴露实例方法：对外提供 `canvasRef.current.exportPNG()` 之类的命令式出口，双向都能用。
- props 同步要用 ref 保存最新值，避免 effect 依赖抖动；重建实例（尺寸变化）与增量更新（数据变化）分开处理。
- 一切以"实例生命周期 > 组件生命周期"管理，绝不每次渲染 new 一个实例。

```tsx
// ChartCanvas.tsx —— Canvas 图表库的 React 包装模板
import { useEffect, useRef, useImperativeHandle, forwardRef, useState } from 'react';

// 假设的原生 Canvas 图表库（命令式 API）
// new CanvasChart(el, options) -> instance.update(data) / resize(w, h) / destroy()

type Props = {
  data: number[];
  width: number;
  height: number;
  onPointClick?: (index: number) => void;
};

export type ChartHandle = { exportPNG: () => string | null };

export const ChartCanvas = forwardRef<ChartHandle, Props>(function ChartCanvas(
  { data, width, height, onPointClick },
  ref,
) {
  const containerRef = useRef<HTMLDivElement>(null);
  // 实例存在 ref 里，不进 state：改实例不触发渲染
  const chartRef = useRef<any>(null);
  const onPointClickRef = useRef(onPointClick);
  onPointClickRef.current = onPointClick; // 最新回调进 ref，effect 依赖保持干净

  // 1. 挂载期初始化一次（依赖为空数组）
  useEffect(() => {
    chartRef.current = new (window as any).CanvasChart(containerRef.current, {
      width, height,
      onClick: (index: number) => onPointClickRef.current?.(index), // 3. 实例事件 -> React props
    });
    return () => {
      chartRef.current.destroy(); // 4. 卸载销毁，防泄漏
      chartRef.current = null;
    };
  }, []); // 注意：width/height 变化走"重建"分支，见下

  // 2a. 数据变化 -> 增量 update，不重建实例
  const dataRef = useRef(data);
  useEffect(() => {
    dataRef.current = data;
    chartRef.current?.update(data);
  }, [data]);

  // 2b. 尺寸变化 -> 需要重建（依赖 width/height）
  useEffect(() => {
    chartRef.current?.resize?.(width, height);
  }, [width, height]);

  // 命令式出口：父组件可 ref.current.exportPNG()
  useImperativeHandle(ref, () => ({
    exportPNG: () => chartRef.current?.exportPNG() ?? null,
  }));

  return <div ref={containerRef} style={{ width, height }} />;
});

// 使用侧
function Demo() {
  const chartRef = useRef<ChartHandle>(null);
  const [data, setData] = useState([1, 2, 3]);
  return (
    <>
      <ChartCanvas ref={chartRef} data={data} width={400} height={200}
        onPointClick={i => console.log('clicked', i)} />
      <button onClick={() => setData(d => [...d, d.length + 1])}>加一个点</button>
      <button onClick={() => console.log(chartRef.current?.exportPNG())}>导出</button>
    </>
  );
}
```
