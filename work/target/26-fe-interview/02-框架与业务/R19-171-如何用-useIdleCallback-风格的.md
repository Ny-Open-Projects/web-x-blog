---
title: [R19-171] 如何用 useIdleCallback 风格的 hook 把长任务切成空闲切片？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-171：如何用 useIdleCallback 风格的 hook 把长任务切成空闲切片？
**答**：
- 问题：一次同步处理 1 万条数据（解析、建索引）阻塞主线程，输入全卡。
- 方案：`requestIdleCallback`（或 setTimeout 兜底）按 deadline 取片，每片处理一批后让出主线程；React 侧配合 setState 分批追加渲染。
- 关键点：deadline.timeRemaining() 判断还能不能干、 cancellable（组件卸载停止）、进度可控（百分比展示）。
- 更现代的替代：Web Worker（不占主线程）适合纯计算；切片法适合"需要渐进渲染到 DOM"的场景。

```tsx
// use-idle-chunks.ts —— 长任务空闲切片 hook
import { useEffect, useRef, useState, useCallback } from 'react';

const rIC: typeof requestIdleCallback =
  (window as any).requestIdleCallback ?? ((cb: any) => setTimeout(() => cb({ timeRemaining: () => 12, didTimeout: false }), 1));
const cIC: typeof cancelIdleCallback =
  (window as any).cancelIdleCallback ?? clearTimeout;

export function useIdleChunks<TIn, TOut>(
  items: TIn[],
  process: (batch: TIn[]) => TOut[],
  batchSize = 200,
) {
  const [results, setResults] = useState<TOut[]>([]);
  const [progress, setProgress] = useState(0);
  const [running, setRunning] = useState(false);
  const cancelRef = useRef<number | null>(null);
  const cursorRef = useRef(0);

  const start = useCallback(() => {
    cursorRef.current = 0;
    setResults([]);
    setProgress(0);
    setRunning(true);

    const step = (deadline: IdleDeadline) => {
      // 每片处理 batchSize 条，或直到 deadline 耗尽
      const startIdx = cursorRef.current;
      const batch = items.slice(startIdx, startIdx + batchSize);
      if (batch.length === 0) {
        setRunning(false);
        return;
      }
      cursorRef.current = startIdx + batch.length;
      setResults(prev => [...prev, ...process(batch)]); // 渐进渲染，不是一口气
      setProgress(Math.round((cursorRef.current / items.length) * 100));

      if (cursorRef.current < items.length) {
        cancelRef.current = rIC(step) as unknown as number; // 下一片等空闲
      } else {
        setRunning(false);
      }
      // 提示：deadline.timeRemaining() < 5 时应立即让出，本例按批次粗粒度控制
    };
    cancelRef.current = rIC(step) as unknown as number;
  }, [items, process, batchSize]);

  const cancel = useCallback(() => {
    if (cancelRef.current !== null) cIC(cancelRef.current);
    setRunning(false);
  }, []);

  useEffect(() => cancel, [cancel]); // 卸载即停止

  return { results, progress, running, start, cancel };
}

// 使用：一万条日志渐进建索引
function LogIndexer({ logs }: { logs: string[] }) {
  const { results, progress, running, start } = useIdleChunks(
    logs,
    batch => batch.map(l => ({ raw: l, tokens: l.split(' ') })),
  );
  return (
    <div>
      <button onClick={start} disabled={running}>
        {running ? `处理中 ${progress}%` : '开始解析'}
      </button>
      <ul>{results.map((r, i) => <li key={i}>{r.raw}</li>)}</ul>
    </div>
  );
}
```
