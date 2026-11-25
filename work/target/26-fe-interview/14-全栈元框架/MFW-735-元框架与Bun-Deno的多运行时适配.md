---
title: [MFW-735] Bun/Deno 多运行时适配
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-735：Bun/Deno 多运行时适配

**答**:
- 元框架的多运行时：1) **Bun**（Node 兼容层——大部分 Node API 可用 + 更快的启动（原生编译——bun 的 runtime 快于 node）；2) **Deno**（Web 标准 API——Node 兼容层（node: 前缀——Deno 的 Node 适配）；3) **适配层的差异**：fs API（Bun 原生快/Deno 兼容层）、进程管理（Bun spawn 快/Deno 子进程权限）、crypto（三者不同实现）。
- 元框架的适配策略：**运行时检测**（process.versions.bun / globalThis.Deno → 运行时分支）+ **Web 标准 API 优先**（Request/Response/ReadableStream——所有 runtime 统一的 API 面）；「Web 标准优先」的适配哲学（Remix 的 Web 标准主义 RBL-534——Request/Response 是所有 runtime 的公共语言）。
- 性能差异的实测口径（RBL-951 宏基准原则）：冷启动 Bun < Node；请求吞吐 Bun ≈ Node；内存 Bun < Node——「实测数据驱动选型」而非 benchmark 广告。
- 追问钩子：为什么「Web 标准 API 优先」是多运行时的唯一可行适配策略？——Node API 在 Bun/Deno 的兼容度不同（Bun 高兼容/Deno 部分兼容）；Web 标准（fetch/ReadableStream/URL）= 所有 runtime 的最大公约数；「适配层的公共语言」：用 Web 标准写的代码无需修改即可跑在任何 runtime（RBL-530 Nitro 的 adapter 哲学——运行时差异被标准化 API 吸收）。

```typescript
// 运行时检测与适配
const runtime = (() => {
  if (typeof Bun !== 'undefined') return 'bun';
  if (typeof Deno !== 'undefined') return 'deno';
  return 'node';
})();
// Web 标准 API 优先（Request/Response）
export default {
  async fetch(req: Request): Promise<Response> {        // Web 标准——所有 runtime 通用
    const data = await fetchData(req.url);              // 内部用标准 fetch
    return new Response(JSON.stringify(data), {
      headers: { 'content-type': 'application/json' },
    });
  },
};
// 运行时特化（仅在必要时）
if (runtime === 'bun') {
  // Bun 的优化路径：Bun.serve / Bun.file（更快）
} else {
  // Node/Deno 的标准路径
}
// Nitro 的运行时适配（RBL-530）
// nitro.config: { preset: 'bun' }  或 'deno-server'  或 'node-server'
```
