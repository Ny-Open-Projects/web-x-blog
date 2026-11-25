---
title: [JS-421] 笔试：手写可取消的 fetch 组合（超时+去重+取消）
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## JS-421：笔试：手写可取消的 fetch 组合

**答**：实现 `smartFetch(url, init, { timeout, signal })`：① 三层取消源合并：调用方 signal + 超时 + 组件卸载信号；② 同 key 并发去重（进行中共享）；③ 超时用 AbortSignal.timeout 合并进链；④ 取消语义区分：AbortError（正常取消静默）与 TimeoutError（重试候选）；⑤ 错误对象带 { layer: 'timeout'|'abort'|'network'|'http' } 分类。写出实现。

```javascript
async function smartFetch(url, init = {}, { timeout = 5000, signal: callerSignal, dedupe = true } = {}) {
  const key = `${init.method || 'GET'} ${url}`;
  const sig = AbortSignal.any?.([
    ...(callerSignal ? [callerSignal] : []),
    AbortSignal.timeout(timeout),
  ]) ?? callerSignal;

  const exec = async () => {
    let res;
    try {
      res = await fetch(url, { ...init, signal: sig });
    } catch (e) {
      if (e.name === 'TimeoutError') throw Object.assign(e, { layer: 'timeout' });
      if (e.name === 'AbortError') throw Object.assign(e, { layer: 'abort' });
      throw Object.assign(e, { layer: 'network' });
    }
    if (!res.ok) throw Object.assign(new Error(`HTTP ${res.status}`), { layer: 'http', status: res.status });
    return res.json();
  };

  if (!dedupe || !(init.method || 'GET').match(/GET|HEAD/i)) return exec();
  inflightMap.set(key, inflightMap.get(key) ?? exec().finally(() => inflightMap.delete(key)));
  return inflightMap.get(key);
}
const inflightMap = new Map();

// 调用方语义处理
try {
  const data = await smartFetch('/api/feed', {}, { timeout: 3000, signal: unmountSignal });
} catch (e) {
  if (e.layer === 'timeout') scheduleRetry(e);   // 重试候选
  else if (e.layer === 'abort') {}               // 正常取消静默
  else showError(e);                             // network/http 展示
}
```

**评分点**：
- AbortSignal.any 合并多取消源（含 AbortSignal.timeout）
- 错误分层标注（layer 字段）供调用方语义分支
- AbortError 静默 vs TimeoutError 重试的区分
- GET 幂等才去重的约束
