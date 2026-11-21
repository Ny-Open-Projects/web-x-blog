---
title: [PER-591] 手写一个 JS chunk 加载失败的自愈加载器：动态 import 失败后刷新资源版本并重试
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-591：手写一个 JS chunk 加载失败的自愈加载器：动态 import 失败后刷新资源版本并重试

**答**：
- 场景：发版后旧 HTML 引用已删除的 chunk（懒加载路由 404），用户停留在旧页面点新路由时炸。自愈方案：捕获 chunk 加载错误 -> 请求最新资源清单 -> 更新 publicPath/重新拉取入口 -> 重试一次；重试仍失败才抛错。
- 要点：错误识别要用 `error.message` 匹配 `Loading chunk \d+ failed`；自愈动作带次数上限（1 次）与标记（localStorage 记录已自愈过，防止循环刷新）。
- 边界：清单请求自身失败要静默放弃；自愈后要上报事件让运维知道这类事故率。
- 评分点：错误识别、次数上限、防循环刷新。

```javascript

const healedKey = '__chunk_healed__';
async function safeImport(loader) {
  try {
    return await loader();
  } catch (err) {
    if (!/Loading chunk \d+ failed|ChunkLoadError/i.test(err.message)) throw err;
    if (localStorage.getItem(healedKey)) throw err;         // 已自愈过，不再循环
    localStorage.setItem(healedKey, '1');
    // 拉最新资源清单，更新运行时 base
    const manifest = await fetch('/asset-manifest.json', { cache: 'no-store' })
      .then(r => r.json()).catch(() => null);
    if (manifest) {
      window.__webpack_public_path__ = manifest.publicPath; // 更新 publicPath
      __webpack_require__.p = manifest.publicPath;          // webpack 运行时
    }
    reportEvent('chunk-selfheal', { manifest: !!manifest });
    return await loader();                                  // 重试一次
  }
}
// 路由注册处使用 safeImport(() => import('./detail'))
// localStorage 的 healed 标记在下次正常发版窗口清除
```
