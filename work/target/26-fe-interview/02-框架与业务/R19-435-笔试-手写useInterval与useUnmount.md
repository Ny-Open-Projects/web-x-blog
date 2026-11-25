---
title: [R19-435] 笔试：手写 useInterval / useUnmount / useAbortOnUnmount
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## R19-435：笔试：手写 useInterval 系列

**答**：实现：① `useInterval(cb, delay | null)`：delay=null 暂停；cb 永远最新（不重设定时器——经典 Dan 模式）；② `useUnmount(fn)`：卸载时调用（fn ref 化防闭包过期）；③ `useAbortOnUnmount()`：返回 controller ref + 卸载自动 abort——fetch 生命周期绑定；④ `useCounter(delay)`：组合示例。写出实现。

```javascript
export function useInterval(cb, delay) {
  const saved = useRef(cb);
  useEffect(() => { saved.current = cb; }, [cb]);     // cb 最新化
  useEffect(() => {
    if (delay == null) return;                        // null = 暂停
    const t = setInterval(() => saved.current(), delay);
    return () => clearInterval(t);                    // delay 变化重设/卸载清理
  }, [delay]);                                        // cb 不进 deps
}

export function useUnmount(fn) {
  const ref = useRef(fn);
  ref.current = fn;
  useEffect(() => () => ref.current(), []);           // 卸载时最新 fn
}

export function useAbortOnUnmount() {
  const ctrl = useRef(null);
  const getSignal = () => {
    ctrl.current?.abort();                            // 旧请求取消
    ctrl.current = new AbortController();
    return ctrl.current.signal;
  };
  useUnmount(() => ctrl.current?.abort());            // 卸载全取消
  return getSignal;
}

// 组合: 轮询 + 可取消
function usePolling(url, delay = 5000) {
  const [data, setData] = useState(null);
  const getSignal = useAbortOnUnmount();
  useInterval(async () => {
    try {
      const r = await fetch(url, { signal: getSignal() });
      setData(await r.json());
    } catch (e) { if (e.name !== 'AbortError') console.error(e); }
  }, delay);
  return data;
}
```

**评分点**：
- useInterval 的「cb 最新化 + delay 驱动」经典模式
- delay=null 暂停语义
- useUnmount 的 ref 化（防闭包过期）
- abort 与卸载生命周期绑定（请求泄漏防护）
