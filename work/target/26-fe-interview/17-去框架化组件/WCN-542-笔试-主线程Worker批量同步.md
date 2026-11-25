---
title: [WCN-542] 笔试：实现「主线程视图信号 ↔ Worker 计算图」的批量消息同步（转移数组 + 版本号）。
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-542：笔试：实现「主线程视图信号 ↔ Worker 计算图」的批量消息同步（转移数组 + 版本号）。

**答**：
- 结论：主线程把多次写聚合成批次，用 transferable 转移 typed array 减少拷贝；每条消息带版本号。
- Worker 回传同样带版本号，主线程丢弃过期结果防竞态。
- 批量窗口用 rAF 或微任务，避免高频输入打爆 postMessage。
- 追问：Worker 崩溃如何降级？（答：超时检测，回退到主线程同步计算图）

```javascript
function bridgeToWorker(worker, sourceSig, viewSig) {
  const buf = []; let ver = 0, scheduled = false;
  sourceSig.subscribe(v => {
    buf.push(v);
    if (scheduled) return; scheduled = true;
    queueMicrotask(() => {
      const arr = new Float64Array(buf), batchVer = ++ver;
      buf.length = 0; scheduled = false;
      worker.postMessage({ type: 'batch', arr, ver: batchVer }, [arr.buffer]); // 转移所有权
    });
  });
  worker.onmessage = ({ data }) => { if (data.ver >= ver) viewSig.set(data.result); };
  return { dispose: () => worker.terminate() };
}
```

**评分点**：
- 批量聚合 + transferable 转移
- 版本号丢弃过期结果
- 微任务窗口防高频
- Worker 超时降级
