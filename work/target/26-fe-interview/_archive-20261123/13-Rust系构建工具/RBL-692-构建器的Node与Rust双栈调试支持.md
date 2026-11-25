---
title: [RBL-692] 构建器的双栈调试：JS 插件断点、Rust panic 符号化与混合堆栈
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-692：构建器的双栈调试：JS 插件断点、Rust panic 符号化与混合堆栈

**答**:
- 构建器出问题时调试横跨两栈：JS 插件侧正常（IDE 断点/堆栈完整），Rust 侧 panic 需要符号化（RUST_BACKTRACE=1 + release 二进制带 debug symbols 剥离文件）；工具链要提供「一键符号化脚本」——发布产物保留 .dwp/symcache 供事后解析。
- 混合堆栈的呈现：NAPI 调用链上 panic 发生在 Rust 内，JS 侧看到的 Error 只有一行「native panic」——构建器的改进是 panic 拦截层：Rust panic 转 JS Error（带 Rust 堆栈摘要 + 诊断码 + 已知问题链接），而不是让 Node 直接 abort。
- JS 插件的调试支持：插件抛错时构建器输出「插件堆栈保留」（不吞 cause）、错误发生时的模块上下文（哪个模块的 transform 失败）、以及「禁用该插件重试」建议——把调试从「猜」变成「定位」。
- 混合执行的时间线可视化：构建 profile 输出「JS 钩子 vs Rust 阶段」的交替时间线（火焰图双色），性能问题一眼分清「JS 插件慢还是 Rust 慢」。
- 追问钩子：为什么 Rust panic 不该被静默 catch？——panic 是不变量破坏（程序进入未知状态），catch 后继续跑会产生错误产物；正确姿势是「panic → 结构化错误报告 → 快速失败」，把「catch 所有」留给明确的边界（单个模块 transform 失败可跳过，核心 panic 必须崩）。

```javascript
// panic 拦截层（NAPI 侧）
function wrapNative(fn) {
  return (...args) => {
    try {
      return fn(...args);
    } catch (e) {
      if (e?.code === 'RUST_PANIC') {
        e.message = `native panic: ${e.summary}\n堆栈摘要:\n${e.rustStack.slice(0, 8).join('\n')}\n已知问题: ${issueLink(e.summary)}`;
        e.diagnostics = { code: 'RBL9000', recoverable: false };
      }
      throw e;
    }
  };
}

// JS 插件错误上下文增强
try {
  await runPipeline(mod);
} catch (e) {
  e.context = {
    module: mod.id, pass: e.pass ?? 'unknown',
    suggestion: `尝试禁用插件 ${e.pluginName} 重跑（--disable-plugin=${e.pluginName}）`,
  };
  throw e;
}

// 双色火焰图时间线
// profile.flame = [
//   { span: [0, 120], kind: 'rust', label: 'resolve' },
//   { span: [120, 180], kind: 'js', label: 'plugin:react transform' },
//   { span: [180, 300], kind: 'rust', label: 'transform(parallel)' },
// ]
```
