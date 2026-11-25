---
title: [RBL-610] Transform 管线的有序合成：TS→JSX→polyfill 的顺序敏感与过滤器
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-610：Transform 管线的有序合成：TS→JSX→polyfill 的顺序敏感与过滤器

**答**：
- 单模块的 transform 是多 pass 合成：`TS 剥离 → JSX/装饰器 → 语法降级 → polyfill 注入 → import 重写`。顺序错误的经典事故：先 polyfill 后降级（降级产物丢了 polyfill 依赖）、TS 转换在 JSX 前（tsx 里类型注解干扰 JSX 解析）——管线要按「语法层 → 类型层 → 目标层」分层排序，构建器内置顺序固定，用户插件钩子在关键节点插入。
- 过滤器（filter）是性能关键：每个 transform 都要声明作用范围（id 正则/扩展名/语言类型），无关模块零成本跳过——大仓库里 1000 个模块 × 10 个 transform，没有过滤就是 1 万次「解析后发现不适用」的浪费。
- pass 间的数据传递：现代设计是「单 AST 多 pass」（OXC 式，见 RBL-559）而非「字符串 → AST → 字符串」往返；每 pass 声明读/写的 AST 区域，调度器做冲突检测（两 pass 改同一节点 → 合并或告警）。
- 错误传播与定位：pass 抛错要带上「pass 名 + 模块 + span」的结构化上下文（RBL-568 诊断体系）；pass 失败策略可选跳过（继续后续 pass）或中断——默认中断（半转换产物更危险）。
- 追问钩子：为什么「语法降级」必须在「类型剥离」后？——TS 的 enum/namespaces/类字段语义转换会产生降级器未覆盖的语法；反过来降级器输出若再遇 TS 语法也会崩——分层顺序是语义依赖而非偏好。

```javascript
// 管线定义与调度
const PIPELINE = [
  { name: 'strip-ts', filter: /\.(ts|tsx)$/, run: stripTS },      // 类型层
  { name: 'jsx', filter: /\.(jsx|tsx)$/, run: transformJSX },     // 语法层
  { name: 'downlevel', filter: /\.(js|jsx|ts|tsx)$/, run: downlevel }, // 目标层
  { name: 'polyfill', filter: /\.(js|jsx|ts|tsx)$/, run: injectPolyfill },
];

async function runPipeline(mod, passes) {
  let ast = parse(mod.code, { lang: mod.lang });
  for (const pass of passes) {
    if (!pass.filter.test(mod.id)) continue;           // 过滤：无关 pass 零成本
    const t0 = performance.now();
    try {
      ast = await pass.run(ast, mod);                  // 单 AST 多 pass
    } catch (e) {
      throw enrich(e, { pass: pass.name, module: mod.id });  // 结构化上下文
    }
    mod.profile.push({ pass: pass.name, ms: performance.now() - t0 });
  }
  return codegen(ast);
}
// 内置顺序固定，插件只能挂到 hook 点（beforePass/afterPass），不能打乱分层
```
