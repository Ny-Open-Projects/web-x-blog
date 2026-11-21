---
title: [RBL-032] 如何编写带异步逻辑的 Rspack 插件？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-032：如何编写带异步逻辑的 Rspack 插件？
**答**：
- 三种 tap：同步 tap(name, fn)、tapAsync(name, (args, cb) => …)、tapPromise(name, async (args) => …)，与 tapable 语义一致；有 IO 的钩子必须用异步注册，否则顺序错乱。
- 高频异步场景：emit 前上传产物到 CDN、构建后写 manifest 到远端、拉取远程配置注入。
- 常见坑：用 tap 注册了异步函数（返回 Promise 被忽略）导致钩子提前完成——报错不明显但产物不全；async 回调忘记调用 cb 导致构建挂起。
- 钩子选择：传产物→emit / afterEmit；注入模块→make 前的 compilation.hooks.additionalAssets 或 entry 补充；统计→done。
- Rspack 差异：部分钩子只支持同步 tap，需要查文档确认；异步支持集中在 emit/done/watchRun 等主流程钩子。
- 追问钩子：异步插件失败要让构建失败（cb(err)），吞错是最常见的线上事故。

```javascript
class UploadPlugin {
  apply(compiler) {
    // tapPromise：emit 前上传 sourcemap 到符号服务
    compiler.hooks.emit.tapPromise('UploadPlugin', async (compilation) => {
      const maps = Object.keys(compilation.assets).filter(n => n.endsWith('.map'));
      await Promise.all(maps.map(n => uploadToSentry(compilation.assets[n])));
      // 上传失败要抛出，让构建失败
    });
  }
}
async function uploadToSentry(asset) {
  const res = await fetch('https://sentry/api/files', { method: 'POST', body: asset });
  if (!res.ok) throw new Error(`upload failed: ${res.status}`);
}
module.exports = UploadPlugin;
```
