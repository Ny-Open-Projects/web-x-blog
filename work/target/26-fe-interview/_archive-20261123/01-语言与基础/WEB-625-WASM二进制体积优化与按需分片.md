---
title: [WEB-625] WASM 二进制体积优化与按需分片
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, WebAssembly]
type: 面试题
---

## WEB-625：WASM 二进制体积优化与按需分片

**答**：
- 编译期裁剪：Rust `opt-level=z` + `wee_alloc`、`panic=abort`；C/C++ `-Os` + 关闭异常/RTTI；链接时 LTO + `--gc-sections` 去死代码
- wasm-opt 再压：Binaryen 的 `wasm-opt -Oz` 通常再省 10~30%；产物 gzip/brotli 后传输体积往往只有裸 wasm 的 1/3~1/2（wasm 可压缩性高）
- 按需分片：大 SDK（如完整 ffmpeg.wasm）按功能拆多模块（core/codec-x/codec-y），核心首载、编解码器按任务动态 instantiate——对应用户「只用一个功能却下全量」的浪费
- 加载体验：wasm 下载期间 UI 提示 + 骨架，`instantiateStreaming` 并行编译；模块缓存放 IndexedDB 二次启动免编译
- 体积红线实践：核心 wasm >1.5MB 就要触发拆分评审；SDK 形态对外交付时给体积承诺

```javascript
// 按需分片: 用到哪种编解码再载哪个模块
const codecCache = new Map();
async function getCodec(name) {
  if (!codecCache.has(name)) {
    const { instance } = await WebAssembly.instantiateStreaming(
      fetch(`/wasm/codec-${name}.wasm`), {});
    codecCache.set(name, instance.exports);
  }
  return codecCache.get(name);
}
// 转码任务: await getCodec('h264') — 未用到的编解码器永不下载
```
