---
title: [SCN-577] 验证组件在 SSR/首屏场景的兼容怎么做？为什么不能服务端渲染验证器？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-577：验证组件 SSR 兼容怎么做？
**答**：
- 占位与水合：验证器只能在客户端挂载（依赖 DOM 事件/指纹 API），SSR 输出占位容器 + 骨架，水合后再挂载；避免 hydration mismatch 用 `mounted` 门控。
- 关键路径延迟意识：登录页的验证器是首屏交互必需——chunk 预取 + 占位可交互（先出「准备中」按钮）。
- 指纹 API 的 SSR 边界：采集层全部 `typeof window !== 'undefined'` 守卫，服务端调用直接返回空信号并标注 serverSide。
- 双端一致性测试：SSR 快照测试保证占位输出稳定，避免每次渲染随机 ID 导致 mismatch。
- 追问钩子：占位期间用户点击怎么办——占位按钮 disable + tooltip「安全组件加载中」，或先走服务端可判定的无感通道。

```javascript
export function RiskSlot({ scene }) {
  const [ready, setReady] = useState(false);
  useEffect(() => {                                // 客户端挂载
    riskGuard.mount({ scene, el: ref.current }).then(() => setReady(true));
  }, [scene]);
  return (
    <div ref={ref} data-ssr-placeholder="risk">
      {!ready && <button disabled title="安全组件加载中">验证准备中…</button>}
    </div>
  );
}
// 采集层守卫
export const signals = typeof window === 'undefined'
  ? { serverSide: true }                            // SSR 空信号
  : collector.snapshot();
```
