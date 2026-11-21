---
title: [PER-274] React 应用有哪些典型内存泄漏点？useEffect 清理不到位如何系统性治理？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-274：React 应用有哪些典型内存泄漏点？useEffect 清理不到位如何系统性治理？

**答**：
- 泄漏点清单：① useEffect 里订阅事件/定时器/Observer 没 return cleanup；② state 里塞了 DOM 节点或大对象，组件卸载不清空；③ ref.current 指向已卸载 DOM；④ 全局事件（window resize）在组件里 add 没有 remove；⑤ Provider 缓存累积（Context 里塞 Map 不清）；⑥ 异步请求 setState 在卸载后执行（泄漏副作用较小，但会造成 stale 闭包持有大 props/state）。
- 系统治理：① 评审 checklist 把"useEffect 必须审视 cleanup"定为卡点；② 封装 useEventListener/useInterval/useObserver 等内部 hook，把解绑逻辑强制内置，业务无法写出无清理版本；③ 状态审计——state 只放"渲染必需"数据，大原始数据放 ref/Worker。
- 验证工具：严格模式下 double-mount 能提前暴露缺 cleanup 的 effect（开发期泄漏翻倍）；配合 PER-266 的 detached 检测做线上回归。

```jsx
// 强制内置清理的自定义 hook：业务方没有"忘写 cleanup"的机会
function useInterval(callback, ms) {
  const ref = useRef(callback);
  useEffect(() => { ref.current = callback; }, [callback]);
  useEffect(() => {
    const t = setInterval(() => ref.current(), ms);
    return () => clearInterval(t);          // 内置清理，无法遗漏
  }, [ms]);
}
function useEventListener(target, type, handler, opts) {
  const ref = useRef(handler);
  useEffect(() => { ref.current = handler; }, [handler]);
  useEffect(() => {
    target.addEventListener(type, (e) => ref.current(e), opts);
    return () => target.removeEventListener(type, ref.current, opts);
  }, [target, type]);
}
// 反例（评审必拦）：useEffect(() => { window.addEventListener('resize', onResize); }, []) —— 无 return
```
