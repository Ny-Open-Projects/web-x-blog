---
title: [AGT-116] 长任务 Agent 的进度如何可视化（步骤树 / 实时日志流）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-116：长任务 Agent 的进度如何可视化（步骤树 / 实时日志流）？
**答**：
- 长任务 UX 三件套：步骤树（计划与依赖可视化、当前步骤高亮）、实时日志流（SSE 推送执行细节）、可中断可恢复。
- 数据源统一：服务端任务状态机每次变更发布事件（与 AGT-065 持久化状态同源），前端刷新页面后进度仍完整。
- 推送通道复用流式基建（SSE/WS），事件结构 {taskId, stepId, status, output}，按依赖关系渲染树。
- 日志分级：关键节点常显，工具原始输出折叠；失败步骤标红并支持单步重试。

```typescript
import { z } from 'zod';

// 服务端：步骤事件推送（SSE）
type StepStatus = 'pending' | 'running' | 'done' | 'failed';
interface StepEvent { taskId: string; stepId: string; status: StepStatus; output?: string }

export function streamTaskProgress(req: any, res: any) {
  const { taskId } = req.params;
  res.setHeader('Content-Type', 'text/event-stream');
  const send = (ev: StepEvent) => res.write(`data: ${JSON.stringify(ev)}\n\n`);
  const snapshot = taskStore.getSteps(taskId);              // 先补发当前快照，防刷新丢进度
  Object.values(snapshot).forEach(send);
  taskBus.on(taskId, send);                                 // 状态机每次变更发布事件（与持久化同源）
  req.on('close', () => taskBus.off(taskId, send));
}

// 前端：步骤树渲染（React）
function TaskTree({ taskId }: { taskId: string }) {
  const [steps, setSteps] = useState<Record<string, StepStatus>>({});
  const [logs, setLogs] = useState<string[]>([]);
  useEffect(() => {
    const es = new EventSource(`/api/tasks/${taskId}/progress`);
    es.onmessage = (e) => {
      const ev: StepEvent = JSON.parse(e.data);
      setSteps((s) => ({ ...s, [ev.stepId]: ev.status }));
      if (ev.output) setLogs((l) => [...l.slice(-200), `[${ev.stepId}] ${ev.output}`]);
    };
    return () => es.close();
  }, [taskId]);
  return (
    <div>
      <StepTreeGraph statuses={steps} />  {/* 依赖图渲染，当前步骤高亮 */}
      <details><summary>执行日志</summary><pre>{logs.join('\n')}</pre></details>
    </div>
  );
}
```
