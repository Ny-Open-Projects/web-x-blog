---
title: [R19-430] 笔试：手写 useId 与 useImperativeHandle
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## R19-430：笔试：手写 useId 与 useImperativeHandle

**答**：实现：① useId：基于「fiber 树位置」生成稳定唯一 id（SSR/CSR 一致，前缀 :r0: 形态）——用「挂载计数器 + 树路径」模拟；② 同一次渲染内多次调用递增；③ useImperativeHandle(ref, create, deps)：deps 变化时更新 ref.current（暴露实例方法集），卸置 null；④ 与 forwardRef/ref prop 的配合。写出实现。

```javascript
let idCounter = 0;
function useId(prefix = ':r') {
  const hook = currentFiber.hookList[hookIndex] ??= { id: null };
  if (!hook.id) {
    // 简化: 全局计数器 + fiber 路径保证稳定(真实实现用树位置编码保证 SSR 一致)
    hook.id = `${prefix}${idCounter++}:`;
  }
  hookIndex++;
  return hook.id;
}
// SSR 一致的关键: 服务端与客户端按「相同树遍历顺序」编号
// 并发渲染下用「树位置」而非「调用计数」保证打断恢复后不漂移

function useImperativeHandle(ref, create, deps) {
  const hook = currentFiber.hookList[hookIndex] ??= { deps: undefined };
  const changed = !hook.deps || deps?.some((d, i) => !Object.is(d, hook.deps[i])) || !deps;
  if (changed) {
    if (ref.current) ref.current = null;             // 先清旧
    // 在 layout 时机设置(简化为同步)
    ref.current = create();                          // 暴露方法集
    hook.deps = deps;
  }
  // 卸载: 渲染器在卸载分支调用 ref.current = null
  hookIndex++;
}
// 用法
function Video({ ref }) {
  const inst = useRef(null);
  useImperativeHandle(ref, () => ({
    play: () => inst.current.play(),
    pause: () => inst.current.pause(),
  }), []);
  return <video ref={inst} />;
}
```

**评分点**：
- useId 稳定性来源（树位置 vs 调用计数）与 SSR 一致性
- useImperativeHandle 的 deps 比较（同 useMemo 逻辑）
- 卸载置 null 的清理语义
- 暴露方法集与命令式 API 边界
