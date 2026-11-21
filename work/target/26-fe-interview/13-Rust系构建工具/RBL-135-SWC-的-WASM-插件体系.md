---
title: [RBL-135] SWC 的插件体系：WASM 插件与生态限制
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-135：SWC 的插件体系：WASM 插件与生态限制

**答**：
- SWC 插件是编译成 WASM 的 Rust 库，实现 `ParsedAst` 上的 visitor，在 transform 阶段被宿主加载执行；加载开销小、可跨工具复用。
- 与 Babel 插件的本质差异：Babel 插件是 JS 函数（visitor 对象）直接操作 JS AST；SWC 插件跑在 WASM 沙箱里，通过 host binding 访问 AST，开发调试成本更高。
- 限制：WASM 内不能直接访问 Node API（fs/network），纯 AST 变换没问题，"读配置文件/发请求"类插件做不了；部分复杂 Babel 插件语义（macros、path 依赖分析）难以 1:1 迁移。
- Rspack 对 swc 插件另有实验性支持（experimental.builtinSwcLoader / plugin 通道），实际项目里更多选择用 Rspack 自身 loader/plugin 承接非编译类逻辑。
- 追问钩子：迁移评估先做插件清单盘点——纯语法类可迁 SWC，工程类（自动埋点注入依赖运行时上下文）考虑换成构建器 plugin 或 babel 双轨。

```rust
// SWC Rust 插件骨架（编译为 wasm32-wasip1 后在 .swcrc 的 jsc.experimental.plugins 引用）
use swc_core::ecma::{ast::Program, visit::FoldWith};
use swc_core::plugin::{plugin_transform, proxies::TransformPluginProgramMetadata};

#[plugin_transform]
pub fn remove_console(program: Program, _m: TransformPluginProgramMetadata) -> Program {
    program.fold_with(&mut as_folder(|expr: &mut Expr| {
        if let Expr::Call(call) = expr {
            if is_console_call(call) { *expr = Expr::Invalid(Invalid { span: DUMMY_SP }); }
        }
    }))
}

// .swcrc 中启用：
// "jsc": { "experimental": { "plugins": [["swc-plugin-remove-console", {}]] } }
```
