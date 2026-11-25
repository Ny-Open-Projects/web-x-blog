---
title: [R19-443] 笔试：手写 useWorker（React 版 Worker hook）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 性能]
type: 笔试题
---

## R19-443：笔试：手写 useWorker

**答**：实现 `useWorker(workerUrl)`：① 返回 { run, status, result }——run(payload) 返回 Promise（reqId 关联）；② Worker 懒创建（首次 run 才 new）+ 复用（不重复创建）；③ 超时取消（terminate 重建——任务不可恢复时丢弃 Worker）；④ 卸载 terminate + pending reject；⑤ status: idle/running/done/error。写出实现。

```javascript
export function useWorker(workerUrl, { timeout = 30_000 } = {}) {
  const workerRef = useRef(null);
  const pendingRef = useRef(new Map());
  const [status, setStatus] = useState('idle');
  const [result, setResult] = useState(null);
  const seqRef = useRef(0);

  function ensureWorker() {
    if (workerRef.current) return workerRef.current;
    const w = new Worker(workerUrl);
    w.onmessage = ({ data: { id, ok, result: r } }) => {
      const p = pendingRef.current.get(id);
      if (!p) return;
      pendingRef.current.delete(id);
      clearTimeout(p.timer);
      ok ? p.resolve(r) : p.reject(new Error(r));
      if (!pendingRef.current.size) setStatus('idle');
    };
    workerRef.current = w;
    return w;
  }

  const run = useCallback((payload, transfer = []) => {
    const w = ensureWorker();
    const id = ++seqRef.current;
    setStatus('running');
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => {
        pendingRef.current.delete(id);
        // 超时: Worker 可能卡死 → terminate 重建
        w.terminate(); workerRef.current = null;
        setStatus('error');
        reject(new Error('worker timeout'));
      }, timeout);
      pendingRef.current.set(id, { resolve, reject, timer });
      w.postMessage({ id, payload }, transfer);
    }).then((r) => { setResult(r); return r; });
  }, [workerUrl, timeout]);

  useEffect(() => () => {                              // 卸载
    workerRef.current?.terminate();
    for (const p of pendingRef.current.values()) { clearTimeout(p.timer); p.reject(new Error('unmounted')); }
    pendingRef.current.clear();
  }, []);
  return { run, status, result };
}
```

**评分点**：
- 懒创建 + 复用（首次 run 才 new）
- reqId 关联的 Promise 化（并发任务安全）
- 超时 terminate 重建（卡死 Worker 恢复）
- 卸载清理（terminate + pending reject）
