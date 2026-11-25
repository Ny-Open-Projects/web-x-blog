---
title: [RBL-501] napi-rs 的线程边界：JS 主线程与 Rust 线程池怎么通信
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-501：napi-rs 的线程边界：JS 主线程与 Rust 线程池怎么通信

**答**：
- Node 的 native addon 约束：**JS 主线程只有一个**（libuv 事件循环），Rust 侧的重活必须放到独立线程——napi-rs 提供三种通信模式：1) **同步调用**（当前线程执行，阻塞事件循环——只适合 <1ms 的短操作，如 hash）；2) **AsyncTask**（Rust 线程池执行，完成后回主线程调 JS 回调——Rspack 的编译主流程）；3) **ThreadsafeFunction**（Rust 侧任意线程随时回调 JS——loader/插件回调通道）。
- Rspack 的架构落位：JS 侧调用 `rspack.build()` → napi AsyncTask 进入 Rust 多线程编译 → 构建完成通过 ThreadsafeFunction 把 artifacts 序列化回 JS。**JS 与 Rust 之间只传序列化数据**（跨桥传对象成本高），loader 内容的往返是主要桥成本。
- 线程边界纪律：Rust 侧可多线程并行（Rayon），但「碰 JS 数据」的临界区必须回主线程——所以 napi 桥的吞吐 = 主线程回调频率上限，高频小回调（每模块一次）会成为瓶颈，批量回传是优化手段。
- 追问钩子：为什么 Rspack loader 生态兼容 webpack 但慢于此预期？——JS loader 每次调用都要跨桥两次（JS in / JS out），「Rust 引擎 + JS 插件」的混合架构里桥是第一成本，这也是 Rolldown 推原生 loader 的动机。

```javascript
// napi-rs 三种通信模式（概念代码）
#[napi]
pub fn hash_sync(input: Buffer) -> String {          // ① 同步：阻塞主线程，<1ms 场景
  sha256(input.as_ref())
}

#[napi]
pub async fn build_async(options: BindOptions) -> Result<Bindings> {  // ② AsyncTask：线程池
  let result = tokio::task::spawn_blocking(move || compile(options)).await??;
  Ok(result)                                          // 完成后自动回主线程
}

#[napi(ts_return_type = "void")]
pub fn register_loader(cb: JsFunction) {              // ③ ThreadsafeFunction：任意线程回调 JS
  let tsfn: ThreadsafeFunction<String> = cb
    .create_threadsafe_function(0, |ctx| Ok(vec![ctx.env.to_string(&ctx.value)?]))?;
  LOADER_TSFN.set(tsfn);
}
// JS 侧：loader 内容跨桥成本 = 序列化 + 主线程回调排队
// 优化：批量回传（一次回调带 N 个模块结果）减少主线程唤醒次数
```
