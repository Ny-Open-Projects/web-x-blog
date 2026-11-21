---
title: [R19-344] 笔试：手写导出任务的进度反馈（SSE + 轮询降级）
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-344：笔试：手写导出任务的进度反馈（SSE + 轮询降级）
**题**：实现：action 触发导出任务返回 taskId；前端 SSE 订阅 /api/task/[id]/progress（EventSource）；SSE 不可用降级轮询；进度 100% 停止订阅并触发下载。

```javascript
'use client'
function ExportButton() {
  const [progress, setProgress] = useState(0)
  async function start() {
    const { taskId } = await exportAction()
    if ('EventSource' in window) {
      const es = new EventSource(`/api/task/${taskId}/progress`)
      es.onmessage = (e) => {
        const { pct, done, url } = JSON.parse(e.data)
        setProgress(pct)
        if (done) { es.close(); window.location.href = url }
      }
      es.onerror = () => { es.close(); pollFallback(taskId) }
    } else pollFallback(taskId)
  }
  async function pollFallback(taskId) {
    const timer = setInterval(async () => {
      const { pct, done, url } = await fetch(`/api/task/${taskId}`).then(r => r.json())
      setProgress(pct)
      if (done) { clearInterval(timer); window.location.href = url }
    }, 2000)
  }
  return <button onClick={start}>{progress ? `导出中 ${progress}%` : '导出报表'}</button>
}
```
**评分点**：
- SSE 优先 + onerror 降级轮询。
- done 后关闭连接（资源清理）。
- 轮询间隔与退出条件（done 清 interval）。
- action 只创建任务，进度走独立通道（长任务不占 action 连接）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-9e855f31-b5de-4ca7-b61e-0faeeff7315f-cwd'; fi
exit "$__zcode_status"
