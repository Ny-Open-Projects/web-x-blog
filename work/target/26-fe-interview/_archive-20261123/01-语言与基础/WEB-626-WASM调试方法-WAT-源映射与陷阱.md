---
title: [WEB-626] WASM 调试方法：WAT、源映射与常见陷阱
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, WebAssembly]
type: 面试题
---

## WEB-626：WASM 调试方法：WAT、源映射与常见陷阱

**答**：
- 读 WAT：`wasm2wat` 把二进制转文本汇编，排查「为什么导出没找到/签名不匹配」最直接——JS import 的签名与 wasm 要求不一致会实例化直接失败
- 源映射：DWARF 调试信息编译进去（Rust `-g`，Emscripten `-g`），Chrome DevTools 可以在 wasm 帧上看到 C/Rust 源码与变量（0.5.x 起支持较好）；生产包要去掉调试段减体积
- 内存问题排查：越界写坏线性内存表现为「后续计算诡异出错」而非立即 trap——用 wasm 工具链的运行时检查（Rust debug 断言、ASan 类构建）在开发期抓
- 常见陷阱清单：字符串按字节长度不是字符数、grow 后视图失效、指针复用导致结果被覆盖、f64 精度与 JS Number 边界
- 调试技巧：在 wasm 侧留一个 debug_log 导出（用 host import 打 console），比反复导出中间结果高效

```bash
wasm2wat app.wasm -o app.wat   # 查看导出/导入签名
# Rust: cargo build --target wasm32-unknown-unknown -g
# DevTools → Sources → wasm 帧显示 Rust 源码
```
