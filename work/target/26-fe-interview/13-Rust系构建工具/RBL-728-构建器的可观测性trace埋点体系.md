---
title: [RBL-728] 构建器的可观测性：分布式 trace 埋点——把构建当成一次请求来追踪
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-728：构建器的可观测性：分布式 trace 埋点——把构建当成一次请求来追踪

**答**:
- 把构建当成一次分布式请求来追踪（OpenTelemetry 模式）：root span = 构建任务，子 span = 阶段（resolve/transform/chunk/codegen），孙 span = 单模块 transform——trace 视图直接展示「时间花在哪、哪个模块拖慢了哪个阶段」，比日志聚合强一个量级。
- 埋点设计原则：1) span 命名语义化（`module.transform: /src/a.ts`）带维度标签；2) **采样与开销**——全量 span 的内存/序列化成本可观，默认采样（慢 span 优先保留：耗时 P95 以上全保）+ 按需全量（debug 会话）；3) 属性裁剪（span 属性只放 id/hash 不放代码内容——隐私与体积）。
- 跨进程 trace 传播：Rust worker/子进程通过 traceparent 上下文传播——同一构建的 trace 在后端拼成完整树（CI 场景每构建一个 trace ID，关联 git commit/PR 元数据）。
- 消费场景：性能回归归因（RBL-587 的 profile 对比升级为 trace 对比——树形 diff 直接显示哪段子树变慢）；故障排查（构建失败的 trace 保留——失败 span 的错误事件携带诊断码）。
- 追问钩子：为什么构建 trace 不该复用日志系统？——日志是离散事件，trace 有因果与时长结构；「transform 3s 是因为它依赖的 resolve 2.8s」这种嵌套归因只有 trace 树能表达；两者互补（trace 定位结构、日志补充内容细节）。

```javascript
// OTel 式构建埋点
const tracer = otel.getTracer('rolldown');

async function tracedBuild(config, ctx) {
  return tracer.startActiveSpan('build', async (root) => {
    root.setAttribute('build.entry', config.entry);
    root.setAttribute('build.commit', ctx.commit);
    const resolve = tracer.startSpan('phase.resolve');
    const mods = await resolveAll(config, { span: resolve });
    resolve.end();
    const transforms = await Promise.all(mods.map(m =>
      tracer.startActiveSpan(`module.transform:${m.id}`, async (s) => {
        s.setAttribute('module.size', m.bytes);
        const out = await transform(m);
        if (out.ms > 500) s.recordException({ message: 'slow-transform' });   // 慢 span 标记
        s.end(); return out;
      })));
    root.end();
    return chunkify(transforms);
  });
}
// 采样策略
const sampler = otel.sampling.parentBased(
  otel.sampling.traceIdRatioBased(0.05),                 // 5% 常规采样
  { slow: otel.sampling.alwaysOn });                     // 慢构建全保
```
