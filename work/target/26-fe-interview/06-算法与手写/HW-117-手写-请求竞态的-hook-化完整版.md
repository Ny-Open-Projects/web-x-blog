---
title: [HW-117] 手写竞态防护完整版——序号丢弃 + Abort 双保险 + 最后结果缓存与卸载保护
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-117：手写竞态防护完整版——序号丢弃 + Abort 双保险 + 最后结果缓存与卸载保护
**答**：HW-050 的工程完整版：三层防护——① AbortController 取消在途请求（省资源）；② 序号比对丢弃过期响应（Abort 可能不被支持的兜底）；③ 卸载后不再 setState（cancelled 标志）；④ 缓存最后成功结果（输入回退到旧值时秒显示）。

```javascript
function useRaceSafeFetch() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const cache = useRef(new Map());          // key -> result
  const seq = useRef(0), ctrl = useRef(null), mounted = useRef(true);

  useEffect(() => () => { mounted.current = false; ctrl.current?.abort(); }, []);

  async function run(key, url) {
    if (cache.current.has(key)) { setData(cache.current.get(key)); return; }   // 缓存命中秒回
    seq.current++;
    const mySeq = seq.current;
    ctrl.current?.abort();
    ctrl.current = new AbortController();
    setLoading(true);
    try {
      const res = await fetch(url, { signal: ctrl.current.signal });
      const json = await res.json();
      if (seq.current !== mySeq || !mounted.current) return;    // 过期/卸载：丢弃
      cache.current.set(key, json);
      setData(json);
    } catch (e) {
      if (e.name === 'AbortError') return;                      // 被新请求取消：静默
      if (seq.current === mySeq && mounted.current) setData({ __error: String(e) });
    } finally {
      if (seq.current === mySeq && mounted.current) setLoading(false);
    }
  }
  return { data, loading, run };
}
// 三层防护缺一不可：Abort 省资源；seq 兜底兼容性；mounted 防 setState-on-unmounted
// 缓存：输入从 "ab" 回退到 "a" 时命中缓存秒显示
```

**评分点**：
- Abort + 序号 + 卸载标志三层防护缺一不可，并说清各自防什么。
- 缓存最后结果（回退输入秒显示）是体验加分项。
- AbortError 与真错误分流。
- finally 中条件复位 loading（过期请求不关掉新请求的 loading）。
