---
title: [RBL-929] 笔试：手写插件兼容层 Proxy 宿主（兼容等级 + 显式诊断）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-929：笔试：手写兼容层 Proxy 宿主（等级 + 诊断）

**答**：实现 `compatHost(plugin, impl, { levels, onDiag })`。levels: `Record<api, 'full'|'partial'|'unsupported'>`（缺省视为 unsupported——显式声明原则）。规则：1) api 在 impl → 返回实现（full）；2) levels[api] === 'partial' → 返回 impl 中的部分实现 + onDiag warn（每 api 只 warn 一次）；3) 'unsupported' 或未声明 → 调用时抛 Error 含诊断码 E9001；4) Proxy 的 get 惰性：未调用的 api 不触发诊断；5) 返回 host 对象（插件 this）。边界：plugin 无 this 依赖（host 空转）；onDiag 未提供默认 console.warn。

```javascript
function compatHost(impl = {}, { levels = {}, onDiag = (m) => console.warn(m) } = {}) {
  const warned = new Set();
  return new Proxy({}, {
    get(_, api) {
      if (api in impl) return impl[api];                // full 或 partial 实现
      const level = levels[api] ?? 'unsupported';
      if (level === 'unsupported')
        return () => { throw new Error(`E9001: this.${String(api)} 未实现（compat=unsupported）——查迁移指南`); };
      if (level === 'partial' && !warned.has(api)) {
        warned.add(api);
        onDiag(`this.${String(api)} 为部分兼容（partial）——行为差异见文档`);
      }
      return null;                                       // partial 缺实现兜底
    },
  });
}

// 自测
const diag = [];
const host = compatHost({
  resolve: async (id) => id + '!resolved',               // full 实现
  emitFile: () => 'partial-result',
}, {
  levels: {
    resolve: 'full', emitFile: 'partial',
    getCombinedSourcemap: 'unsupported',
  },
  onDiag: (m) => diag.push(m),
});

(async () => {
  console.log(await host.resolve('./a') === './a!resolved');   // full 直接用
  console.log(host.emitFile() === 'partial-result');
  console.log(diag.length === 1 && diag[0].includes('emitFile'));  // partial 一次性 warn
  console.log(diag.length === 1);                        // 再次访问不再 warn
  host.emitFile();
  console.log(diag.length === 1);

  let e; try { await host.getCombinedSourcemap(); } catch (x) { e = x; }
  console.log(/E9001/.test(e.message) && /getCombinedSourcemap/.test(e.message));

  // 未声明的 api 也是 unsupported
  e = null; try { await host.mysteryApi(); } catch (x) { e = x; }
  console.log(/E9001.*mysteryApi/.test(e.message));
})();
```

**评分点**：
- 惰性 Proxy（未调用不诊断）+ partial 一次性 warn（去重）；显式 unsupported 抛 E9001 含 api 名
- 缺省视为 unsupported（显式声明原则——未声明 API 不静默）；diag 回调注入可测
- full 实现优先于等级表；边界
- 能说清「兼容层静默 null 是最阴险 bug——显式 not-implemented 把不兼容变成可见诊断」属于加分
