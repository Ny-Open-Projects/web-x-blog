---
title: [PER-309] SRI 上 CDN 场景如何协同？发布时序错开导致校验失败的工程怎么治？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-309：SRI 上 CDN 场景如何协同？发布时序错开导致校验失败的工程怎么治？

**答**：
- 失败场景：HTML 引用 `app.js` + integrity(v1)，发布时先传了新 app.js(v2)、HTML 还没更新（CDN 缓存）——线上拿到新文件旧哈希，全站脚本加载失败。SRI 把"字节一致性"从 CDN 的软承诺变成硬校验，时序问题被放大成故障。
- 治理三板斧：① 文件名带内容 hash（`app.8f3c.js`），HTML 引用永远指向唯一版本，CDN 上新旧文件并存——时序错开最多造成 404（回退加载旧 HTML 指向旧文件仍在）而不是校验失败；② 发布顺序：先传全部静态资源 → 资源探活（校验 CDN 返回字节 hash = 构建记录）→ 再更新 HTML；③ HTML 短缓存 + SWR，发布后主动预热新 HTML。
- 构建管线自动化：CI 里"构建 → 计算 hash → 上传 → 探活校验 → 生成带 integrity 的 HTML → 上传 HTML"，任何一步失败中止发布；哈希清单落盘（manifest.json）供回滚对账。
- 监控：`window.onerror` 监听 SRI 校验失败（事件 target 是 script 且无加载错误详情）→ 上报带当前 HTML 版本与资源 URL，区分"校验失败 vs 404 vs 网络错误"。

```text
安全发布流水线（每步可校验、可回滚）：
build → manifest.json { app.8f3c.js: sha384-CTkZ... } 
      → upload assets(CDN) → probe: GET each asset, hash(cdn bytes) === manifest ? ok : abort
      → render HTML(integrity from manifest) → upload html(SWR 60s) → warm new html
回滚 = 重新发布旧 manifest 对应的 HTML（旧 assets 仍在 CDN 未删）
SRI 失败监控：script.onerror + 尝试二次加载（去 integrity 的 fallback 仅限报告期使用）
```
