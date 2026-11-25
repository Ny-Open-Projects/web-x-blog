---
title: [MFW-196] 笔试：手写流式渲染 deadline 兜底（超时切静态壳）
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-196：笔试：手写流式渲染 deadline 兜底（超时切静态壳）
**答**：流式 SSR 中，慢依赖（如推荐服务 8s）会拖死首屏。实现带 deadline 的分段流式：① 整页设 deadline（如 4s），超时后仍未完成的段**放弃数据渲染，改输出静态兜底内容**（如默认推荐位/骨架），绝不无限等待；② 已完成的段照常输出（先到的先 flush）；③ 每段支持单独超时（段级 > 整页级）；④ 兜底内容要标注（`data-degraded`），前端与监控能识别降级；⑤ 取消：用户断连（request abort）时停止所有待渲染任务。

```ts
type Segment = { name: string; render: () => Promise<string>; fallback: string; timeout: number };

export async function streamPage(segments: Segment[], deadlineMs: number, signal: AbortSignal) {
  const DEADLINE = Date.now() + deadlineMs;
  const write = (s: string) => process.stdout.write(s); // 简化：真实场景写 res

  write('<main>');
  await Promise.all(segments.map(async (seg) => {
    const budget = Math.min(seg.timeout, Math.max(1, DEADLINE - Date.now())); // ③ 段级与整页取小
    try {
      const html = await Promise.race([
        seg.render(),
        new Promise<never>((_, rej) =>
          setTimeout(() => rej(new Error('timeout')), budget)),
      ]);
      if (signal.aborted) throw new DOMException('aborted', 'AbortError'); // ⑤ 断连
      write(segHtml(seg.name, html, false));
    } catch (e) {
      if ((e as Error).name === 'AbortError') throw e;      // ⑤ 断连直接终止整页
      write(segHtml(seg.name, seg.fallback, true));          // ①② 超时兜底，不拖死整页
    }
  }));
  write('</main>');
}

function segHtml(name: string, html: string, degraded: boolean) {
  return degraded
    ? `<section data-seg="${name}" data-degraded="true">${html}</section>` // ④ 标注降级
    : `<section data-seg="${name}">${html}</section>`;
}
```

**评分点**：
1. `Promise.race` + 取小后的预算：段级超时与整页剩余 deadline 联动，晚到的段预算自然缩短。
2. 并行分段渲染、先完成先写：保证慢段不影响快段输出（流式的意义所在）。
3. 超时走兜底而不是报错，且带 `data-degraded` 标注——监控与前端可识别降级状态。
4. abort 语义正确：用户断连时抛 AbortError 终止整页，防止继续消耗服务端资源。
5. 能提到兜底段后续可补流（SSR 降级后客户端再拉一次真实数据替换），体现端到端思维。
