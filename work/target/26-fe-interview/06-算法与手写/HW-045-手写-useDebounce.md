---
title: [HW-045] 手写 useDebounce
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-045：手写 useDebounce

**答**：
- 评分点：返回的是**延迟后的值**（与防抖函数相反——防抖防的是函数调用，useDebounce 防的是值更新），高频输入时下游昂贵渲染（如请求）只拿最终值；实现：state 保存 debounce 后的值 + useEffect 监听 value 变化 setTimeout 更新；**cleanup 里 clearTimeout 是精髓**——value 再变时上一轮定时器被取消，天然实现防抖；依赖数组 `[value, delay]` 必须写全；配套追问：useThrottledValue 用时间戳版实现。

```javascript
// ===== 5 分钟速写版 =====
function useDebounce(value, delay = 300) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer); // value 再变：取消上一轮，只剩最后一轮生效
  }, [value, delay]);
  return debounced;
}
// 用法：const kw = useDebounce(input, 400); useEffect(() => { search(kw) }, [kw])

// ===== 标准完整版（含边界处理）=====
function useDebouncePro(value, { delay = 300, leading = false } = {}) {
  const [debounced, setDebounced] = useState(value);
  const isFirst = useRef(true);
  useEffect(() => {
    // leading：首次挂载立即同步，不等 delay（首屏直接用初始值）
    if (leading && isFirst.current) {
      isFirst.current = false;
      setDebounced(value);
      return;
    }
    isFirst.current = false;
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);
  // 组件卸载时把最新值同步出去，避免最后一次输入丢失。
  // 注意不能写成 useEffect(() => () => setDebounced(value), [value])：
  // 那样每次 value 变化都会先执行 cleanup，把上一轮旧值刷进 state，防抖就失效了。
  // 用 ref 保存最新值 + 空依赖数组，保证 cleanup 只在卸载时执行。
  const latestRef = useRef(value);
  latestRef.current = value;
  useEffect(() => () => setDebounced(latestRef.current), []);
  return debounced;
}
// 节流值版（对照理解）：
function useThrottledValue(value, interval = 300) {
  const [throttled, setThrottled] = useState(value);
  const lastRef = useRef(0);
  const timerRef = useRef(null);
  useEffect(() => {
    const now = Date.now();
    const remain = interval - (now - lastRef.current);
    if (remain <= 0) {
      lastRef.current = now;
      setThrottled(value);
    } else if (!timerRef.current) {
      timerRef.current = setTimeout(() => {
        timerRef.current = null;
        lastRef.current = Date.now();
        setThrottled(value);
      }, remain);
    }
    return () => { if (timerRef.current) { clearTimeout(timerRef.current); timerRef.current = null; } };
  }, [value, interval]);
  return throttled;
}
// 追问：useDebounceValue 与「防抖搜索函数」的差异 —— 前者把防抖结果暴露为状态，
// 便于多个副作用共享；后者把逻辑封装进回调。两者都基于「定时器 + 清理」这一套。
```

---
