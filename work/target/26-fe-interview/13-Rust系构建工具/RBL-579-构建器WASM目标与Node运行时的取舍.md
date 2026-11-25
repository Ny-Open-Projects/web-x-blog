---
title: [RBL-579] WASM 版构建器：同一份 Rust 代码跑浏览器与 Node 的取舍
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-579：WASM 版构建器：同一份 Rust 代码跑浏览器与 Node 的取舍

**答**：
- Rust 工具链编译到 wasm32-wasi 后可在浏览器/受限环境运行（swc-wasm、rolldown-wasm 的存在理由：无原生二进制平台、在线 IDE（StackBlitz/WebContainer）、跨平台一致性测试）。核心取舍是**性能与能力的让步**：wasm 比 native 慢 2~10 倍，无直接线程（需要 SharedArrayBuffer + COOP/COEP 头）、文件系统是虚拟的。
- IO 边界重构：native 版直接 syscall 读文件，wasm 版要把 FS 调用抽象成 trait——Node 下走 NAPI 直连 fs，浏览器下走虚拟 FS（内存 FS 或 IndexedDB backed）；这决定了代码结构必须「核心纯计算 + IO 依赖注入」，否则 wasm 移植寸步难行。
- 内存模型差异：wasm 线性内存有上限且增长昂贵（内存副本），arena 分配器在大仓库场景要限制规模；JS↔wasm 边界传递大数据（源码字符串）要过 TextEncoder/UTF-8 转换，比 native NAPI 更贵——所以 wasm 版接口粒度更粗（一次构建一个调用，而非逐模块）。
- 实战用法：CI 一致性验证（native 与 wasm 各跑一遍对比产物 hash，验证跨平台确定性）；浏览器内构建场景（教学/演示/沙箱执行不可信代码）。
- 追问钩子：wasm-bindgen 与 NAPI 的边界数据模型差异——wasm-bindgen 用 JS 对象代理 + boxing，NAPI 用线程安全引用；高频小调用在两者都贵，所以「批处理接口」设计（一次传一批模块）是通用优化。

```javascript
// 双后端 IO 抽象（Rust trait 概念 + JS 消费视角）
// Rust 侧：
// trait FileSystem { fn read(&self, p: &Path) -> io::Result<Vec<u8>>; fn write(...); }
// NativeFs / VirtualFs(wasm) 两个实现，build(fs: impl FileSystem) 通用

// JS 侧选择后端
import { build, NodeFs, MemFs } from 'rolldown-wasm';

// Node：fs 直连（NAPI 快路径）
await build({ fs: NodeFs, input: 'src/index.ts' });

// 浏览器：内存虚拟 FS（源码来自在线 IDE 的编辑器 state）
const vfs = new MemFs({ '/src/index.ts': editor.getValue('/src/index.ts') });
const out = await build({ fs: vfs, input: '/src/index.ts' });   // 无磁盘参与

// CI 一致性验证
const a = await build({ fs: NodeFs, hashOnly: true });
const b = await build({ fs: NodeFs, backend: 'wasm', hashOnly: true });
if (a.hash !== b.hash) throw new Error('跨后端产物不一致——确定性破坏');
```
