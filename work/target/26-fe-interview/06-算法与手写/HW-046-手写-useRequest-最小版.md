---
title: [HW-046] 手写 useRequest 最小版
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-046：手写 useRequest 最小版

**答**：
- 评分点：管理三个状态 loading / data / error（每次请求开始 loading 置 true、清 error）；run 返回 Promise 供调用方 await；**竞态保护**是加分核心——用自增 requestId 标记，响应回来时只有最新一次才允许写入 state（旧请求晚到直接丢弃）；组件卸载后不能再 setState（用 ref 标记 mounted）；手动触发 run 而不是渲染即请求（可选 auto 参数演示立即执行）。

```javascript
// ===== 5 分钟速写版 =====
function useRequest(fn) {
  const [state, setState] = useState({ loading: false, data: null, error: null });
  const latestId = useRef(0);
  const run = useCallback(async (...args) => {
    const id = ++latestId.current;         // 竞态保护：只认最新请求
    setState({ loading: true, data: null, error: null });
    try {
      const data = await fn(...args);
      if (id !== latestId.current) return; // 旧请求晚到，丢弃
      setState({ loading: false, data, error: null });
      return data;
    } catch (e) {
      if (id !== latestId.current) return;
      setState({ loading: false, data: null, error: e });
      throw e;
    }
  }, [fn]);
  return { ...state, run };
}

// ===== 标准完整版（含边界处理）=====
function useRequestPro(fn, { manual = false, onSuccess, onError, defaultParams = [] } = {}) {
  const [state, setState] = useState({
    loading: manual === false, // auto 模式挂载即 loading
    data: null,
    error: null
  });
  const latestId = useRef(0);
  const mountedRef = useRef(true);
  const fnRef = useRef(fn);
  fnRef.current = fn; // 每次渲染同步最新 fn，避免闭包旧值（React 官方推荐范式）
  useEffect(() => {
    mountedRef.current = true;
    return () => { mountedRef.current = false; }; // 卸载标记
  }, []);
  const run = useCallback(async (...args) => {
    const id = ++latestId.current;
    if (mountedRef.current) setState(s => ({ ...s, loading: true, error: null }));
    try {
      const data = await fnRef.current(...args);
      if (id !== latestId.current || !mountedRef.current) return data; // 过期/已卸载：不写 state
      setState({ loading: false, data, error: null });
      onSuccess && onSuccess(data);
      return data;
    } catch (e) {
      if (id !== latestId.current || !mountedRef.current) throw e;
      setState({ loading: false, data: null, error: e });
      onError && onError(e);
      throw e;
    }
  }, []);
  useEffect(() => {
    if (!manual) run(...defaultParams); // auto 模式：挂载即请求
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  const cancel = useCallback(() => {
    // 逻辑取消：提升 id，让在途响应全部过期
    latestId.current++;
    if (mountedRef.current) setState(s => ({ ...s, loading: false }));
  }, []);
  return { ...state, run, cancel };
}
// 追问：
// 1. 竞态场景 —— 输入快速变化连续请求，慢的旧响应覆盖新结果；解决：id 标记 / AbortController / SwitchMap 思想
// 2. 为什么用 fnRef —— useCallback 依赖 fn 会频繁换引用，ref 让 run 永远调用最新逻辑
```

---
